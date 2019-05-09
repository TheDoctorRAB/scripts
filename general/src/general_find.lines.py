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
find_lines1='SDEF   POS d1 ERG d2              $SP1 has to have the same number of entries as sources'
#
find_lines2='SP1    1 1444R'
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
for line_number1,line in enumerate(tempfile,1): # use 1 to give vim line number
    if find_lines1 in line:
        print find_lines1,'   ',line_number1
###
for line_number2,line in enumerate(tempfile,1): # use 1 to give vim line number
    if find_lines2 in line:
        print find_lines2,'   ',line_number2
#
#######
#
# EOF
#
#######
