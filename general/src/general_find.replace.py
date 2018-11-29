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
new_lines='annotate_y4=0.15'
#
###
#
old_lines='annotate_y4=1.1'
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
