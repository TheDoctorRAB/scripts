########################################################################
# R.A.Borrelli
# @TheDoctorRAB
# rev.05.June.2014
########################################################################
# This script edits the particle history (NPS) for an input deck.
# The text to be replaced is 'NPS    NUMBER'.
# The number of spaces is important because MCNPX is FORTRAN.
########################################################################
#
#
####### imports
from sys import argv
script,mcnp_input=argv
#######
#
####### Set up first part of line
NPS_header='NPS    '
#######
#
####### Get the NPS
NPS_history=open('nps.inp','r').read()
#######
#
####### Combine the header and history strings
NPS_new=NPS_header+NPS_history+'\n'
#######
#
####### open mcnp input file
mcnp_infile=open(mcnp_input,'r')
#######
#
####### Find the original NPS
for line in mcnp_infile:
  if 'NPS' in line:
    NPS_old=line
# endif  
# end line
#######
#
####### Close the mcnp input file
mcnp_infile.close()
#######
#
####### Open the mcnp input file and read
# This is ok because the input files for mcnp are small for memory
mcnp_tempfile=open(mcnp_input,'r').read()
#######
#
####### Replace the NPS 
mcnp_tempfile=mcnp_tempfile.replace(NPS_old,NPS_new)
#######
#
####### Write the file
open(mcnp_input,'w').write(mcnp_tempfile)
#######
#
#
########################################################################
#      EOF
########################################################################
