#######
# @TheDoctorRAB
#######
#
# prepare material card for an mcnp input file
# assumes a file with radionuclide name in column 1
# remaining columns are mass fraction
#
#######
#
# currently built for origen output
# creates two column files as (radionuclide, weight fraction)
#
#######
#
# imports
import os
import numpy
from sys import argv
script,timefile,datafile=argv
#
#######
#
# read data files
#
labels=numpy.genfromtxt(datafile,dtype=str,usecols=[0])
raw_data=numpy.genfromtxt(datafile,dtype=float)[:,1:]
time=numpy.genfromtxt(timefile,dtype=float)
#
#######
#
# get number of rows and columns
#
rows=labels.shape[0]
columns=raw_data.shape[1]
#
#######
#
# make integers for time steps
# used for file labels
#
for i in range(0,columns):
  time[i]=int(time[i])
#
#######
#
# prepare output file
#
#material_card_file=os.path.splitext(datafile)[0]+'_material.card.out'
#
######
#
# compute weight fraction
#
#weight_fraction=numpy.zeros((rows,columns))
#
#for i in range (0,rows):
#  for j in range (0,columns):
#     weight_fraction[i,j]=raw_data[i,j]*1E-06
#
#######
#
# combine
#
#material_card=numpy.c_[labels,weight_fraction] #saves as strings
#
######
#
# save file
#
#numpy.savetxt(material_card_file,material_card,fmt='%s',delimiter='\t')
#
#######
# EOF
#######
