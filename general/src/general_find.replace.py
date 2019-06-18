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
# new_lines1="annotate_title2='Water-Glass backfill'"
# new_lines2='annotate_x=23'
# new_lines3='annotate_x2=23'
# new_lines4='annotate_x3=23'
# new_lines5='ymax=2200'
new_lines6='annotate_y=1000'
new_lines7='annotate_y2=700'
new_lines8='annotate_y3=400'
# new_lines9='annotate_x4=23'
# new_lines10='ymin=0.1'
#
###
#
# old_lines1="annotate_title2='Water backfill'"
# old_lines2='annotate_x=25'
# old_lines3='annotate_x2=25'
# old_lines4='annotate_x3=25'
# old_lines5='ymax=1500'
old_lines6='annotate_y=1700'
old_lines7='annotate_y2=1400'
old_lines8='annotate_y3=1100'
# old_lines9='annotate_x4=24'
# old_lines10='ymin=1'
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
# mcnp_tempfile=mcnp_tempfile.replace(old_lines1,new_lines1)
# mcnp_tempfile=mcnp_tempfile.replace(old_lines2,new_lines2)
# mcnp_tempfile=mcnp_tempfile.replace(old_lines3,new_lines3)
# mcnp_tempfile=mcnp_tempfile.replace(old_lines4,new_lines4)
# mcnp_tempfile=mcnp_tempfile.replace(old_lines5,new_lines5)
mcnp_tempfile=mcnp_tempfile.replace(old_lines6,new_lines6)
mcnp_tempfile=mcnp_tempfile.replace(old_lines7,new_lines7)
mcnp_tempfile=mcnp_tempfile.replace(old_lines8,new_lines8)
# mcnp_tempfile=mcnp_tempfile.replace(old_lines9,new_lines9)
# mcnp_tempfile=mcnp_tempfile.replace(old_lines10,new_lines10)
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
