########################################################################
# R.A.Borrelli
# @TheDoctorRAB
# rev.21.December.2015
########################################################################
# This script edits a given line for an input deck.
# The number of spaces is important because MCNPX is FORTRAN.
########################################################################
#
#
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
# set the line to be edited
#
new_line='       OMIT=1 6 6014 7016 8018 9018 91230 95240'+'\n'
#
#######
# 
# open mcnp deck
#
mcnp_infile=open(mcnp_input,'r')
#
#######
# 
# find the original line
#
for line in mcnp_infile:
  if 'OMIT' in line:
    old_line=line
# endif  
# end line
#
#######
# 
# close mcnp deck
#
mcnp_infile.close()
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
mcnp_tempfile=mcnp_tempfile.replace(old_line,new_line)
#
#######
#
# write the file
#
open(mcnp_input,'w').write(mcnp_tempfile)
#
########################################################################
#
# EOF
#
########################################################################
