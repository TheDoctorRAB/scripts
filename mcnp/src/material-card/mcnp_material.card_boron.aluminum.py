#######
# @TheDoctorRAB
#######
#
# prepare material card for an mcnp input file
# compute weight fraction and density for boron aluminum given wt% of boron carbide
#
#######
#
# imports
from sys import argv
script=argv
#
#######
#
# data
#
boron_carbide_density=2.52  #g/cc
aluminum_density=2.6989     #g/cc
#
boron_weight_percent=0.782610    #boron in boron carbide
carbon_weight_percent=0.217390 #carbon in boron carbide
#
#######
#
# calculations
#
bc_weight_percent=0.10 #variable wt% in borated aluminum compund
al_weight_percent=1-bc_weight_percent
#
density=((bc_weight_percent/boron_carbide_density)+(al_weight_percent/aluminum_density))**(-1) #principle of additive volumes
#
boron_al_weight_percent=bc_weight_percent*boron_weight_percent
carbon_al_weight_percent=bc_weight_percent*carbon_weight_percent
#
#######
#
# print to screen
#
print density
print '5011.66c  ',boron_al_weight_percent
print '6012.66c  ',carbon_al_weight_percent
print '13027.66c  ',al_weight_percent
#
#######
# EOF
#######
