#######
# @TheDoctorRAB
#######
#
# delete lines in the scale extracted files
# lines need to be deleted prior to using the file as a data matrix
#
# should be applicable to any file where lines need to be deleted
# only if lines are actually known
#
# python starts at line 0, whereas vim starts at line 1
#
#######
#
# imports
#
import os
import numpy
from sys import argv
script,datafile0,datafile1,datafile2,datafile3,datafile4,datafile5,datafile6,datafile7=argv #add as many as needed
#
#######
#
# open data file
#
data_file0=open(datafile0,'r').readlines()
data_file1=open(datafile1,'r').readlines()
data_file2=open(datafile2,'r').readlines()
data_file3=open(datafile3,'r').readlines()
data_file4=open(datafile4,'r').readlines()
data_file5=open(datafile5,'r').readlines()
data_file6=open(datafile6,'r').readlines()
data_file7=open(datafile7,'r').readlines()
#
#######
#
# get number of lines in each file
#
total_lines0=len(data_file0)
total_lines1=len(data_file1)
total_lines2=len(data_file2)
total_lines3=len(data_file3)
total_lines4=len(data_file4)
total_lines5=len(data_file5)
total_lines6=len(data_file6)
total_lines7=len(data_file7)
#
#######
#
# open new output file for undeleted lines
# the trick is to write to a new file containing the lines that are not to be deleted
#
output_file0=os.path.splitext(datafile0)[0]+'_fixed.out'
output_file1=os.path.splitext(datafile1)[0]+'_fixed.out'
output_file2=os.path.splitext(datafile2)[0]+'_fixed.out'
output_file3=os.path.splitext(datafile3)[0]+'_fixed.out'
output_file4=os.path.splitext(datafile4)[0]+'_fixed.out'
output_file5=os.path.splitext(datafile5)[0]+'_fixed.out'
output_file6=os.path.splitext(datafile6)[0]+'_fixed.out'
output_file7=os.path.splitext(datafile7)[0]+'_fixed.out'
#
#######
#
# open output files for writing
#
outputfile0=open(output_file0,'w+')
outputfile1=open(output_file1,'w+')
outputfile2=open(output_file2,'w+')
outputfile3=open(output_file3,'w+')
outputfile4=open(output_file4,'w+')
outputfile5=open(output_file5,'w+')
outputfile6=open(output_file6,'w+')
outputfile7=open(output_file7,'w+')
#
#######
#
# delete lines
#
for position,line in enumerate(data_file0):
    if (position != 0) and (position != 1) and (position != 2) and (position != 3) and (position !=4) and (position != (total_lines0-2)):
        outputfile0.write(line)
###
#
for position,line in enumerate(data_file1):
    if (position != 0) and (position != 1) and (position != 2) and (position != 3) and (position !=4) and (position != (total_lines1-2)):
        outputfile1.write(line)
###
#
for position,line in enumerate(data_file2):
    if (position != 0) and (position != 1) and (position != 2) and (position != 3) and (position !=4) and (position != (total_lines2-2)):
        outputfile2.write(line)
###
#
for position,line in enumerate(data_file3):
    if (position != 0) and (position != 1) and (position != 2) and (position != 3) and (position !=4) and (position != (total_lines3-2)):
        outputfile3.write(line)
###
#
for position,line in enumerate(data_file4):
    if (position != 0) and (position != 1) and (position != 2) and (position != 3) and (position !=4) and (position != (total_lines4-2)):
        outputfile4.write(line)
###
#
for position,line in enumerate(data_file5):
    if (position != 0) and (position != 1) and (position != 2) and (position != 3) and (position !=4) and (position != (total_lines5-2)):
        outputfile5.write(line)
###
#
for position,line in enumerate(data_file6):
    if (position != 0) and (position != 1) and (position != 2) and (position != 3) and (position !=4) and (position != (total_lines6-2)):
        outputfile6.write(line)
###
#
for position,line in enumerate(data_file7):
    if (position != 0) and (position != 1) and (position != 2) and (position != 3) and (position !=4) and (position != (total_lines7-2)):
        outputfile7.write(line)
#
#######
#
# close file
#
outputfile0.close()
outputfile1.close()
outputfile2.close()
outputfile3.close()
outputfile4.close()
outputfile5.close()
outputfile6.close()
outputfile7.close()
#
#######
# EOF
#######
