#######
# @TheDoctorRAB
#######
#
# checks to make sure the mcnp run completed
#
#######
#
# imports
#
import os
from sys import argv
script,mcnp_output=argv
#
#######
#
# get current directory
#
dir_path=os.getcwd()
#
#######
#
# open mcnp output file
#
mcnp_file=open(mcnp_output,'r').readlines()
#
#######
#
# open file to write status check
#
status_check_output=open('status_check.out','a+')
#
# get number of lines in each file
# with mcnp each file has a different number of lines
#
totlines=len(mcnp_file)
#
######
#
# write status check
#
status_check_output.write(str.format('%s'%dir_path)+'\t'+str.format('%s'%mcnp_file[totlines-5])+'\n')
#
#######
#
# close file
#
status_check_output.close()
#
#######
# EOF
#######
