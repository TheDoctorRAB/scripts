import os
import shutil

file_name = "cm_7"

lower_bound = 3.000000
upper_bound = 9.000000
lower_tolerance = 0.9997
upper_tolerance = 1.0003

radius_step = (upper_bound - lower_bound) / 4.0

keff = 0
input_radius = lower_bound + radius_step * 2.0
#cylinder_height = input_radius

calc_count = 0

while keff > upper_tolerance or keff < lower_tolerance:
    with open('%s.inp'%(file_name),'r') as input_file, open('temp.inp','w') as output_file:
        count = 1
        for line in input_file:
            if count == 43:
                output_file.write("10     rcc 0 0 -3.0   0 0 6.0   %.6f    $plutonium cylinder\n"\
                        %(input_radius))
            else:
                output_file.write(line)
            count = count+1

    shutil.move('temp.inp','%s.inp'%(file_name))
    
    os.system("del %s.out"%(file_name))
    os.system("del run*")
    os.system("del sr*")
    os.system("mcnpx i=%s.inp o=%s.out"%(file_name,file_name))
    
    with open('%s.out'%(file_name),'r') as input_file:
        count = 1
        for line in input_file:
            if count == 1553:
                keff = float(line[27:34])
            count = count+1

    if keff < 1.0:
         input_radius = input_radius + radius_step
    if keff > 1.0:
        input_radius = input_radius - radius_step
    radius_step = radius_step / 2.0

    #if calc_count%4 == 0 and keff > 1.5:
    #    cylinder_height = cylinder_height / 2.0
    #    radius_step = input_radius / 2.0
