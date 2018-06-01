########################################################################
# R.A.Borrelli
# @TheDoctorRAB
# rev.08.May.2014
########################################################################
# This script inserts the dose card.
# When I build my decks I leave a marker for the dose card.
# This just finds the marker and replaces it with the dose card.
# The number of spaces is important because MCNPX is FORTRAN.
########################################################################
#
#
####### imports
from sys import argv
script,mcnp_input=argv
#######
#
####### assign the dose card
# FYI these are just the standard defaults
# edit here for anything different
dose_card='DF0    IU 2 FAC 1 LOG IC 10'+'\n'
#######
#
####### open mcnp input file
mcnp_infile=open(mcnp_input,'r')
#######
#
####### Find dose marker
for line in mcnp_infile:
  if 'dose' in line:
    dose_marker=line
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
####### Replace the dose marker with the dose card 
mcnp_tempfile=mcnp_tempfile.replace(dose_marker,dose_card)
#######
#
####### Write the file
open(mcnp_input,'w').write(mcnp_tempfile)
#######
#
########################################################################
#      EOF
########################################################################
