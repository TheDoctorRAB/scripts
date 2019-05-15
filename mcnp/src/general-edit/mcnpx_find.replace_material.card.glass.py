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
# there are a set of comibinations for bare or concrete design
#
new_lines1='''c      7 - cladding gap
c      9 - borosilicate glass'''
# new_lines1='''c      8 - boron frits-baryte concrete
# c      9 - borosilicate glass'''
#
new_lines2='''c 110    7 -0.0001785 -11 13 -17 19 23 -25 #199            imp:n,p=1      $backfill - helium
110    9 -2.230     -11 13 -17 19 23 -25 #199            imp:n,p=1      $backfill - borosilicate glass'''
#
new_lines3='''M7     2004.70c    -1.0                $He
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
# new_lines3='''       56138.66c -0.401300
#c      ---
#c
#c      ---
#c      borosilicate glass - 2.230 g/cc
#c      ---
#M9     5011.70c      -0.040066
#       8016.70c      -0.539559
#       11023.70c     -0.028191
#       13027.70c     -0.011644
#       14000.70c     -0.377220
#       19000.70c     -0.003321'''
#
new_lines4='c 110    5 -0.001205  -11 13 -17 19 23 -25 #199            imp:n,p=1      $backfill - air'
# new_lines4='c 110    3 -1.00      -11 13 -17 19 23 -25 #199            imp:n,p=1      $backfill - water'
###
#
old_lines1='c      7 - cladding gap'
#old_lines1='c      8 - boron frits-baryte concrete'
#
old_lines2='c 110    7 -0.0001785 -11 13 -17 19 23 -25 #199            imp:n,p=1      $backfill - helium'
# old_lines2='110    7 -0.0001785 -11 13 -17 19 23 -25 #199            imp:n,p=1      $backfill - helium'
#
old_lines3='M7     2004.70c    -1.0                $He'
# old_lines3='       56138.66c -0.401300'
#
old_lines4='110    5 -0.001205  -11 13 -17 19 23 -25 #199            imp:n,p=1      $backfill - air'
# old_lines4='110    3 -1.00      -11 13 -17 19 23 -25 #199            imp:n,p=1      $backfill - water'
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
mcnp_tempfile=mcnp_tempfile.replace(old_lines1,new_lines1)
mcnp_tempfile=mcnp_tempfile.replace(old_lines2,new_lines2)
mcnp_tempfile=mcnp_tempfile.replace(old_lines3,new_lines3)
mcnp_tempfile=mcnp_tempfile.replace(old_lines4,new_lines4)
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
