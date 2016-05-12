########################################################################
# R.A.Borrelli
# @TheDoctorRAB
# rev.28.January.2016
########################################################################
#
# Inserts burnup into the file containing radionuclide mass from BURN.
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
script,mcnpx_output,burnup_input=argv
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
burnup_file=numpy.loadtxt(burnup_input,dtype=str) #make sure to use the correct dirpath on the command line
output_file_name=os.path.basename(mcnpx_output)
#
#######
#
# read number of lines in the input file 
#
i=0
for line in burnup_file:
    i=i+1
# end i
#
#######
#
# add data column
#
for j in range(0,i):
    mcnpx_file[j,2]=burnup_file[j,8] #column 2 in the radionuclide content file only holds zaid 
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
