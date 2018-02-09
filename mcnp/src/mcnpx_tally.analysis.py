########################################################################
# R.A.Borrelli
# @TheDoctorRAB
# rev.14.May.2014
########################################################################
# This writes the tallies to a separate file.
# The tallies have to be set in the script here a priori, obviously.
# Sometimes a single deck contains a lot of them, so this should help.
# This also reorders the tallies by 'class', like F2s, then F4s, etc.  
########################################################################
#
#
####### imports
import os
from sys import argv
script,mcnpx_output=argv
#######
#
####### open mcnp output file
mcnpx_file=open(mcnpx_output,'r').readlines()
#######
#
####### prepare output files 
mcnpx_output_file=os.path.splitext(mcnpx_output)[0]+'_tally.analysis.out'
check_output_file=os.path.splitext(mcnpx_output)[0]+'_tally.check.out'
#######
#
####### open the tally file for writing
tally_file=open(mcnpx_output_file,'w+')
check_file=open(check_output_file,'w+')
#######
#
####### initialize the counter
i=0
#######
#
####### search the file for the individual tallies
# line will write the current line
# mcnpx_file[i] writes the next line
# F2s
#
for line in mcnpx_file:
  i=i+1
  if '1tally   2' in line and 'nps' in line:
    tally_file.write(line)
#
  if 'surface  10' in line and 'cosine bin:   0.00000E+00 to  1.00000E+00' in mcnpx_file[i]:
    tally_file.write(line)
    tally_file.write(mcnpx_file[i])
    tally_file.write(mcnpx_file[i+1])
#
  if 'surface  11' in line and 'cosine bin:  -1.          to  0.00000E+00' in mcnpx_file[i]:
    tally_file.write(line)
    tally_file.write(mcnpx_file[i])
    tally_file.write(mcnpx_file[i+1])
#
  if 'surface  12' in line and 'cosine bin:   0.00000E+00 to  1.00000E+00' in mcnpx_file[i]:
    tally_file.write(line)
    tally_file.write(mcnpx_file[i])
    tally_file.write(mcnpx_file[i+1])
#
  if 'surface union total' in line and 'cosine bin:  total' in mcnpx_file[i] and 'tally   2' in mcnpx_file[i+2]:
    tally_file.write(line)
    tally_file.write(mcnpx_file[i])
    tally_file.write(mcnpx_file[i+1])
    tally_file.write('\n')        
#
  if '1tally  12' in line and 'nps' in line:
    tally_file.write(line)
#
  if 'surface  13' in line and 'cosine bin:   0.00000E+00 to  1.00000E+00' in mcnpx_file[i]:
    tally_file.write(line)
    tally_file.write(mcnpx_file[i])
    tally_file.write(mcnpx_file[i+1])
#
  if 'surface  14' in line and 'cosine bin:  -1.          to  0.00000E+00' in mcnpx_file[i]:
    tally_file.write(line)
    tally_file.write(mcnpx_file[i])
    tally_file.write(mcnpx_file[i+1])
#
  if 'surface union total' in line and 'cosine bin:  total' in mcnpx_file[i] and 'tally  12' in mcnpx_file[i+2]:
    tally_file.write(line)
    tally_file.write(mcnpx_file[i])
    tally_file.write(mcnpx_file[i+1])
    tally_file.write('\n')
#
  if '1tally  22' in line and 'nps' in line:
    tally_file.write(line)
#
  if 'surface  18' in line and 'cosine bin:   0.00000E+00 to  1.00000E+00' in mcnpx_file[i]:
    tally_file.write(line)
    tally_file.write(mcnpx_file[i])
    tally_file.write(mcnpx_file[i+1])
#
  if 'surface  19' in line and 'cosine bin:   0.00000E+00 to  1.00000E+00' in mcnpx_file[i]:
    tally_file.write(line)
    tally_file.write(mcnpx_file[i])
    tally_file.write(mcnpx_file[i+1])
