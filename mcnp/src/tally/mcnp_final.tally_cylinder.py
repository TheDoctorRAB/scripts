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
import numpy
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
# tally 62
#
###
#
# get line number
# remember python starts a line 0, whereas vim starts at line 1
#
tallyline62_10wt=totlines_10wt-13
tallyline62_30wt=totlines_30wt-13
tallyline62_50wt=totlines_50wt-13
tallyline62_70wt=totlines_70wt-13
tallyline62_90wt=totlines_90wt-13
#
###
#
# get tally data
#
tally62_10wt=mcnpread_10wt[tallyline32_10wt-1][13:30]
tally62_30wt=mcnpread_30wt[tallyline32_30wt-1][13:30]
tally62_50wt=mcnpread_50wt[tallyline32_50wt-1][13:30]
tally62_70wt=mcnpread_70wt[tallyline32_70wt-1][13:30]
tally62_90wt=mcnpread_90wt[tallyline32_90wt-1][13:30]
#
#######
#
# tally 72
#
###
#
# get line number
# remember python starts a line 0, whereas vim starts at line 1
#
tallyline72_10wt=totlines_10wt-13
tallyline72_30wt=totlines_30wt-13
tallyline72_50wt=totlines_50wt-13
tallyline72_70wt=totlines_70wt-13
tallyline72_90wt=totlines_90wt-13
#
###
#
# get tally data
#
tally72_10wt=mcnpread_10wt[tallyline42_10wt-1][53:70]
tally72_30wt=mcnpread_30wt[tallyline42_30wt-1][53:70]
tally72_50wt=mcnpread_50wt[tallyline42_50wt-1][53:70]
tally72_70wt=mcnpread_70wt[tallyline42_70wt-1][53:70]
tally72_90wt=mcnpread_90wt[tallyline42_90wt-1][53:70]
#
#######
#
# tally 82
#
###
#
# get line number
# remember python starts a line 0, whereas vim starts at line 1
#
tallyline82_10wt=totlines_10wt-13
tallyline82_30wt=totlines_30wt-13
tallyline82_50wt=totlines_50wt-13
tallyline82_70wt=totlines_70wt-13
tallyline82_90wt=totlines_90wt-13
#
###
#
# get tally data
#
tally82_10wt=mcnpread_10wt[tallyline52_10wt-1][93:110]
tally82_30wt=mcnpread_30wt[tallyline52_30wt-1][93:110]
tally82_50wt=mcnpread_50wt[tallyline52_50wt-1][93:110]
tally82_70wt=mcnpread_70wt[tallyline52_70wt-1][93:110]
tally82_90wt=mcnpread_90wt[tallyline52_90wt-1][93:110]
#
#######
#
#
# open files for writing
#
mcnpwrite_tally62=open('single.assembly_7815_container.surface.out','a')
mcnpwrite_tally72=open('single.assembly_7815_container.top.out','a')
mcnpwrite_tally82=open('single.assembly_7815_container.bottom.out','a')
#
#######
#
# write files
#
mcnpwrite_tally62.write(tally62_10wt+' '+tally62_30wt+' '+tally62_50wt+' '+tally62_70wt+' '+tally62_90wt+'\n')
mcnpwrite_tally72.write(tally72_10wt+' '+tally72_30wt+' '+tally72_50wt+' '+tally72_70wt+' '+tally72_90wt+'\n')
mcnpwrite_tally82.write(tally82_10wt+' '+tally82_30wt+' '+tally82_50wt+' '+tally82_70wt+' '+tally82_90wt+'\n')
#
#######
#
# close files
#
mcnpwrite_tally62.close()
mcnpwrite_tally72.close()
mcnpwrite_tally82.close()
#
#######
# EOF
#######
