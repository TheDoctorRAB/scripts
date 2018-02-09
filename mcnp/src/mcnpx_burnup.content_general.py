########################################################################
# R.A.Borrelli
# @TheDoctorRAB
# rev.27.December.2015
########################################################################
# 
# Searches each of the burnup data and finds the keff and associated burnup closest to critical
# Pulls the keff and burnup from the partial table 210 from BURN card
# Run mcnpx_general.burnup first
# Writes a new file with keff and burnup
# New file first column is blank so thorium content can be entered
#
########################################################################
#
#
#
####### 
#
# imports
#
import os
import numpy
from sys import argv
script,mcnpx_output=argv
#
########################################################################
#
#
#
#######
#
# time and content steps
#
content_steps=20 #thorium content from 0.00 to 0.95
time_steps=40 # not time=0
#
#######
#
# open mcnpx output file
#
mcnpx_file=numpy.loadtxt(mcnpx_output)
#
#######
# 
# open the new data file for writing
#
content_burnup_file=open('burnup.content.out','a')
#
#######
#
# initialize keff array
#
keff_comparison=numpy.zeros((time_steps))
#
#######
#
# search the file
#
for i in range(0,time_steps):
    keff_comparison[i]=abs(mcnpx_file[i,4]-1)/mcnpx_file[i,4]
# end i 
#
minimum_keff_index=numpy.argmin(keff_comparison)
content_burnup_file.write('\t'+str.format('%.3e'%mcnpx_file[minimum_keff_index,8])+'\t'+str.format('%.5f'%mcnpx_file[minimum_keff_index,4])+'\n')
#######
# 
# close files
#
content_burnup_file.close()
#
########################################################################
#
# EOF
#
########################################################################
