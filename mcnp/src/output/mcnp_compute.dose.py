#######
# @TheDoctorRAB
#######
#
# compute dose from mcnp tally output
# input a matrix of tally values with odd columns having error
#
#######
#
# imports
import os
import numpy
from sys import argv
script,datafile=argv
#
#######
#
# read data files
#
raw_data=numpy.genfromtxt(datafile,delimiter=' ',dtype=None)
#
#######
#
# get number of rows and columns
#
rows=raw_data.shape[0]
columns=raw_data.shape[1]
#
#######
#
# input neutron emisson rate
#
neutron_emission_rate=1.1410E+08
#
#######
#
# compute dose rate
#
for i in range (0,rows):
  for j in range (0,columns):
    if (j%2==0):
      raw_data[i,j]=raw_data[i,j]*neutron_emission_rate*1E+06 #microsieverts per hour
    else:
      raw_data[i,j]=raw_data[i,j]*raw_data[i,j-1] #error
#
#######
#
# open file to write
#
dose_rate=os.path.splitext(datafile)[0]+'_dose.rate'+'.out'
#
#######
#
# write to file
#
numpy.savetxt(dose_rate,raw_data,fmt='%.4e')
#
#######
# EOF
#######
