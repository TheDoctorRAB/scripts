#######
# @TheDoctorRAB
#######
#
# copy final tallies at the end of the mcnp output file into individual separate files
# originally for the igem project but should be applicable for anything else and generalized
#
#######
#
# imports
import os
# import numpy
from sys import argv
script,mcnpout_10wt,mcnpout_30wt,mcnpout_50wt,mcnpout_70wt,mcnpout_90wt=argv
#
#######
#
# read data files
#
mcnpread_10wt=open(mcnpout_10wt,'r').readlines()
mcnpread_30wt=open(mcnpout_30wt,'r').readlines()
mcnpread_50wt=open(mcnpout_50wt,'r').readlines()
mcnpread_70wt=open(mcnpout_70wt,'r').readlines()
mcnpread_90wt=open(mcnpout_90wt,'r').readlines()
#
#######
#
# get number of lines in each file
# with mcnp each file has a different number of lines
#
totlines_10wt=len(mcnpread_10wt)
totlines_30wt=len(mcnpread_30wt)
totlines_50wt=len(mcnpread_50wt)
totlines_70wt=len(mcnpread_70wt)
totlines_90wt=len(mcnpread_90wt)
#
#######
#
# tally 02
#
###
#
# get line number
# remember python starts a line 0, whereas vim starts at line 1
#
tallyline02_10wt=totlines_10wt-27
tallyline02_30wt=totlines_30wt-27
tallyline02_50wt=totlines_50wt-27
tallyline02_70wt=totlines_70wt-27
tallyline02_90wt=totlines_90wt-27
#
###
#
# get tally data
#
tally02_10wt=mcnpread_10wt[tallyline02_10wt-1][13:30]
tally02_30wt=mcnpread_30wt[tallyline02_30wt-1][13:30]
tally02_50wt=mcnpread_50wt[tallyline02_50wt-1][13:30]
tally02_70wt=mcnpread_70wt[tallyline02_70wt-1][13:30]
tally02_90wt=mcnpread_90wt[tallyline02_90wt-1][13:30]
#
#######
#
# tally 12
#
###
#
# get line number
# remember python starts a line 0, whereas vim starts at line 1
#
tallyline12_10wt=totlines_10wt-27
tallyline12_30wt=totlines_30wt-27
tallyline12_50wt=totlines_50wt-27
tallyline12_70wt=totlines_70wt-27
tallyline12_90wt=totlines_90wt-27
#
###
#
# get tally data
#
tally12_10wt=mcnpread_10wt[tallyline12_10wt-1][53:70]
tally12_30wt=mcnpread_30wt[tallyline12_30wt-1][53:70]
tally12_50wt=mcnpread_50wt[tallyline12_50wt-1][53:70]
tally12_70wt=mcnpread_70wt[tallyline12_70wt-1][53:70]
tally12_90wt=mcnpread_90wt[tallyline12_90wt-1][53:70]
#
#######
#
# tally 22
#
###
#
# get line number
# remember python starts a line 0, whereas vim starts at line 1
#
tallyline22_10wt=totlines_10wt-27
tallyline22_30wt=totlines_30wt-27
tallyline22_50wt=totlines_50wt-27
tallyline22_70wt=totlines_70wt-27
tallyline22_90wt=totlines_90wt-27
#
###
#
# get tally data
#
tally22_10wt=mcnpread_10wt[tallyline22_10wt-1][93:110]
tally22_30wt=mcnpread_30wt[tallyline22_30wt-1][93:110]
tally22_50wt=mcnpread_50wt[tallyline22_50wt-1][93:110]
tally22_70wt=mcnpread_70wt[tallyline22_70wt-1][93:110]
tally22_90wt=mcnpread_90wt[tallyline22_90wt-1][93:110]
#
#######
#
# tally 32
#
###
#
# get line number
# remember python starts a line 0, whereas vim starts at line 1
#
tallyline32_10wt=totlines_10wt-13
tallyline32_30wt=totlines_30wt-13
tallyline32_50wt=totlines_50wt-13
tallyline32_70wt=totlines_70wt-13
tallyline32_90wt=totlines_90wt-13
#
###
#
# get tally data
#
tally32_10wt=mcnpread_10wt[tallyline32_10wt-1][13:30]
tally32_30wt=mcnpread_30wt[tallyline32_30wt-1][13:30]
tally32_50wt=mcnpread_50wt[tallyline32_50wt-1][13:30]
tally32_70wt=mcnpread_70wt[tallyline32_70wt-1][13:30]
tally32_90wt=mcnpread_90wt[tallyline32_90wt-1][13:30]
#
#######
#
# tally 42
#
###
#
# get line number
# remember python starts a line 0, whereas vim starts at line 1
#
tallyline42_10wt=totlines_10wt-13
tallyline42_30wt=totlines_30wt-13
tallyline42_50wt=totlines_50wt-13
tallyline42_70wt=totlines_70wt-13
tallyline42_90wt=totlines_90wt-13
#
###
#
# get tally data
#
tally42_10wt=mcnpread_10wt[tallyline42_10wt-1][53:70]
tally42_30wt=mcnpread_30wt[tallyline42_30wt-1][53:70]
tally42_50wt=mcnpread_50wt[tallyline42_50wt-1][53:70]
tally42_70wt=mcnpread_70wt[tallyline42_70wt-1][53:70]
tally42_90wt=mcnpread_90wt[tallyline42_90wt-1][53:70]
#
#######
#
# tally 52
#
###
#
# get line number
# remember python starts a line 0, whereas vim starts at line 1
#
tallyline52_10wt=totlines_10wt-13
tallyline52_30wt=totlines_30wt-13
tallyline52_50wt=totlines_50wt-13
tallyline52_70wt=totlines_70wt-13
tallyline52_90wt=totlines_90wt-13
#
###
#
# get tally data
#
tally52_10wt=mcnpread_10wt[tallyline52_10wt-1][93:110]
tally52_30wt=mcnpread_30wt[tallyline52_30wt-1][93:110]
tally52_50wt=mcnpread_50wt[tallyline52_50wt-1][93:110]
tally52_70wt=mcnpread_70wt[tallyline52_70wt-1][93:110]
tally52_90wt=mcnpread_90wt[tallyline52_90wt-1][93:110]
#
#######
#
#
# open files for writing
#
mcnpwrite_tally02=open('single.assembly_7815_west.plate.out','a')
mcnpwrite_tally12=open('single.assembly_7815_east.plate.out','a')
mcnpwrite_tally22=open('single.assembly_7815_south.plate.out','a')
mcnpwrite_tally32=open('single.assembly_7815_north.plate.out','a')
mcnpwrite_tally42=open('single.assembly_7815_cap.out','a')
mcnpwrite_tally52=open('single.assembly_7815_plug.out','a')
#
#######
#
# write files
#
mcnpwrite_tally02.write(tally02_10wt+' '+tally02_30wt+' '+tally02_50wt+' '+tally02_70wt+' '+tally02_90wt+'\n')
mcnpwrite_tally12.write(tally12_10wt+' '+tally12_30wt+' '+tally12_50wt+' '+tally12_70wt+' '+tally12_90wt+'\n')
mcnpwrite_tally22.write(tally22_10wt+' '+tally22_30wt+' '+tally22_50wt+' '+tally22_70wt+' '+tally22_90wt+'\n')
mcnpwrite_tally32.write(tally32_10wt+' '+tally32_30wt+' '+tally32_50wt+' '+tally32_70wt+' '+tally32_90wt+'\n')
mcnpwrite_tally42.write(tally42_10wt+' '+tally42_30wt+' '+tally42_50wt+' '+tally42_70wt+' '+tally42_90wt+'\n')
mcnpwrite_tally52.write(tally52_10wt+' '+tally52_30wt+' '+tally52_50wt+' '+tally52_70wt+' '+tally52_90wt+'\n')
#
#######
#
# close files
#
mcnpwrite_tally02.close()
mcnpwrite_tally12.close()
mcnpwrite_tally22.close()
mcnpwrite_tally32.close()
mcnpwrite_tally42.close()
mcnpwrite_tally52.close()
#
#######
# EOF
#######
