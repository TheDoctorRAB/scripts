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
new_lines='''c      FC2    west plate
c      F2:N   10
c      C2     0 1 T
c      ---'''
new_lines2='c      FC12   east plate'
new_lines3='c      F12:N  14'
new_lines4='''c      C12    0 1 T
c      ---'''
new_lines5='''c      FC22   south plate
c      F22:N  16
c      C22    0 1 T
c      ---
c      FC32   north plate
c      F32:N  20
c      C32    0 1 T
c      ---
c      FC42   cap
c      F42:N  26
c      C42    0 1 T
c      ---
c      FC52   plug
c      F52:N  22
c      C52    0 1 T
c      ---
FC62   container surface
F62:N  100
C62    0 1 T
c      ---
FC72   container top
F72:N  101
C72    0 1 T
c      ---
FC82   container bottom
F82:N  102
C82    0 1 T'''
#
###
#
old_lines='''FC2    west plate
F2:N   10
C2     0 1 T
c'''
###
#
# there is a weird white space on F12:N that I cannot seem to get around
#
old_lines2='FC12   east plate'
old_lines3='F12:N  14'
old_lines4='''C12    0 1 T
c'''
###
#
old_lines5='''FC22   south plate
F22:N  16
C22    0 1 T
c
FC32   north plate
F32:N  20
C32    0 1 T
c      ---
FC42   cap
F42:N  26
C42    0 1 T
c      ---
FC52   plug
F52:N  22
C52    0 1 T'''
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
tempfile=tempfile.replace(old_lines2,new_lines2)
tempfile=tempfile.replace(old_lines3,new_lines3)
tempfile=tempfile.replace(old_lines4,new_lines4)
tempfile=tempfile.replace(old_lines5,new_lines5)
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
