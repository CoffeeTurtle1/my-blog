# Calcu-16 ISA
<h3>2019 01 09</h3>

As you know I have been making a 16-bit processor (that I have creatively named
Calcu-16 /s) in Verilog to gain experience before going on to design a RISC-V
based processor. My next step will be to design the instruction set, that is
what this blog post is about.

Calcu-16 is almost complete. The only thing I need to add to it is an I/O
system; at this point I don't fully understand how modern processors handle
I/O.

## Registers
Calcu-16 has eight **general purpose** registers r0-r7. Each register is 16-bits
wide. There are three other registers, the IR (**I**nstruction **R**egister
26-bit), the PC (**P**rogram **C**ounter 16-bit) and the carry register
(1-bit). 

## Instruction formats
### Register Format
```
0:3     4:6 7:9 10:12
op-code registers       unused
 │           │              │
┌┴─┐ ┌───────┴─┐ ┌──────────┴┐
0000 000 000 000 0000000000000
     └┬┘ └┬┘ └┬┘
     r1  r2  r3
```

### Immediate/Memory Format
```
0:3     4:6   7:9 10:25
op-code registers immediate/addr
 │        │        │
┌┴─┐ ┌────┴┐ ┌─────┴────────┐
0000 000 000 0000000000000000
     └┬┘ └┬┘
     r1  r2
```

## Instructions
|Instruction           | Op-Code | Format    | Description                                   |
|----------------------|---------|-----------|-----------------------------------------------|
|nop                   |0000     |N/A        |Does nothing.                                  |
|add reg1, reg2, reg3  |0001     |Register   |Adds reg2 to reg3. Stores the result in reg1.  |
|addi reg1, reg2, Imm  |0010     |Immediate  |Adds reg3 to Imm. Stores the result in reg1.   |
|jmp addr              |0011     |Memory     |Sets the PC to the value of addr.              |
|jeq reg1, reg2, addr  |0100     |Memory     |If reg1 = reg2 then jump to addr.              |
|store reg1, addr      |0101     |Memory     |Store reg1 at addr.                            |
|load reg1, addr       |0110     |Memory     |Load reg1 with the value stored at addr.       |
|xor reg1, reg2, reg3  |0111     |Register   |XOR reg2 and reg3 put the result in reg2.      |
|and reg1, reg2, reg3  |1000     |Register   |AND reg2 and reg3 put the result in reg2.      |
|jc addr               |1001     |Memory     |If the carry flag is set jump to addr.         |

Calcu-16 has no subtract function because you can add signed negative numbers for
subtraction.