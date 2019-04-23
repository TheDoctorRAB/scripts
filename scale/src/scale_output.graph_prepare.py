#######
# @TheDoctorRAB
#######
#
# prepare ORIGEN data for graphing
# data files from the extract scripts have the time over the rows
# this script takes the data in the row and puts it in a column for use with the plot script
#
#######
#
# data file first column is the radionuclide label (string)
# remaining columns are data (float)
# use _fixed.out as datafile
#
#######
#
# The workaround is then to use numpy.genfromtxt
# 1. Load the first column as str
# 2. Load the rest as float
#
#######
#
# imports
#
import os
import numpy
from sys import argv
script,datafile,timefile=argv
#
#######
#
# read data files
#
labels=numpy.genfromtxt(datafile,dtype=str,usecols=[0])
raw_data=numpy.genfromtxt(datafile,dtype=float)[:,1:]
time_data=numpy.genfromtxt(timefile,dtype=float)
#
#######
#
# get number of rows and columns
#
rows=labels.shape[0]
columns=raw_data.shape[1]
print rows,columns
#
#######
#
# raw data is given per MTU
# compute per assembly
#
mtu_per_assembly=0.475
#
assembly_calculation=numpy.zeros(columns)
#
for j in range(0,columns):
    assembly_calculation[j]=mtu_per_assembly*raw_data[rows-1,j]
#
#######
#
# prepare output file
#
output_file=os.path.splitext(datafile)[0]+'_'+labels[rows-1]+'_to.graph.out'
#
#######
#
# open file for writing
#
graph_preparation=open(output_file,'w+')
#
#######
#
# write to file
#
for j in range(0,columns):
    graph_preparation.write(str.format('%.2f'%time_data[j])+'\t'+str.format('%.4e'%raw_data[rows-1,j])+'\t'+str.format('%.4e'%assembly_calculation[j])+'\n')
#
#######
#
# close file
#
graph_preparation.close()
#
#######
# EOF
#######