#
  if 'surface  20' in line and 'cosine bin:  -1.          to  0.00000E+00' in mcnpx_file[i]:
    tally_file.write(line)
    tally_file.write(mcnpx_file[i])
    tally_file.write(mcnpx_file[i+1])
#
  if 'surface union total' in line and 'cosine bin:  total' in mcnpx_file[i] and 'tally  22' in mcnpx_file[i+2]:
    tally_file.write(line)
    tally_file.write(mcnpx_file[i])
    tally_file.write(mcnpx_file[i+1])
    tally_file.write('\n')        

  if '1tally  32' in line and 'nps' in line:
    tally_file.write(line)
#
  if 'surface  61' in line and 'cosine bin:  -1.          to  0.00000E+00' in mcnpx_file[i+1]:
    tally_file.write(line)
    tally_file.write(mcnpx_file[i+1])
    tally_file.write(mcnpx_file[i+2])
#
  if 'surface  61' in line and 'cosine bin:  total' in mcnpx_file[i+1]:
    tally_file.write(line)
    tally_file.write(mcnpx_file[i+1])
    tally_file.write(mcnpx_file[i+2])
    tally_file.write('\n')
#
  if '1tally  42' in line and 'nps' in line:
    tally_file.write(line)
#
  if 'surface  62' in line and 'cosine bin:   0.00000E+00 to  1.00000E+00' in mcnpx_file[i+1]:
    tally_file.write(line)
    tally_file.write(mcnpx_file[i+1])
    tally_file.write(mcnpx_file[i+2])
#
  if 'surface  62' in line and 'cosine bin:  total' in mcnpx_file[i+1]:
    tally_file.write(line)
    tally_file.write(mcnpx_file[i+1])
    tally_file.write(mcnpx_file[i+2])
    tally_file.write('\n')
# end ifs
# end line
####### reset the counter
i=0
tally_file.write('#######\n\n')
#######
# F4s
#
for line in mcnpx_file:
  i=i+1
  if '1tally   4' in line and 'nps' in line:
    tally_file.write(line)
#
  if 'cell  100' in line:
    tally_file.write(line)
    tally_file.write(mcnpx_file[i])
    tally_file.write('\n')
#
  if '1tally  14' in line and 'nps' in line:
    tally_file.write(line)
#
  if 'cell  101' in line:
    tally_file.write(line)
    tally_file.write(mcnpx_file[i])
    tally_file.write('\n')
#
  if '1tally  24' in line and 'nps' in line:
    tally_file.write(line)
#
  if 'cell  102' in line:
    tally_file.write(line)
    tally_file.write(mcnpx_file[i])
    tally_file.write('\n')
#
  if '1tally  34' in line and 'nps' in line:
    tally_file.write(line)
#
  if 'cell  104' in line:
    tally_file.write(line)
    tally_file.write(mcnpx_file[i])
    tally_file.write('\n')
#    
  if '1tally  44' in line and 'nps' in line:
    tally_file.write(line)
#
  if 'cell  110' in line:
    tally_file.write(line)
    tally_file.write(mcnpx_file[i])
    tally_file.write('\n')
#
  if '1tally  54' in line and 'nps' in line:
    tally_file.write(line)
#
  if 'cell  111' in line:
    tally_file.write(line)
    tally_file.write(mcnpx_file[i])
    tally_file.write('\n')
#
  if '1tally  64' in line and 'nps' in line:
    tally_file.write(line)
#
  if 'cell  112' in line:
    tally_file.write(line)
    tally_file.write(mcnpx_file[i])
    tally_file.write('\n')
#        
# endifs  
# end line
#######
#
####### reset the counter
i=0
tally_file.write('#######\n\n')
#######
#
####### record tally checks
# F2s
#
for line in mcnpx_file:
  i=i+1
  if 'results of 10 statistical checks' in line and 'tally   2' in line:
    check_file.write(mcnpx_file[i-3])
    check_file.write(line)
    for x in range(0,9):
      check_file.write(mcnpx_file[i+x])
    check_file.write('\n')  
