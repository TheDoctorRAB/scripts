#######
# @TheDoctorRAB
#######
#
# finds the line number for a string
#
#######
#
# imports
#
from sys import argv
script,input_file=argv
#
#######
#
# set lines to find
#
find_lines1=''
#
find_lines2=''
#
#######
#
# open the mcnp deck and read
# this is ok because the input files for mcnp are small for memory
#
tempfile=open(input_file,'r').readlines()
#
#######
#
# find line numbers
#
for line_number1,line in enumerate(tempfile,1):
    if find_lines1 in line:
        print find_lines1,'   ',line_number1
###
for line_number2,line in enumerate(tempfile,1):
    if find_lines2 in line:
        print find_lines2,'   ',line_number2
#
#######
#
# EOF
#
#######
