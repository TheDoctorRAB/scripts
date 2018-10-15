#######
# @TheDoctorRAB
#######
#
# edits a given set of lines in the input file
# number of spaces is important because MCNP is FORTRAN
# probably not the most elegant
#
#######
#
# imports
#
from sys import argv
script,inputfile=argv
#
#######
#
# set the lines to be edited
#
new_lines='''c      window for lattice is the fuel block given in 78 - 81
c      ---
c      end
c      ---
c
c      ---
c      container
c      ---
100    c/z 17.159 17.159 50.630                       $container - radius + container thickness and changes with plate thickness
101    pz  436.0                                      $cap - surface 26 + container thickness
102    pz -26.0                                       $plug - surface 22 - container thickness'''
#
###
#
old_lines='c      window for lattice is the fuel block given in 78 - 81'
#
#######
#
# open the mcnp deck and read
# this is ok because the input files for mcnp are small for memory
#
tempfile=open(inputfile,'r').read()
#
#######
#
# replace
#
tempfile=tempfile.replace(old_lines,new_lines)
#
#######
#
# write the file
#
open(inputfile,'w').write(tempfile)
#
########################################################################
#
# EOF
#
########################################################################
