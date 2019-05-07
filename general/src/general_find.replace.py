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
new_lines1='''c 104    5 -0.001205  -93 94 -95 96       u=2 imp:n,p=1                            $air cell with no fuel
c 104    3 -1.00      -93 94 -95 96       u=2 imp:n,p=1                            $water cell with no fuel
104    7 -0.0001785 -93 94 -95 96       u=2 imp:n,p=1                            $helium cell with no fuel
c      ---
c      0,0,0 is NW on VISED but for cartesian x,y,z it is SW
c      important for SDEF source particle designation
c      ---
105    0 -93  94 -95  96                u=3 lat=1 fill=0:16 0:16 0:0
       1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
       1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
       1 1 1 1 1 2 1 1 2 1 1 2 1 1 1 1 1
       1 1 1 2 1 1 1 1 1 1 1 1 1 2 1 1 1
       1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
       1 1 2 1 1 2 1 1 2 1 1 2 1 1 2 1 1
       1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
       1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
       1 1 2 1 1 2 1 1 2 1 1 2 1 1 2 1 1
       1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
       1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
       1 1 2 1 1 2 1 1 2 1 1 2 1 1 2 1 1
       1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
       1 1 1 2 1 1 1 1 1 1 1 1 1 2 1 1 1
       1 1 1 1 1 2 1 1 2 1 1 2 1 1 1 1 1
       1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
       1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
       imp:n,p=1'''
#
new_lines2='199    0  78 -79  80 -81  82 -83                 fill=3    imp:n,p=1      $lattice window'
#
###
#
old_lines1='104    0  82 -83 -93  94 -95  96       u=2 lat=1 fill=1    imp:n,p=1      $lattice unit cell'
#
old_lines2='199    0  78 -79  80 -81  82 -83                 fill=2    imp:n,p=1      $lattice window'
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
