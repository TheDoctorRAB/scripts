#######
# @TheDoctorRAB
#######
#
# edits a given set of lines in the input file
# number of spaces is important because MCNP is FORTRAN
# probably not the most elegant
#
#######
#
# imports
#
from sys import argv
script,inputfile=argv
#
#######
#
# set the lines to be edited
#
###
#
# header
#
header_new_lines='''c      7 - cladding gap
c      8 - boron frits-baryte concrete'''
#
header_old_lines='c      7 - cladding gap'
#
###
#
# surface
#
surface_new_lines='''c      window for lattice is the fuel block given in 78 - 81
c      ---
c      end
c      ---
c
c      ---
c      container
c      ---
100    c/z 17.159 17.159 84.572                       $container - radius + container thickness and changes with plate thickness
101    pz  460.0                                      $cap - surface 26 + container thickness
102    pz -50.0                                       $plug - surface 22 - container thickness'''
#
surface_old_lines='c      window for lattice is the fuel block given in 78 - 81'
#
###
#
# cell
#
cell_new_lines='''c      container
c      ---
400    8 -3.10 (-10:14:-16:20) -100  22 -26   imp:n,p=1 VOL=2.23713e+06   $container - change volume with plate thickness
401    8 -3.10                 -100  26 -101  imp:n,p=1                   $container cap
402    8 -3.10                 -100 -22  102  imp:n,p=1                   $container plug
c      ---
c      end
c      ---
c
c      ---
c      end cask'''
#
cell_old_lines='c      end cask'
#
###
#
# universe
#
universe_new_lines='999    0  100:101:-102  imp:n,p=0'
#
universe_old_lines='999    0        -10:14:-16:20:-22:26   imp:n,p=0'
#
###
#
# tally
#
tally_new_lines='''c      FC2    west plate
c      F2:N   10
c      C2     0 1 T
c      ---'''
tally_new_lines2='c      FC12   east plate'
tally_new_lines3='c      F12:N  14'
tally_new_lines4='''c      C12    0 1 T
c      ---'''
tally_new_lines5='''c      FC22   south plate
c      F22:N  16
c      C22    0 1 T
c      ---
c      FC32   north plate
c      F32:N  20
c      C32    0 1 T
c      ---
c      FC42   cap
c      F42:N  26
c      C42    0 1 T
c      ---
c      FC52   plug
c      F52:N  22
c      C52    0 1 T
c      ---
FC62   container surface
F62:N  100
C62    0 1 T
c      ---
FC72   container top
F72:N  101
C72    0 1 T
c      ---
FC82   container bottom
F82:N  102
C82    0 1 T'''
#
tally_old_lines='''FC2    west plate
F2:N   10
C2     0 1 T
c'''
#
# there is a weird white space on F12:N that I cannot seem to get around
#
tally_old_lines2='FC12   east plate'
tally_old_lines3='F12:N  14'
tally_old_lines4='''C12    0 1 T
c'''
#
tally_old_lines5='''FC22   south plate
F22:N  16
C22    0 1 T
c
FC32   north plate
F32:N  20
C32    0 1 T
c      ---
FC42   cap
F42:N  26
C42    0 1 T
c      ---
FC52   plug
F52:N  22
C52    0 1 T'''
#
###
#
# material
#
material_new_lines='''c      cladding gap
c      ---
M7     2004.70c    -1.0                $He
c      ---
c
c      ---
c      boron frits-baryte concrete
c      ---
M8     1001.66c  -0.005600
       5011.66c  -0.010400
       8016.66c  -0.338000
       9019.66c  -0.002300
       11023.66c -0.012100
       12000.66c -0.002300
       13027.66c -0.006400
       14000.60c -0.033100
       16000.66c -0.091500
       19000.66c -0.001000
       20000.66c -0.062600
       25055.66c -0.000200
       26000.50c -0.021900
       30000.42c -0.006600
       56138.66c -0.401300'''
#
material_old_lines='''c      cladding gap
c      ---
M7     2004.70c    -1.0                $He'''
#
###
#
# NPS
#
nps_new_lines='NPS    3000000'
#
nps_old_lines='NPS    2000000'
#
#######
#
# open the mcnp deck and read
# this is ok because the input files for mcnp are small for memory
#
tempfile=open(inputfile,'r').read()
#
#######
#
# replace
#
tempfile=tempfile.replace(header_old_lines,header_new_lines)
#
tempfile=tempfile.replace(surface_old_lines,surface_new_lines)
#
tempfile=tempfile.replace(cell_old_lines,cell_new_lines)
#
tempfile=tempfile.replace(universe_old_lines,universe_new_lines)
#
tempfile=tempfile.replace(tally_old_lines,tally_new_lines)
tempfile=tempfile.replace(tally_old_lines2,tally_new_lines2)
tempfile=tempfile.replace(tally_old_lines3,tally_new_lines3)
tempfile=tempfile.replace(tally_old_lines4,tally_new_lines4)
tempfile=tempfile.replace(tally_old_lines5,tally_new_lines5)
#
tempfile=tempfile.replace(material_old_lines,material_new_lines)
#
tempfile=tempfile.replace(nps_old_lines,nps_new_lines)
#######
#
# write the file
#
open(inputfile,'w').write(tempfile)
#
########################################################################
#
# EOF
#
########################################################################
