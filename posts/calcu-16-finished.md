# Calcu-16 Finished
<h3>2019-01-18</h3>
Calcu-16 is a processor I have been working on for the last few weeks to help me
learn verilog. 

At first the plan was to make a module for each part of the processor and
attach them together in a core module but I couldn't get it to work. The
problem was that if I attach the output of the register module to input *a* (or
*b*) of the alu module, the output of the alu becomes *x*. This only happened
when one output of the register module was 0. You can see my first attempt on  
[GitHub](https://github.com/CoffeeTurtle1/Calcu-16/tree/master/old_attempt).

As a result of this problem I decided to start again with a simpler design. I
ended up making more of an emulator than a complete 'hardware model'. The
entire design is only 90 lines long, where as the original was around about 250
lines of code.

I also wrote a terrible 'assembler' in python. At some point I might come back
to it and rewrite the assembler in C++ and use flex to make a proper lexer.

You can see the source code [here](https://github.com/CoffeeTurtle1/Calcu-16).
There are instructions in the readme for how to run a program on Calcu-16 if
you want to try it out yourself.

Thanks for reading.
