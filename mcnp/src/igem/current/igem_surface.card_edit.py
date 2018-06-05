########################################################################
# @TheDoctorRAB
########################################################################
# This script edits the surface cards for the igem single assembly cask.
# The number of spaces is important because MCNP is FORTRAN.
########################################################################
#
#
####### imports
from sys import argv
import numpy
numpy.set_printoptions(suppress=True) #if numbers in array range in order of magnitude, numpy goes auto to scientific notation
script=argv
#######
#
# inputs
# units in cm
#
###
#
# fuel block
#
assembly_width=21.318
assembly_length=assembly_width
assembly_height=400
#
###
#
# fuel rod
#
fuel_pitch=1.254
fuel_radius=0.4095
fuel_height=assembly_height
gap_radius=0.4177
cladding_radius=0.4750
#
###
#
# thickness of gap around assembly, also vertical
#
gap_thickness=5
#
###
#
# cooling plate
#
plate_thickness=3.0
plate_width=assembly_width+2*gap_thickness
plate_length=plate_width
plate_height=assembly_height+2*gap_thickness
#
###
#
# internal pipes
#
pipes_per_plate=4
total_plates=4
torus_height=7.6
pipe_height=plate_height-torus_height #Sakae design constraint
pipe_IR=0.25 #also fluid diameter
pipe_OR=0.30
pipe_half_distance=plate_width/(2*pipes_per_plate) #half distrance between pipes, used for torus radii and pipe
pipe_distance=2*pipe_half_distance #distance between pipes
pipe_plane=0.5*plate_thickness #pipe is located in the midplane of the plate
#
#######
#
# pipe position
#
# pipes are cylinders of fluid surrounded by a cylinder of solid
#
# c/z is used for the surfaces in MCNP
#
# c/z x y R
#
# (x,y) =  position on plate where pipes are located
# R = pipe radius
#
# for the east and west plates, the coordinates are just flipped around
# (x,y) on south plate 1 = (y,x) on west plate 1
# (x,y) on north plate 1 = (y,x) on east plate 1
# no new calculations needed
#
# first position - left to right, bottom to top
#
###
#
pipe_position_south=numpy.zeros((pipes_per_plate*2,3)) #factor of 2 because surface is needed for IR and another for OR
pipe_position_north=numpy.zeros((pipes_per_plate*2,3)) #factor of 2 because surface is needed for IR and another for OR
pipe_position_west=numpy.zeros((pipes_per_plate*2,3)) #factor of 2 because surface is needed for IR and another for OR
pipe_position_east=numpy.zeros((pipes_per_plate*2,3)) #factor of 2 because surface is needed for IR and another for OR
#
###
#
# cylinder radii
#
for i in range (0,(pipes_per_plate*2)):
  if (i%2)==0:
    pipe_position_south[i,2]=pipe_IR
    pipe_position_north[i,2]=pipe_IR
    pipe_position_west[i,2]=pipe_IR
    pipe_position_east[i,2]=pipe_IR
  else:
    pipe_position_south[i,2]=pipe_OR
    pipe_position_north[i,2]=pipe_OR
    pipe_position_west[i,2]=pipe_OR
    pipe_position_east[i,2]=pipe_OR
#
###
#
# y coordinate
#
for i in range (0,(pipes_per_plate*2)):
  pipe_position_south[i,1]=pipe_plane
  pipe_position_north[i,1]=pipe_plane+plate_thickness+plate_width
  pipe_position_west[i,0]=pipe_plane
  pipe_position_east[i,0]=pipe_plane+plate_thickness+plate_width
#
###
#
# first position on north and south plates
# always 2 here because the first position is calculated different than the rest
# because of corner welds
#
for i in range(0,2):
  pipe_position_south[i,0]=pipe_half_distance+plate_thickness
  pipe_position_north[i,0]=pipe_half_distance+plate_thickness
  pipe_position_west[i,1]=pipe_half_distance+plate_thickness
  pipe_position_east[i,1]=pipe_half_distance+plate_thickness
