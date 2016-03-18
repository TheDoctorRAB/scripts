########################################################################
# R.A.Borrelli
# @TheDoctorRAB
# rev.27.January.2016
########################################################################
#
# This searches for radionuclide data on the BURN card and just writes the line to a separate file.
#
########################################################################
#
#
#
####### 
#
# imports
#
import os
from sys import argv
script,mcnpx_output,zaid=argv
#
########################################################################
#
#
#
####### 
#
# open mcnp output file
#
mcnpx_file=open(mcnpx_output,'r').readlines()
#
#######
#
# prepare output files 
#
mcnpx_output_temp=os.path.splitext(mcnpx_output)[0] #separates filename.suffix, keeps filename
mcnpx_output_file=os.path.splitext(mcnpx_output_temp)[0]+'_radionuclide.content.out' #same thing, these particular files were filename.suffix1.suffix2
#
#######
#
# open the tally file for writing
#
os.chdir('../../../radionuclide.content/12.54mm_pitch/dt50') #verify directory location and radionuclide
print 'Current directory path is: ',os.getcwd(),'for' ,zaid
raw_input('Go/NoGo')
dir_check=os.path.isdir('../../../radionuclide.content/12.54mm_pitch/dt50/'+zaid) #check if directory exists
#
if(dir_check==False):
    os.mkdir(zaid)
# end if
#
os.chdir(zaid)
radionuclide_content_file=open(mcnpx_output_file,'w+')
#
#######
#
# initialize the counters
#
print_table_210=0
print_table_220=0
line_number=0
#
#######
#
# search the file for the individual tallies
# line will write the current line
# use ZAID to find the radionuclide of interest entered on the command line
# there will be multiple lines based on number of time steps selected on BURN card in input deck
#
for line in mcnpx_file: #finds the line numbers containing BURN print table 210
    print_table_210=print_table_210+1
    if 'print table 210' in line:
	break    
# end if
# end line
#
for line in mcnpx_file: #finds the line numbers containing BURN print table 220
    print_table_220=print_table_220+1
    if 'print table 220' in line:
	break    
# end if
# end line
#
for line in mcnpx_file: #only writes occurance of zaid from print table 210
    line_number=line_number+1
    if line_number>print_table_210 and line_number<print_table_220 and zaid in line: 
	radionuclide_content_file.write('\t'+line)
# end if
# end line
#
#######
#
# close file
#
radionuclide_content_file.close()
#
########################################################################
#
# EOF
#
########################################################################
