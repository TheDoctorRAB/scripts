########################################################################
# @TheDoctorRAB
########################################################################
# This finds and writes/prints the final estimated keff and error.
########################################################################
#
#
####### imports
import os
from sys import argv
script,mcnp_output=argv
#######
#
####### open mcnp output file
mcnp_file=open(mcnp_output,'r').readlines()
#######
#
#######
#
####### initialize the counter
i=0
#######
#
####### search the file for thekeff estimate
# line will write the current line
# mcnp_file[i] writes the next line (if needed)
#
for line in mcnp_file:
  i=i+1
  if '  | the final estimated' in line:
    print line
#
#######
#EOF
#######
