#######
# R.A.Borrelli
# @TheDoctorRAB
#######
# Extract nuclide data from scale output files
#######
#
#
####### imports
import os
from sys import argv
script,scale_output=argv
#######
#
####### open scale output file
scale_file=open(scale_output,'r').readlines()
#######
#
####### prepare output file
scale_output_file=os.path.splitext(scale_output)[0]+'_mass.out'
#######
#
###### open file for writing
nuclide_file=open(scale_output_file,'w+')
######
#
###### initialize flag
extract=False
######
#
###### extract data
for line in scale_file:
    if line.strip() == "=   Nuclide concentrations in grams for case 'decay' (#2/2)                                                             =":
        extract = True
    elif line.strip() == "=========================================================================================================================":
        extract = False
    elif extract:
        nuclide_file.write(line)
#######
#
####### close file
nuclide_file.close()
#######
