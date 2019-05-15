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
new_lines1='''c      8 - boron frits-baryte concrete
c      9 - borosilicate glass'''
#
new_lines2='''c 110    7 -0.0001785 -11 13 -17 19 23 -25 #199            imp:n,p=1      $backfill - helium
c 110    9 -2.230     -11 13 -17 19 23 -25 #199            imp:n,p=1      $backfill - borosilicate glass'''
#
new_lines3='''       56138.66c -0.401300
c      ---
c
c      ---
c      borosilicate glass - 2.230 g/cc
c      ---
M9     5011.70c      -0.040066
       8016.70c      -0.539559
       11023.70c     -0.028191
       13027.70c     -0.011644
       14000.70c     -0.377220
       19000.70c     -0.003321'''
###
#
old_lines1='c      8 - boron frits-baryte concrete'
#
old_lines2='c 110    7 -0.0001785 -11 13 -17 19 23 -25 #199            imp:n,p=1      $backfill - helium'
#
old_lines3='       56138.66c -0.401300'
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
mcnp_tempfile=mcnp_tempfile.replace(old_lines1,new_lines1)
mcnp_tempfile=mcnp_tempfile.replace(old_lines2,new_lines2)
mcnp_tempfile=mcnp_tempfile.replace(old_lines3,new_lines3)
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
