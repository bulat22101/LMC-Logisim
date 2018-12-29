# LMC-Logisim
Emulating little man computer 
<br/>
<br/>Supported operations
<ol>
<li>add 10xxxx add the value stored at xxxx to whatever value is currently on the accumulator</li>
<li>sub 20xxxx subtract the value stored at xxxx from whatever value is currently on the accumulator</li>
<li>sta 30xxxx store the contents of the accumulator at xxxx</li>
<li>lda 50xxxx load the value stored at xxxx and enter it in the accumulator</li>
<li>bra 60xxxx set the program counter to the given address</li>
<li>brz 70xxxx if the accumulator contains the value 000000, set the program counter to the value xxxx</li>
<li>brp 80xxxx if the accumulator contains the value >=0, set the program counter to the value xxxx</li>
<li>inp 900000 add value stored at xxxx input accumulator value</li>
<li>out a00000 add value stored at xxxx output accumulator value</li>
</ol>
<br/>
LMC.circ - model in Logisim 
<br/>
main.py - simple compiler