#
###
#
#rest of the positions
#
for i in range(2,(pipes_per_plate*2)):
  pipe_position_south[i,0]=pipe_position_south[i-2,0]+pipe_distance
  pipe_position_north[i,0]=pipe_position_north[i-2,0]+pipe_distance
  pipe_position_west[i,1]=pipe_position_west[i-2,1]+pipe_distance
  pipe_position_east[i,1]=pipe_position_east[i-2,1]+pipe_distance
#
#######
#
# torus position
#
# there are two pipes per torus
#
# a torus is half a donut
#
# same as pipes - cylinders of fluid surrounded by a cylinder of solid
#
# tx or ty is used for the surfaces in MCNP
#
# tx x y z A B C
# ty x y z A B C
#
# (x,y,z) = midpoint of torus
#
# A = radius of the torus
# B = radius of the tube on one end
# C = radius of the tube on the other end
#
# first position - left to right, bottom to top
#
###
#
torus_position_south=numpy.zeros((pipes_per_plate,6))
torus_position_north=numpy.zeros((pipes_per_plate,6))
torus_position_west=numpy.zeros((pipes_per_plate,6))
torus_position_east=numpy.zeros((pipes_per_plate,6))
#
###
#
# pipe radii
#
for i in range(0,pipes_per_plate):
  if (i%2==0):
    torus_position_west[i,4]=pipe_IR
    torus_position_east[i,4]=pipe_IR
    torus_position_south[i,4]=pipe_IR
    torus_position_north[i,4]=pipe_IR
#
    torus_position_west[i,5]=pipe_IR
    torus_position_east[i,5]=pipe_IR
    torus_position_south[i,5]=pipe_IR
    torus_position_north[i,5]=pipe_IR
  else:
    torus_position_west[i,4]=pipe_OR
    torus_position_east[i,4]=pipe_OR
    torus_position_south[i,4]=pipe_OR
    torus_position_north[i,4]=pipe_OR
#
    torus_position_north[i,4]=pipe_OR
    torus_position_west[i,5]=pipe_OR
    torus_position_east[i,5]=pipe_OR
    torus_position_south[i,5]=pipe_OR
    torus_position_north[i,5]=pipe_OR
#
###
#
# torus height - midpoint
# height at center of the donut hole
#
for i in range(0,pipes_per_plate):
  torus_position_west[i,2]=pipe_height
  torus_position_east[i,2]=pipe_height
  torus_position_south[i,2]=pipe_height
  torus_position_north[i,2]=pipe_height
#
###
#
# torus radius
#
for i in range(0,pipes_per_plate):
  torus_position_west[i,3]=pipe_half_distance
  torus_position_east[i,3]=pipe_half_distance
  torus_position_south[i,3]=pipe_half_distance
  torus_position_north[i,3]=pipe_half_distance
#
###
#
# x,y coordinates
#
for i in range(0,pipes_per_plate):
  torus_position_west[i,0]=pipe_plane
  torus_position_east[i,0]=pipe_plane+plate_width+plate_thickness
  torus_position_south[i,1]=pipe_plane
  torus_position_north[i,1]=pipe_plane+plate_width+plate_thickness
#
for i in range(0,pipes_per_plate,2):
 torus_position_west[i,1]=pipe_distance+plate_thickness+i*pipe_distance
 torus_position_west[i+1,1]=pipe_distance+plate_thickness+i*pipe_distance
 torus_position_east[i,1]=pipe_distance+plate_thickness+i*pipe_distance
 torus_position_east[i+1,1]=pipe_distance+plate_thickness+i*pipe_distance
#
 torus_position_south[i,0]=pipe_distance+plate_thickness+i*pipe_distance
 torus_position_south[i+1,0]=pipe_distance+plate_thickness+i*pipe_distance
 torus_position_north[i,0]=pipe_distance+plate_thickness+i*pipe_distance
 torus_position_north[i+1,0]=pipe_distance+plate_thickness+i*pipe_distance
