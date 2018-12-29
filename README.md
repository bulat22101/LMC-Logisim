# LMC-Logisim
Emulating little man computer 

Supported operations
add 10xxxx add the value stored at xxxx to whatever value is currently on the accumulator
sub 20xxxx subtract the value stored at xxxx from whatever value is currently on the accumulator
sta 30xxxx store the contents of the accumulator at xxxx
lda 50xxxx load the value stored at xxxx and enter it in the accumulator
bra 60xxxx set the program counter to the given address
brz 70xxxx if the accumulator contains the value 000000, set the program counter to the value xxxx
brp 80xxxx if the accumulator contains the value >=0, set the program counter to the value xxxx
inp 900000 add value stored at xxxx input accumulator value
out a00000 add value stored at xxxx output accumulator value

LMC.circ - model in Logisim 
main.py - simple compiler
