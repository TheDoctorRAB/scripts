#######
# @TheDoctorRAB
#######
#
# compute dimensions and surface cards for concrete container
#
#######
#
# imports
#
import os
import numpy
from sys import argv
script,mcnp_output=argv
#
#######
#
# open mcnp output file
#
mcnp_file=open(mcnp_output,'r').readlines()
#
#######
#
# search the file for the dimensions to calculate the container
#
###
#
# surface 10
#
for line in mcnp_file:
  if '10     px' in line:
    surface_10=numpy.float(line[10:18])
    print line,surface_10
#
###
#
# surface 13
#
for line in mcnp_file:
  if '13     px' in line:
    surface_13=numpy.float(line[10:18])
    print line,surface_13
#
###
#
# surface 14
#
for line in mcnp_file:
  if '14     px' in line:
    surface_14=numpy.float(line[10:18])
    print line,surface_14
#
###
#
# surface 22
#
for line in mcnp_file:
  if '22     pz' in line:
    surface_22=numpy.float(line[10:18])
    print line,surface_22
#
###
#
# surface 26
#
for line in mcnp_file:
  if '26     pz' in line:
    surface_26=numpy.float(line[10:18])
    print line,surface_26
#
#######
#
# calculations
# units in cm
#
container_thickness=20
plate_thickness=surface_13-surface_10
radius=0.5*(surface_14-surface_10)*numpy.sqrt(2)
volume=(surface_26-surface_22)*(numpy.pi*radius*radius-(surface_14-surface_10)*(surface_14-surface_10))
#
print 'plate thickness:',plate_thickness
print 'container thickness:',container_thickness
print 'radius:',radius
print 'volume:',volume
#
#######
#
# prepare new cards for the container
#
surface_card_output=open('igem_surface.card_single.assembly_'+str.format('%.1f'%(container_thickness))+'cm_'+str.format('%.1f'%(plate_thickness))+'cm.out','w+')
#
surface_card_output.write(
 'c      ---'+'\n'
+'c      container'+'\n'
+'c      ---'+'\n'
+'400    8 -3.10 (-10:14:-16:20) -100  22 -26   imp:n,p=1 VOL='+str.format('%.5e'%(volume))+'   $container - change volume with plate thickness'+'\n'
+'401    8 -3.10                 -100  26 -101  imp:n,p=1                   $container cap'+'\n'
+'402    8 -3.10                 -100 -22  102  imp:n,p=1                   $container plug'+'\n'
+'c      ---'+'\n'
+'c      end'+'\n'
+'c      ---'+'\n'
+'c'+'\n'
+'c      ---'+'\n'
+'c      end cask'+'\n'
+'c      ---'+'\n'
+'c'+'\n'
+'c      ---'+'\n'
+'c      outside universe'+'\n'
+'c      ---'+'\n'
+'999    0  100:101:-102 imp:n,p=0'+'\n'
+'c      ---'+'\n\n\n'
+'c      ---'+'\n'
+'c      container'+'\n'
+'c      ---'+'\n'
+'100    c/z 17.159 17.159 '+str.format('%.3f'%(radius+container_thickness))+'                       $container - radius + container thickness and changes with plate thickness'+'\n'
 +'101    pz  '+str.format('%.1f'%(surface_26+container_thickness))+'                                      $cap - surface 26 + container thickness'+'\n'
 +'102    pz '+str.format('%.1f'%(surface_22-container_thickness))+'                                        $plug - surface 22 - container thickness'+'\n'
+'c      ---'+'\n'
+'c      end'+'\n'
+'c      ---'+'\n'
+'c'+'\n'
+'c      -----------'+'\n'
+'c      end surface cards'+'\n'
+'c      -----------'+'\n')
###
#
surface_card_output.close()
#
#######
# EOF
#######
