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
new_lines1='annotate_x=26'
new_lines2='annotate_y=2500'
new_lines3='annotate_x2=26'
new_lines4='annotate_y2=1500'
new_lines5='annotate_x3=26'
new_lines6='annotate_y3=700'
new_lines7='annotate_x4=24'
new_lines8='annotate_y4=0.2'
#new_lines9='ymax=13000'
#
###
#
old_lines1='annotate_x=25'
old_lines2='annotate_y=2700'
old_lines3='annotate_x2=25'
old_lines4='annotate_y2=1700'
old_lines5='annotate_x3=25'
old_lines6='annotate_y3=900'
old_lines7='annotate_x4=21'
old_lines8='annotate_y4=0.15'
#old_lines9='ymax=12000'
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
tempfile=tempfile.replace(old_lines1,new_lines1)
tempfile=tempfile.replace(old_lines2,new_lines2)
tempfile=tempfile.replace(old_lines3,new_lines3)
tempfile=tempfile.replace(old_lines4,new_lines4)
tempfile=tempfile.replace(old_lines5,new_lines5)
tempfile=tempfile.replace(old_lines6,new_lines6)
tempfile=tempfile.replace(old_lines7,new_lines7)
tempfile=tempfile.replace(old_lines8,new_lines8)
#tempfile=tempfile.replace(old_lines9,new_lines9)
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
