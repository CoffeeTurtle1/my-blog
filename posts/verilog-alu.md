# Learning Verilog and implementing an ALU
<h3>2018 12 21</h3>

I decided it would be cool to implement a [**RISC-V**](https://riscv.org/)
processor in Verilog. This is the first post documenting that journey.

My first step is to learn Verilog. To help me learn this I am going to
implement a simple processor so that I can get used to how it works. So far I
have made a four function ALU (arithmetic logic unit). It takes in four inputs
"a", "b", "select" and "enable". "select" selects the operation to preform on
"a" and "b". "enable" enables output.

Here is the code for the ALU module.
```verilog
// ALU
module alu (
    input [0:15] a,
    input [0:15] b,
    input [0:2]  select,
    input enable,
    output [0:15] out,
    output carry
);
    reg [0:15] result;
    wire [0:16] tmp;

    assign tmp = {1'b0, a} + {1'b0, b};
    assign carry = tmp[16];
    assign out = result;

    always @(posedge enable) begin
        case (select)
            3'b000:
                result = a + b;
            3'b001:
                result = a - b;
            3'b010:
                result = a ^ b;
            3'b011:
                result = a & b;
        endcase
    end
endmodule
```

Here is code for the test bench.
```verilog
// Test bench
module alu_tb;
    reg [0:15] A, B;
    reg [0:2] select;
    reg en;
    wire [0:15] result;
    wire carry;

    alu alu_1(
        .a(A),
        .b(B),
        .select(select),
        .enable(en),
        .out(result),
        .carry(carry) 
    );

    initial begin
        $monitor("enable=%b a=%b b=%b \nselect=%b result=%b carry=%b\n\n",
                en, A, B, select, result, carry);
        A = 2;
        B = 2;
        en = 1;
        select = 0;
        #5
        en = 0;
        en = 1;
        select = 1;
        #5
        en = 0;
        en = 1;
        select = 2;
        #5
        en = 0;
        en = 1;
        select = 3;
    end
endmodule
```

Once compiled and simulated I get this output.
```
enable=1 a=0000000000000010 b=0000000000000010 // Add
select=000 result=0000000000000100 carry=0


enable=1 a=0000000000000010 b=0000000000000010 // Sub
select=001 result=0000000000000000 carry=0


enable=1 a=0000000000000010 b=0000000000000010 // XOR
select=010 result=0000000000000000 carry=0


enable=1 a=0000000000000010 b=0000000000000010 // AND
select=011 result=0000000000000010 carry=0
```