#
#######
#
# fuel lattice 'window' (or assembly)
#
west_boundary=plate_thickness+gap_thickness
east_boundary=west_boundary+assembly_length
south_boundary=gap_thickness+plate_thickness
north_boundary=south_boundary+assembly_width
#
######
#
# unit cell
#
# located lower left of lattice
# coordinates for the center of the unit cell
# use with c/z
#
unit_x=plate_thickness+gap_thickness+0.5*fuel_pitch
unit_y=plate_thickness+gap_thickness+0.5*fuel_pitch
#
#
# unit cell boundary
#
right_edge=plate_thickness+gap_thickness+fuel_pitch
left_edge=plate_thickness+gap_thickness
front_edge=plate_thickness+gap_thickness+fuel_pitch
back_edge=plate_thickness+gap_thickness
#
#######
#
# print to screen
#
print 'assembly dimensions',assembly_width,assembly_length,assembly_height
print 'gap',gap_thickness
print 'plate dimensions',plate_thickness,plate_width,plate_length,plate_height
print 'pipe dimensions',pipe_height,pipe_IR,pipe_OR
print 'pipe distance',pipe_distance,pipe_half_distance,pipe_plane
print
print west_boundary,east_boundary,south_boundary,north_boundary
print unit_x,unit_y
print right_edge,left_edge,front_edge,back_edge
print
print 'pipe position south'
print pipe_position_south
print
print 'pipe position north'
print pipe_position_north
print
print
print 'pipe position west'
print pipe_position_west
print
print 'pipe position east'
print pipe_position_east
print
print
print 'torus position west'
print torus_position_west
print
print 'torus position east'
print torus_position_east
print
print
print 'torus position south'
print torus_position_south
print
print 'torus position north'
print torus_position_north
#
#######
#
# write surfaces to file
#
# set up based on the MCNP file for 4 pipes per plate
# add new surface cards in MCNP first for more pipes
#
surface_card_output=open('igem_surface.card_single.assembly.out','w+')
#
surface_card_output.write('10'+'     px  0          $1'+'\n'
+'11'+'     px  '+str.format('%.3f'%(plate_width+plate_thickness))+'     $plate width + plate thickness'+'\n'
+'13'+'     px  '+str.format('%.1f'%(plate_thickness))+'     $plate thickness'+'\n'
+'14'+'     px  '+str.format('%.3f'%(2*plate_thickness+plate_width))+'     $plate_width + 2*plate thickness'+'\n'
+'c      ---'+'\n'
+'16'+'     py  0          $11'+'\n'
+'17'+'     py  '+str.format('%.3f'%(plate_thickness+plate_width))+'     $plate width + plate thickness'+'\n'
+'19'+'     py  '+str.format('%.1f'%(plate_thickness))+'     $plate thickness'+'\n'
+'20'+'     py  '+str.format('%.3f'%(2*plate_thickness+plate_width))+'     $plate width + 2*plate thickness'+'\n'
+'c      ---'+'\n'
+'22'+'     pz '+str.format('%.1f'%((-1)*plate_thickness))+'     $plate thickness'+'\n'
+'23'+'     py  0          $401'+'\n'
+'24'+'     pz  '+str.format('%.1f'%(pipe_height))+'     $pipe height - 7.6 cm below plate height'+'\n'
+'25'+'     pz  '+str.format('%.1f'%(plate_height))+'     $plate height'+'\n'
+'26'+'     pz  '+str.format('%.1f'%(plate_height+plate_thickness))+'     $plate height + plate thickness'+'\n'
+'30'+'     c/z '+str.format('%.5f'%(pipe_position_south[0,0]))+'  '+str.format('%.2f'%(pipe_position_south[0,1]))+'   '+str.format('%.2f'%(pipe_position_south[0,2]))+'     $fluid radius/pipe IR - south plate 1'+'\n'
+'31'+'     c/z '+str.format('%.5f'%(pipe_position_south[1,0]))+'  '+str.format('%.2f'%(pipe_position_south[1,1]))+'   '+str.format('%.2f'%(pipe_position_south[1,2]))+'     $pipe OR - south plate 1'+'\n'
+'32'+'     c/z '+str.format('%.5f'%(pipe_position_north[0,0]))+'  '+str.format('%.3f'%(pipe_position_north[0,1]))+' '+str.format('%.2f'%(pipe_position_north[0,2]))+'     $fluid radius/pipe IR - north plate 1'+'\n'
+'33'+'     c/z '+str.format('%.5f'%(pipe_position_north[1,0]))+'  '+str.format('%.3f'%(pipe_position_north[1,1]))+' '+str.format('%.2f'%(pipe_position_north[1,2]))+'     $pipe OR - north plate 1'+'\n'
+'c      ---'+'\n'
+'34'+'     c/z '+str.format('%.5f'%(pipe_position_south[2,0]))+' '+str.format('%.2f'%(pipe_position_south[2,1]))+'   '+str.format('%.2f'%(pipe_position_south[2,2]))+'     $fluid radius/pipe IR - south plate 2'+'\n'
+'35'+'     c/z '+str.format('%.5f'%(pipe_position_south[3,0]))+' '+str.format('%.2f'%(pipe_position_south[3,1]))+'   '+str.format('%.2f'%(pipe_position_south[3,2]))+'     $pipe OR - south plate 2'+'\n'
+'36'+'     c/z '+str.format('%.5f'%(pipe_position_north[2,0]))+' '+str.format('%.3f'%(pipe_position_north[2,1]))+' '+str.format('%.2f'%(pipe_position_north[2,2]))+'     $fluid radius/pipe IR - north plate 2'+'\n'
+'37'+'     c/z '+str.format('%.5f'%(pipe_position_north[3,0]))+' '+str.format('%.3f'%(pipe_position_north[3,1]))+' '+str.format('%.2f'%(pipe_position_north[3,2]))+'     $pipe OR - north plate 2'+'\n'
+'c      ---'+'\n'
+'38'+'     c/z '+str.format('%.5f'%(pipe_position_south[4,0]))+' '+str.format('%.2f'%(pipe_position_south[4,1]))+'   '+str.format('%.2f'%(pipe_position_south[4,2]))+'     $fluid radius/pipe IR - south plate 3'+'\n'
+'39'+'     c/z '+str.format('%.5f'%(pipe_position_south[5,0]))+' '+str.format('%.2f'%(pipe_position_south[5,1]))+'   '+str.format('%.2f'%(pipe_position_south[5,2]))+'     $pipe OR - south plate 3'+'\n'
+'40'+'     c/z '+str.format('%.5f'%(pipe_position_north[4,0]))+' '+str.format('%.3f'%(pipe_position_north[4,1]))+' '+str.format('%.2f'%(pipe_position_north[4,2]))+'     $fluid radius/pipe IR - north plate 3'+'\n'
+'41'+'     c/z '+str.format('%.5f'%(pipe_position_north[5,0]))+' '+str.format('%.3f'%(pipe_position_north[5,1]))+' '+str.format('%.2f'%(pipe_position_north[5,2]))+'     $pipe OR - north plate 3'+'\n'
+'c      ---'+'\n'
+'42'+'     c/z '+str.format('%.5f'%(pipe_position_south[6,0]))+' '+str.format('%.2f'%(pipe_position_south[6,1]))+'   '+str.format('%.2f'%(pipe_position_south[6,2]))+'     $fluid radius/pipe IR - south plate 4'+'\n'
+'43'+'     c/z '+str.format('%.5f'%(pipe_position_south[7,0]))+' '+str.format('%.2f'%(pipe_position_south[7,1]))+'   '+str.format('%.2f'%(pipe_position_south[7,2]))+'     $pipe OR - south plate 4'+'\n'
+'44'+'     c/z '+str.format('%.5f'%(pipe_position_north[6,0]))+' '+str.format('%.3f'%(pipe_position_north[6,1]))+' '+str.format('%.2f'%(pipe_position_north[6,2]))+'     $fluid radius/pipe IR - north plate 4'+'\n'
+'45'+'     c/z '+str.format('%.5f'%(pipe_position_north[7,0]))+' '+str.format('%.3f'%(pipe_position_north[7,1]))+' '+str.format('%.2f'%(pipe_position_north[7,2]))+'     $pipe OR - north plate 4'+'\n'
+'c      ---'+'\n'
+'46'+'     c/z '+str.format('%.2f'%(pipe_position_west[0,0]))+'   '+str.format('%.5f'%(pipe_position_west[0,1]))+'  '+str.format('%.2f'%(pipe_position_west[0,2]))+'     $fluid radius/pipe IR - west plate 1'+'\n'
+'47'+'     c/z '+str.format('%.2f'%(pipe_position_west[1,0]))+'   '+str.format('%.5f'%(pipe_position_west[1,1]))+'  '+str.format('%.2f'%(pipe_position_west[1,2]))+'     $pipe OR - west plate 1'+'\n'
+'48'+'     c/z '+str.format('%.3f'%(pipe_position_east[0,0]))+' '+str.format('%.5f'%(pipe_position_east[0,1]))+'  '+str.format('%.2f'%(pipe_position_east[0,2]))+'     $fluid radius/pipe IR - east plate 1'+'\n'
+'49'+'     c/z '+str.format('%.3f'%(pipe_position_east[1,0]))+' '+str.format('%.5f'%(pipe_position_east[1,1]))+'  '+str.format('%.2f'%(pipe_position_east[1,2]))+'     $pipe OR - east plate 1'+'\n'
+'c      ---'+'\n'
+'50'+'     c/z '+str.format('%.2f'%(pipe_position_west[2,0]))+'   '+str.format('%.5f'%(pipe_position_west[2,1]))+' '+str.format('%.2f'%(pipe_position_west[2,2]))+'     $fluid radius/pipe IR - west plate 2'+'\n'
+'51'+'     c/z '+str.format('%.2f'%(pipe_position_west[3,0]))+'   '+str.format('%.5f'%(pipe_position_west[3,1]))+' '+str.format('%.2f'%(pipe_position_west[3,2]))+'     $pipe OR - west plate 2'+'\n'
+'52'+'     c/z '+str.format('%.3f'%(pipe_position_east[2,0]))+' '+str.format('%.5f'%(pipe_position_east[2,1]))+' '+str.format('%.2f'%(pipe_position_east[2,2]))+'     $fluid radius/pipe IR - east plate 2'+'\n'
+'53'+'     c/z '+str.format('%.3f'%(pipe_position_east[3,0]))+' '+str.format('%.5f'%(pipe_position_east[3,1]))+' '+str.format('%.2f'%(pipe_position_east[3,2]))+'     $pipe OR - east plate 2'+'\n'
+'c      ---'+'\n'
+'54'+'     c/z '+str.format('%.2f'%(pipe_position_west[4,0]))+'   '+str.format('%.5f'%(pipe_position_west[4,1]))+' '+str.format('%.2f'%(pipe_position_west[4,2]))+'     $fluid radius/pipe IR - west plate 3'+'\n'
+'55'+'     c/z '+str.format('%.2f'%(pipe_position_west[5,0]))+'   '+str.format('%.5f'%(pipe_position_west[5,1]))+' '+str.format('%.2f'%(pipe_position_west[5,2]))+'     $pipe OR - west plate 3'+'\n'
+'56'+'     c/z '+str.format('%.3f'%(pipe_position_east[4,0]))+' '+str.format('%.5f'%(pipe_position_east[4,1]))+' '+str.format('%.2f'%(pipe_position_east[4,2]))+'     $fluid radius/pipe IR - east plate 3'+'\n'
+'57'+'     c/z '+str.format('%.3f'%(pipe_position_east[5,0]))+' '+str.format('%.5f'%(pipe_position_east[5,1]))+' '+str.format('%.2f'%(pipe_position_east[5,2]))+'     $pipe OR - east plate 3'+'\n'
+'c      ---'+'\n'
+'58'+'     c/z '+str.format('%.2f'%(pipe_position_west[6,0]))+'   '+str.format('%.5f'%(pipe_position_west[6,1]))+' '+str.format('%.2f'%(pipe_position_west[6,2]))+'     $fluid radius/pipe IR - west plate 4'+'\n'
+'59'+'     c/z '+str.format('%.2f'%(pipe_position_west[7,0]))+'   '+str.format('%.5f'%(pipe_position_west[7,1]))+' '+str.format('%.2f'%(pipe_position_west[7,2]))+'     $pipe OR - west plate 4'+'\n'
+'60'+'     c/z '+str.format('%.3f'%(pipe_position_east[6,0]))+' '+str.format('%.5f'%(pipe_position_east[6,1]))+' '+str.format('%.2f'%(pipe_position_east[6,2]))+'     $fluid radius/pipe IR - east plate 4'+'\n'
+'61'+'     c/z '+str.format('%.3f'%(pipe_position_east[7,0]))+' '+str.format('%.5f'%(pipe_position_east[7,1]))+' '+str.format('%.2f'%(pipe_position_east[7,2]))+'     $pipe OR - east plate 4'+'\n'
+'c      ---'+'\n'
+'62'+'     tx '+str.format('%.2f'%(torus_position_west[0,0]))+' '+str.format('%.4f'%(torus_position_west[0,1]))+'   '+str.format('%.1f'%(torus_position_west[0,2]))+'   '+str.format('%.5f'%(torus_position_west[0,3]))+' '+str.format('%.2f'%(torus_position_west[0,4]))+' '+str.format('%.2f'%(torus_position_west[0,5]))+'     $fluid - west plate 1 - change z for height'+'\n'
+'63'+'     tx '+str.format('%.2f'%(torus_position_west[1,0]))+' '+str.format('%.4f'%(torus_position_west[1,1]))+'   '+str.format('%.1f'%(torus_position_west[1,2]))+'   '+str.format('%.5f'%(torus_position_west[1,3]))+' '+str.format('%.2f'%(torus_position_west[1,4]))+' '+str.format('%.2f'%(torus_position_west[1,5]))+'     $pipe - west plate 1 - change z for height'+'\n'
+'64'+'     tx '+str.format('%.2f'%(torus_position_west[2,0]))+' '+str.format('%.5f'%(torus_position_west[2,1]))+' '+str.format('%.1f'%(torus_position_west[2,2]))+' '+str.format('%.5f'%(torus_position_west[2,3]))+' '+str.format('%.2f'%(torus_position_west[2,4]))+' '+str.format('%.2f'%(torus_position_west[2,5]))+'     $fluid - west plate 2 - change z for height'+'\n'
+'65'+'     tx '+str.format('%.2f'%(torus_position_west[3,0]))+' '+str.format('%.5f'%(torus_position_west[3,1]))+' '+str.format('%.1f'%(torus_position_west[3,2]))+' '+str.format('%.5f'%(torus_position_west[3,3]))+' '+str.format('%.2f'%(torus_position_west[3,4]))+' '+str.format('%.2f'%(torus_position_west[3,5]))+'     $pipe - west plate 2 - change z for height'+'\n'
+'c      ---'+'\n'
+'66'+'     tx '+str.format('%.3f'%(torus_position_east[0,0]))+' '+str.format('%.4f'%(torus_position_east[0,1]))+'   '+str.format('%.1f'%(torus_position_east[0,2]))+' '+str.format('%.5f'%(torus_position_east[0,3]))+' '+str.format('%.2f'%(torus_position_east[0,4]))+' '+str.format('%.2f'%(torus_position_east[0,5]))+'     $fluid - east plate 1 - change z for height'+'\n'
+'67'+'     tx '+str.format('%.3f'%(torus_position_east[1,0]))+' '+str.format('%.4f'%(torus_position_east[1,1]))+'   '+str.format('%.1f'%(torus_position_east[1,2]))+' '+str.format('%.5f'%(torus_position_east[1,3]))+' '+str.format('%.2f'%(torus_position_east[1,4]))+' '+str.format('%.2f'%(torus_position_east[1,5]))+'     $pipe - east plate 1 - change z for height'+'\n'
+'68'+'     tx '+str.format('%.3f'%(torus_position_east[2,0]))+' '+str.format('%.4f'%(torus_position_east[2,1]))+'  '+str.format('%.1f'%(torus_position_east[2,2]))+' '+str.format('%.5f'%(torus_position_east[2,3]))+' '+str.format('%.2f'%(torus_position_east[2,4]))+' '+str.format('%.2f'%(torus_position_east[2,5]))+'     $fluid - east plate 2 - change z for height'+'\n'
+'69'+'     tx '+str.format('%.3f'%(torus_position_east[3,0]))+' '+str.format('%.4f'%(torus_position_east[3,1]))+'  '+str.format('%.1f'%(torus_position_east[3,2]))+' '+str.format('%.5f'%(torus_position_east[3,3]))+' '+str.format('%.2f'%(torus_position_east[3,4]))+' '+str.format('%.2f'%(torus_position_east[3,5]))+'     $pipe - east plate 2 - change z for height'+'\n'
+'c      ---'+'\n'
+'70'+'     ty '+str.format('%.4f'%(torus_position_south[0,0]))+'   '+str.format('%.2f'%(torus_position_south[0,1]))+'   '+str.format('%.1f'%(torus_position_south[0,2]))+' '+str.format('%.5f'%(torus_position_south[0,3]))+' '+str.format('%.2f'%(torus_position_south[0,4]))+' '+str.format('%.2f'%(torus_position_south[0,5]))+'     $fluid - south plate 1 - change z for height'+'\n'
+'71'+'     ty '+str.format('%.4f'%(torus_position_south[1,0]))+'   '+str.format('%.2f'%(torus_position_south[1,1]))+'   '+str.format('%.1f'%(torus_position_south[1,2]))+' '+str.format('%.5f'%(torus_position_south[1,3]))+' '+str.format('%.2f'%(torus_position_south[1,4]))+' '+str.format('%.2f'%(torus_position_south[1,5]))+'     $pipe - south plate 1 - change z for height'+'\n'
+'72'+'     ty '+str.format('%.4f'%(torus_position_south[2,0]))+'  '+str.format('%.2f'%(torus_position_south[2,1]))+'   '+str.format('%.1f'%(torus_position_south[2,2]))+' '+str.format('%.5f'%(torus_position_south[2,3]))+' '+str.format('%.2f'%(torus_position_south[2,4]))+' '+str.format('%.2f'%(torus_position_south[2,5]))+'     $fluid - south plate 2 - change z for height'+'\n'
+'73'+'     ty '+str.format('%.4f'%(torus_position_south[3,0]))+'  '+str.format('%.2f'%(torus_position_south[3,1]))+'   '+str.format('%.1f'%(torus_position_south[3,2]))+' '+str.format('%.5f'%(torus_position_south[3,3]))+' '+str.format('%.2f'%(torus_position_south[3,4]))+' '+str.format('%.2f'%(torus_position_south[3,5]))+'     $pipe - south plate 2 - change z for height'+'\n'
+'c      ---'+'\n'
+'74'+'     ty '+str.format('%.4f'%(torus_position_north[0,0]))+'   '+str.format('%.3f'%(torus_position_north[0,1]))+' '+str.format('%.1f'%(torus_position_north[0,2]))+' '+str.format('%.5f'%(torus_position_north[0,3]))+' '+str.format('%.2f'%(torus_position_north[0,4]))+' '+str.format('%.2f'%(torus_position_north[0,5]))+'     $fluid - north plate 1 - change z for height'+'\n'
+'75'+'     ty '+str.format('%.4f'%(torus_position_north[1,0]))+'   '+str.format('%.3f'%(torus_position_north[1,1]))+' '+str.format('%.1f'%(torus_position_north[1,2]))+' '+str.format('%.5f'%(torus_position_north[1,3]))+' '+str.format('%.2f'%(torus_position_north[1,4]))+' '+str.format('%.2f'%(torus_position_north[1,5]))+'     $pipe - north plate 1 - change z for height'+'\n'
+'76'+'     ty '+str.format('%.4f'%(torus_position_north[2,0]))+'  '+str.format('%.3f'%(torus_position_north[2,1]))+' '+str.format('%.1f'%(torus_position_north[2,2]))+' '+str.format('%.5f'%(torus_position_north[2,3]))+' '+str.format('%.2f'%(torus_position_north[2,4]))+' '+str.format('%.2f'%(torus_position_north[2,5]))+'     $fluid - north plate 2 - change z for height'+'\n'
+'77'+'     ty '+str.format('%.4f'%(torus_position_north[3,0]))+'  '+str.format('%.3f'%(torus_position_north[3,1]))+' '+str.format('%.1f'%(torus_position_north[3,2]))+' '+str.format('%.5f'%(torus_position_north[3,3]))+' '+str.format('%.2f'%(torus_position_north[3,4]))+' '+str.format('%.2f'%(torus_position_north[3,5]))+'     $pipe - north plate 2 - change z for height'+'\n'
+'c      ---'+'\n'
+'78'+'     px '+str.format('%.1f'%(west_boundary))+'     $fuel block - change for gap or thickness'+'\n'
+'79'+'     px '+str.format('%.3f'%(east_boundary))+'     $fuel block - change for gap or thickness'+'\n'
+'c      ---'+'\n'
+'80'+'     py '+str.format('%.1f'%(south_boundary))+'     $fuel block - change for gap or thickness'+'\n'
+'81'+'     py '+str.format('%.3f'%(north_boundary))+'     $fuel block - change for gap or thickness'+'\n'
+'c      ---'+'\n'
+'82'+'     pz '+str.format('%.0f'%(gap_thickness))+'     $fuel block - change for gap or thickness'+'\n'
+'83'+'     pz '+str.format('%.0f'%(gap_thickness+assembly_height))+'     $fuel block - change for gap or thickness'+'\n'
+'c      ---'+'\n'
+'90'+'     c/z '+str.format('%.3f'%(unit_x))+' '+str.format('%.3f'%(unit_y))+' '+str.format('%.4f'%(fuel_radius))+'     $fuel rod radius'+'\n'
+'91'+'     c/z '+str.format('%.3f'%(unit_x))+' '+str.format('%.3f'%(unit_y))+' '+str.format('%.4f'%(gap_radius))+'     $fuel rod gap radius'+'\n'
+'92'+'     c/z '+str.format('%.3f'%(unit_x))+' '+str.format('%.3f'%(unit_y))+' '+str.format('%.4f'%(cladding_radius))+'     $fuel rod cladding radius'+'\n'
+'c      ---'+'\n'
+'93'+'     px '+str.format('%.3f'%(right_edge))+'     $right edge of cell - thickness + gap + pitch'+'\n'
+'94'+'     px '+str.format('%.1f'%(left_edge))+'     $left edge of cell - thickness + gap + pitch'+'\n'
+'c      ---'+'\n'
+'95'+'     py '+str.format('%.3f'%(front_edge))+'     $front edge of cell - thickness + gap + pitch'+'\n'
+'96'+'     py '+str.format('%.1f'%(back_edge))+'     $back edge of cell - thickness + gap + pitch'+'\n')
#
surface_card_output.close()
#
#######
#
#
########################################################################
#      EOF
########################################################################
