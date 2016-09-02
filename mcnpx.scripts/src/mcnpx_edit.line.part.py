########################################################################
# R.A.Borrelli
# @TheDoctorRAB
# rev.05.June.2014
########################################################################
# Replace part of a line in a file.  
# The number of spaces is important because MCNPX is FORTRAN.
########################################################################
#
#
####### imports
import fileinput
from sys import argv
script,mcnp_input=argv
#######
#
####### Get the line to insert
edit_line=open('edit.inp','r').read()
#######
#
####### Get the line to replace
replace_line=open('replace.inp','r').read()
#######
#
####### open mcnp input file
mcnp_infile=open(mcnp_input,'r')
#######
#
for line in fileinput.FileInput(mcnp_infile,inplace=1):
    line=line.replace(replace_line,edit_line)
# end line
#######
#
#
########################################################################
#      EOF
########################################################################
