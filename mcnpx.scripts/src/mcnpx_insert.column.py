########################################################################
# R.A.Borrelli
# @TheDoctorRAB
# rev.28.January.2016
########################################################################
#
# Inserts a column of text into existing tab delimited file.
#
########################################################################
#
#
#
####### 
#
# imports
#
import os
import numpy
from sys import argv
script,mcnpx_output,text_input=argv
#
########################################################################
#
#
#
####### 
#
# open files
#
mcnpx_file=numpy.loadtxt(mcnpx_output,dtype=str) 
input_file=numpy.loadtxt(text_input) 
output_file_name=os.path.basename(mcnpx_output)
#
#######
#
# read number of lines in the input file 
#
i=0
for line in input_file:
    i=i+1
# end i
#
#######
#
# add data column
#
for j in range(0,i):
    mcnpx_file[j,0]=input_file[j]
# end j
#
#######
#
# save file
#
numpy.savetxt(output_file_name,mcnpx_file,fmt='%s',delimiter='\t')
#
########################################################################
#
# EOF
#
########################################################################
