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
print 'make sure you have the right neutron emission rate selected!'
#
neutron_emission_rate=1.1410E+08   #L-3030
# neutron_emission_rate=8.8398E+08    #H-5060
#
print neutron_emission_rate
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
# prepare thickness column
#
thickness=numpy.array([1.50,3.00,6.00,12.0,18.0,30.0,60.0])
#
#######
#
# make new data array
#
newdata=numpy.zeros((rows,columns+1))
#
#######
#
# write new data
#
for j in range (0,(columns+1)):
  for i in range (0,rows):
    if (j==0):
      newdata[i,j]=thickness[i]
    else:
      newdata[i,j]=raw_data[i,j-1]
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
numpy.savetxt(dose_rate,newdata,fmt='%.4e')
#
#######
# EOF
#######
