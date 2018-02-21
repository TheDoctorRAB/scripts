#######
# R.A.Borrelli
# @TheDoctorRAB
#######
#
# Find the maximum/minimum value in a column of data for a multi column file where the first column is the label
#
#######
#
# For these output files, the first column is the radionuclide label (string)
# The remaining columns are data (float)
# Pandas only recogized some of the data columns as float and the rest as str
# So pandas would not be able to do any statistics on the columns
# It was because small values did not contain the 'E' for scientific notation and was read as NaN; i.e., 1.0133-114
# Still can't get cutoffs right in SCALE
#
#######
#
# The workaround is then to use numpy.genfromtxt
# 1. Load the first column as str
# 2. Load the rest as float
# 3. Find the NaNs and locations
# 4. Replace NaNs with 0
#
####### imports
import os
import numpy
from sys import argv
script,datafile,timefile=argv
#######
#
####### read data files
labels=numpy.genfromtxt(datafile,dtype=str,usecols=[0])
raw_data=numpy.genfromtxt(datafile,dtype=float)[:,1:]
time_data=numpy.genfromtxt(timefile,dtype=float)
#######
#
####### get number of rows and columns
rows=labels.shape[0]
columns=raw_data.shape[1]
#print rows,columns
#print 'Remember column = number of data columns. +1 for the column of labels'
#######
#
####### prepare output file
output_file=os.path.splitext(datafile)[0]+'_sorted.out'
#######
#
###### initialize matrix
selected_values=numpy.zeros(columns)
######
#
###### open file for writing
sorted_file=open(output_file,'w+')
######
#
###### find and replace NaN with 0
for i in range (0,rows):
  for j in range (0,columns):
    if (numpy.isnan(raw_data[i,j])) == True:
#      print 'NaN at: ',i,j
#      print 'replacing'
      raw_data[i,j]=0
#
###### find maximum/minimum of each column
for j in range (0,columns):
  selected_values[j]=numpy.nanmax(raw_data[:,j])
######
#
####### find the row location for the maximum/minimum value
for j in range (0,columns):
  for i in range(0,rows):
    if raw_data[i,j] == selected_values[j]:
#      print i,j,labels[i],selected_values[j],time_data[j]
# write to file
      sorted_file.write(str.format('%.2f'%time_data[j])+'\t'+str.format('%s'%labels[i])+'\t'+str.format('%.4e'%selected_values[j])+'\n')
#
###### close file
sorted_file.close()
#######
