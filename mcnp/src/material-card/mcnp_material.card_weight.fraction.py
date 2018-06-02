#######
# @TheDoctorRAB
#######
#
# prepare material card for an mcnp input file
# assumes a file with radionuclide name in column 1
# remaining columns are mass or mass fraction
#
#######
#
# currently built for origen output
# computes weight fraction
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
labels=numpy.genfromtxt(datafile,dtype=str,usecols=[0])
raw_data=numpy.genfromtxt(datafile,dtype=float)[:,1:]
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
# prepare output file
#
material_card_file=os.path.splitext(datafile)[0]+'_material.card.out'
#
######
#
# compute weight fraction
#
weight_fraction=numpy.zeros((rows,columns))
#
for i in range (0,rows):
  for j in range (0,columns):
     weight_fraction[i,j]=raw_data[i,j]*(-1)*1E-06 #negative is added here because MCNP uses (-) for weight fraction
#
#######
#
# combine
#
material_card=numpy.c_[labels,weight_fraction] #saves as strings
#
######
#
# save file
#
numpy.savetxt(material_card_file,material_card,fmt='%s',delimiter='\t')
#
#######
# EOF
#######
