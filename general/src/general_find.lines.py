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
import os
from sys import argv
script,input_file=argv
#
#######
#
# get current directory
#
dir_path=os.getcwd()
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
# open file to write line numbers
#
line_number_output=open('line_numbers.out','a+')
#
#######
#
# find line numbers
#
for find_line_number1,line in enumerate(tempfile,1): # use 1 to give vim line number
    if find_lines1 in line:
        print find_line_number1,'          ',find_lines1
        line_number1=find_line_number1
###
for find_line_number2,line in enumerate(tempfile,1): # use 1 to give vim line number
    if find_lines2 in line:
        print find_line_number2,'          ',find_lines2
        line_number2=find_line_number2
#
#######
#
# write line numbers
#
line_number_output.write(str.format('%s'%dir_path)+'\t'+str.format('%.0f'%line_number1)+'\t'+str.format('%.0f'%line_number2)+'\n')
#
#
#######
#
# close file
#
line_number_output.close()
#
#######
#
# EOF
#
#######
