# -*- coding: utf-8 -*-
"""
MCNP Lattice helper code
--for defining ksrc in square lattice structure
--generates a text document that can be pasted directly
  in to ksrc portion of MCNP code

@author: James
"""
import numpy as np
import cStringIO

#number of rows and columns
nRow = 82
nCol = 82


#number of sources to appear on one line of code
nSrc = 4

#pitch
p = 1.1 #cm

#IO to write MCNP code to .txt file
output = cStringIO.StringIO()

#assumes first source is at origin
x = 0
y = 0
z = 0



#Keeps track of when to insert newline in to code output
newLineCounter = 1

for i in range(0,nCol):
    if x != 0:
        output.write("\nc\n")
        output.write("c   ---Row " + str(i+1) + " ---\n")
        output.write("c\n       ")
        y = y + p
    x = 0
    for j in range(0,nRow):
        output.write(str(x) + " " + str(y) + " "+ str(z) + "   ")

        if newLineCounter == nSrc or j == 82:
            #sends MCNP code to the next line
            output.write("   \n       ")
            newLineCounter = 0
        newLineCounter = newLineCounter + 1
        x = x + p

#write output to file
fd= open("C:\Users\James\Documents\GitHub\\450_Project\Python Scripts\lattice.txt", "w")
fd.write(output.getvalue())
output.close()
