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
import numpy
from sys import argv
script,mcnp_output=argv
#
#######
#
# open mcnp output file
#
mcnp_file=open(mcnp_output,'r').readlines()
#
#######
#
# get number of lines in each file
# with mcnp each file has a different number of lines
#
totlines=len(mcnp_file)
#
######
#
# find EOF flag
#
print mcnp_file[totlines-5]
#
#######
# EOF
#######
