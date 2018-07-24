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
total_boron_weight_fraction=0.782610    #total boron in boron carbide
carbon_weight_fraction=0.217390         #carbon in boron carbide
#
#######
#
# user set parameters
#
boron10_weight_fraction=float(raw_input('boron 10 weight fraction: '))
boron11_weight_fraction=1-boron10_weight_fraction
#
bc_weight_fraction=float(raw_input('total boron carbide weight fraction: ')) #total boron carbide weight fraction in B4C-aluminum compound
al_weight_fraction=1-bc_weight_fraction
#
#######
#
# calculations
#
density=((bc_weight_fraction/boron_carbide_density)+(al_weight_fraction/aluminum_density))**(-1) #principle of additive volumes
#
boron10_al_weight_fraction=boron10_weight_fraction*bc_weight_fraction*total_boron_weight_fraction #boron 10 weight fraction in B4C-aluminum compound
boron11_al_weight_fraction=boron11_weight_fraction*bc_weight_fraction*total_boron_weight_fraction #boron 11 weight fraction in B4C-aluminum compound
carbon_al_weight_fraction=bc_weight_fraction*carbon_weight_fraction #carbon weight fraction in B4C-aluminum compound
#
#######
#
# print to screen
#
print bc_weight_fraction
print '%.5f'%density
print '5010.66c   ','%.6f'%-boron10_al_weight_fraction
print '5011.66c   ','%.6f'%-boron11_al_weight_fraction
print '6012.66c   ','%.6f'%-carbon_al_weight_fraction
print '13027.66c  ','%.6f'%-al_weight_fraction
print boron10_al_weight_fraction+boron11_al_weight_fraction+carbon_al_weight_fraction+al_weight_fraction
#
#######
# EOF
#######
