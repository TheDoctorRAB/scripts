########################################################################
# R.A.Borrelli
# @TheDoctorRAB
# rev.27.December.2015
########################################################################
# 
# Interpolates radionuclide mass at critical for selected radionuclide
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
script,mcnpx_output,zaid=argv
#
########################################################################
#
#
#
#######
#
# open files
#
mcnpx_file=numpy.loadtxt(mcnpx_output,dtype=float) #make sure to add correct dirpath on command line
interpolated_file=open(zaid+'.mass_interpolated.out','a') 
#
#######
#
# read number of lines in the input file 
#
i=0
for line in mcnpx_file:
    i=i+1
# end i
#
#######
#
# search the file
#
for j in range(0,i-1):
    if (mcnpx_file[j,1]>1) and (mcnpx_file[j+1,1]<1):
	interpolated_mass=(mcnpx_file[j+1,3])+((1.00-mcnpx_file[j+1,1])*(mcnpx_file[j,3]-mcnpx_file[j+1,3]))/(mcnpx_file[j,1]-mcnpx_file[j+1,1])
        interpolated_file.write('\t'+str.format('%.3e'%interpolated_mass)+'\n')
# end j 
#
#######
# 
# close files
#
interpolated_file.close()
#
########################################################################
#
# EOF
#
########################################################################
