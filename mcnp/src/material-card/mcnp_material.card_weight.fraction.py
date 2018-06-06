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
import pyne
from sys import argv
from pyne import nucname
script,timefile,datafile=argv
#
#######
#
# read data files
#
labels=numpy.genfromtxt(datafile,dtype=object,usecols=[0])
raw_data=numpy.genfromtxt(datafile,dtype=float)[:,1:]
time=numpy.genfromtxt(timefile,dtype=str) #read in as string because time step is used as output file label
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
# change to ZAID
#
for i in range (0,rows):
  labels[i]=str(pyne.nucname.zzzaaa(labels[i]))+'.70c'
#
# write weight fractions above prescribed cutoff to new file
#
cutoff=1E-06
#
for j in range(0,columns):
###
#
# open material card
#
  material_card=open(os.path.splitext(datafile)[0]+'_material.card_'+time[j]+'.out','w+')
#
###
#
  for i in range(0,rows):
   if(abs(weight_fraction[i,j])>cutoff):
    material_card.write('        '+str.format('%s'%labels[i])+'     '+str.format('%.6e'%weight_fraction[i,j])+'\n')
#
  material_card.close()
#
#######
# EOF
#######
