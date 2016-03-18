########################################################################
# R.A.Borrelli
# @TheDoctorRAB
# rev.10.November.2014
# v1.0
########################################################################
# This file executes the mcnpx simulations for the shielding study.
# It should be adaptable to other execution routines.
########################################################################
#
#
#
####### imports
import os

########################################################################
#
#
#
####### change the working directory
print os.getcwd()
os.chdir('C:\\mcnp\\mcnp5\\bin\\Windows')
print os.getcwd()
########################################################################
#
#
#
####### set the commands
#
cmd1='mcnpx c i=75\\continue.inp o=75\\1ad.wwg.54_erd.salt.out r=75\\1ad.wwg.54_erd.salt.con'
cmd2='mcnpx c i=75\\continue.inp o=75\\1bd.wwg.54_erd.metal.out r=75\\1bd.wwg.54_erd.metal.con'
cmd3='mcnpx c i=75\\continue.inp o=75\\2d.wwg.54_er.u.tru.salt.out r=75\\2d.wwg.54_er.u.tru.salt.con'
cmd4='mcnpx c i=75\\continue.inp o=75\\3ad.wwg.54_ew.tru.salt.out r=75\\3ad.wwg.54_ew.tru.salt.con'
cmd5='mcnpx c i=75\\continue.inp o=75\\3bd.wwg.54_ew.tru.cd.out r=75\\3bd.wwg.54_ew.tru.cd.con'
cmd6='mcnpx c i=75\\continue.inp o=75\\4d.wwg.54_ff.alloy.out r=75\\4d.wwg.54_ff.alloy.con'
#
########################################################################
#
#
#
####### select the file
select_file=raw_input('Select file: ')
########################################################################
#
#
#
####### execute simulation
if (select_file=='1'):
    os.system(cmd1)
elif (select_file=='2'):
    os.system(cmd2)
elif (select_file=='3'):
    os.system(cmd3)
elif (select_file=='4'):
    os.system(cmd4)
elif (select_file=='5'):
    os.system(cmd5)
elif (select_file=='6'):
    os.system(cmd6)
# end if
########################################################################
#
#
#
########################################################################
#       EOF
########################################################################    