#
  if 'results of 10 statistical checks' in line and 'tally  12' in line:
    check_file.write(mcnpx_file[i-3])
    check_file.write(line)
    for x in range(0,9):
      check_file.write(mcnpx_file[i+x])
    check_file.write('\n')
#
  if 'results of 10 statistical checks' in line and 'tally  22' in line:
    check_file.write(mcnpx_file[i-3])
    check_file.write(line)
    for x in range(0,9):
      check_file.write(mcnpx_file[i+x])
    check_file.write('\n')
#        
  if 'results of 10 statistical checks' in line and 'tally  32' in line:
    check_file.write(mcnpx_file[i-3])
    check_file.write(line)
    for x in range(0,9):
      check_file.write(mcnpx_file[i+x])
    check_file.write('\n')
#        
  if 'results of 10 statistical checks' in line and 'tally  42' in line:
    check_file.write(mcnpx_file[i-3])
    check_file.write(line)
    for x in range(0,9):
      check_file.write(mcnpx_file[i+x])
    check_file.write('\n\n')
#
# endifs  
# end line
#######
#
####### reset the counter
i=0
#######
#
####### record tally checks
# F4s
#
for line in mcnpx_file:
  i=i+1
  if 'results of 10 statistical checks' in line and 'tally   4' in line:
    check_file.write(mcnpx_file[i-3])
    check_file.write(line)
    for x in range(0,9):
      check_file.write(mcnpx_file[i+x])
    check_file.write('\n')
#
  if 'results of 10 statistical checks' in line and 'tally  14' in line:
    check_file.write(mcnpx_file[i-3])
    check_file.write(line)
    for x in range(0,9):
      check_file.write(mcnpx_file[i+x])
    check_file.write('\n')
#
  if 'results of 10 statistical checks' in line and 'tally  24' in line:
    check_file.write(mcnpx_file[i-3])
    check_file.write(line)
    for x in range(0,9):
      check_file.write(mcnpx_file[i+x])
    check_file.write('\n')
#
  if 'results of 10 statistical checks' in line and 'tally  34' in line:
    check_file.write(mcnpx_file[i-3])
    check_file.write(line)
    for x in range(0,9):
      check_file.write(mcnpx_file[i+x])
    check_file.write('\n')
#        
  if 'results of 10 statistical checks' in line and 'tally  44' in line:
    check_file.write(mcnpx_file[i-3])
    check_file.write(line)
    for x in range(0,9):
      check_file.write(mcnpx_file[i+x])
    check_file.write('\n')
#        
  if 'results of 10 statistical checks' in line and 'tally  54' in line:
    check_file.write(mcnpx_file[i-3])
    check_file.write(line)
    for x in range(0,9):
      check_file.write(mcnpx_file[i+x])
    check_file.write('\n')
#
  if 'results of 10 statistical checks' in line and 'tally  64' in line:
    check_file.write(mcnpx_file[i-3])
    check_file.write(line)
    for x in range(0,9):
      check_file.write(mcnpx_file[i+x])
    check_file.write('\n\n')
#                                
# endifs  
# end line
#######
#
#######
#
####### reset the counter
i=0
#######
#
####### record check summary
for line in mcnpx_file:
  i=i+1
  if 'all bins' in line:
    check_file.write(line)
    for x in range(0,36):
      check_file.write(mcnpx_file[i+x])
    check_file.write('\n\n')    
#
#######
#
####### reset the counter
i=0
#######
#
####### record summary charts
for line in mcnpx_file:
  i=i+1
  if '                       tally    2' in line:
    check_file.write(line)
    for x in range(0,95):
      check_file.write(mcnpx_file[i+x])
    check_file.write('\n\n')    
#
####### close files
tally_file.close()
check_file.close()
#######
#
########################################################################
#      EOF
########################################################################
