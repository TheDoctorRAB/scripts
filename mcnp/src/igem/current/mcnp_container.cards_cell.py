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
new_lines='''c      container
c      ---
400    8 -3.10 (-10:14:-16:20) -100  22 -26   imp:n,p=1 VOL=4.51992e+05   $container - change volume with plate thickness
401    8 -3.10                 -100  26 -101  imp:n,p=1                   $container cap
402    8 -3.10                 -100 -22  102  imp:n,p=1                   $container plug
c      ---
c      end
c      ---
c
c      ---
c      end cask'''
#
###
#
old_lines='c      end cask'
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
