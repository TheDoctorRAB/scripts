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
script,mcnp_input=argv
#
#######
#
# set the lines to be edited
#
new_lines='''
c      cladding gap
c      ---
M7     2004.70c    -1.0                $He
c      ---
c
c      ---
c      boron frits-baryte concrete
c      ---
M8     1001.66c  -0.005600
       5011.66c  -0.010400
       8016.66c  -0.338000
       9019.66c  -0.002300
       11023.66c -0.012100
       12000.66c -0.002300
       13027.66c -0.006400
       14000.60c -0.033100
       16000.66c -0.091500
       19000.66c -0.001000
       20000.66c -0.062600
       25055.66c -0.000200
       26000.50c -0.021900
       30000.42c -0.006600
       56138.66c -0.401300'''
#
###
#
old_lines='c      cladding gap'
#
#######
#
# open the mcnp deck and read
# this is ok because the input files for mcnp are small for memory
#
mcnp_tempfile=open(mcnp_input,'r').read()
#
#######
#
# replace
#
mcnp_tempfile=mcnp_tempfile.replace(old_lines,new_lines)
#
#######
#
# write the file
#
open(mcnp_input,'w').write(mcnp_tempfile)
#
#######
#
# EOF
#
#######
