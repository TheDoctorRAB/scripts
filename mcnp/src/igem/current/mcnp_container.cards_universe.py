#######
# @TheDoctorRAB
#######
#
# edits a given set of lines in the input file
# number of spaces is important because MCNP is FORTRAN
# probably not the most elegant
#
#######
#
# imports
#
from sys import argv
script,inputfile=argv
#
#######
#
# set the lines to be edited
#
new_lines='999    0  100:101:-102  imp:n,p=0'
#
###
#
old_lines='999    0        -10:14:-16:20:-22:26   imp:n,p=0'
#
#######
#
# open the mcnp deck and read
# this is ok because the input files for mcnp are small for memory
#
tempfile=open(inputfile,'r').read()
#
#######
#
# replace
#
tempfile=tempfile.replace(old_lines,new_lines)
#
#######
#
# write the file
#
open(inputfile,'w').write(tempfile)
#
########################################################################
#
# EOF
#
########################################################################
