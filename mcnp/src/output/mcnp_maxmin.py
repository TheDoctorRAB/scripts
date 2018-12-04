#######
# @TheDoctorRAB
#######
#
# find maximum and minumum values in an array
# mcnp output would need to be postprocessed first
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
# find maximum and minumum values
#
###
#
max=0
min=1000000
#
###
#
for i in range (0,rows):
  for j in range (0,columns):
    if (j%2!=0):
      if (raw_data[i,j]>max):
        max=raw_data[i,j]
      if (raw_data[i,j]<min):
        min=raw_data[i,j]
#
#######
#
# print values
#
print max,min
#
#######
#
# change directory to write file
#
os.chdir('/home/borrelli/github/igem/neutronics-shielding/low-burnup/L-3030/container/')
#
#######
#
# open file to write
#
maxminfile=open('maxmin.out','a')
#
#######
#
# write to file
#
maxminfile.write(str.format('%.0f'%max)+'\t'+str.format('%.2f'%min)+'\n')
#
#######
#
# close file
#
maxminfile.close()
#
#######
# EOF
#######
