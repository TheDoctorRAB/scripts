#######
# @TheDoctorRAB
#######
#
# prepare material card for an mcnp input file
# assumes a file with radionuclide name in column 1
# remaining columns are mass fraction*1E6 based on origen output
# for use with _fixed.out file
# remember file has 'totals' in last row
#
#######
#
# computes weight fraction in mcnp style
#
#######
#
# imports
import os
import numpy
#import pyne
from sys import argv
#from pyne import nucname - installation problems with pyne
script,datafile,timefile=argv
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
# weight fraction cutoff
# after calculating actual weight fraction
#
cutoff=1E-06
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
weight_fraction=numpy.zeros((rows-2,columns))
#
for i in range (0,rows-2):
  for j in range (0,columns):
     weight_fraction[i,j]=raw_data[i,j]*(-1)*1E-06 #negative is added here because MCNP uses (-) for weight fraction
#
#######
#
# change to ZAID
#
#for i in range (0,rows):
#  labels[i]=str(pyne.nucname.zzzaaa(labels[i]))+'.70c'
#
#######
#
# write weight fractions above prescribed cutoff to new file
#
for j in range(0,columns):
  material_card=open(os.path.splitext(datafile)[0]+'_material.card_'+time[j]+'.out','w+') #open material card
  for i in range(0,(rows-2)):
   if(abs(weight_fraction[i,j])>cutoff):
    material_card.write('        '+str.format('%s'%labels[i])+'     '+str.format('%.6e'%weight_fraction[i,j])+'\n')
#
  material_card.close()
#
#######
# EOF
#######
