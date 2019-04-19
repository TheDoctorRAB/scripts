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
