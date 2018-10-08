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
c      cooling fluid
c      ---
M3     1001.70c    -0.111894           $H
       8016.70c    -0.888106           $O
c      ---
c
c      ---
c      stainless steel 316
c      ---
M4     14000.42c   -0.010000           $Si
       24000.42c   -0.170000           $Cr
       25055.70c   -0.020000           $Mn
       26000.42c   -0.655000           $Fe
       28000.42c   -0.120000           $Ni
       42000.42c   -0.025000           $Mo
c      ---'''
#
###
#
old_lines='''
c      stainless steel 316
c      ---
M3     14000.42c   -0.010000           $Si
       24000.42c   -0.170000           $Cr
       25055.70c   -0.020000           $Mn
       26000.42c   -0.655000           $Fe
       28000.42c   -0.120000           $Ni
       42000.42c   -0.025000           $Mo
c      ---
c
c      ---
c      cooling fluid
c      ---
M4     1001.70c    -0.111894           $H
       8016.70c    -0.888106           $O
c      ---'''
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
