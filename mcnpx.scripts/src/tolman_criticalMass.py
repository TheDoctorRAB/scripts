import os
import shutil

lower_bound = 6.000000
upper_bound = 7.000000
lower_tolerance = 0.9997
upper_tolerance = 1.0003

radius_step = (upper_bound - lower_bound) / 4.0

keff = 0
input_radius = lower_bound + radius_step * 2.0

while keff > upper_tolerance or keff < lower_tolerance:
    with open('jezebel_52.inp','r') as input_file, open('temp.inp','w') as output_file:
        count = 1
        for line in input_file:
            if count == 44:
                output_file.write("10     SPH  %.6f    $plutonium sphere\n"%(input_radius))
            else:
                output_file.write(line)
            count = count+1

    shutil.move('temp.inp','jezebel_52.inp')
    
    os.system("del jezebel_52.out")
    os.system("del run*")
    os.system("del sr*")
    os.system("mcnpx i=jezebel_52.inp o=jezebel_52.out")
    
    with open('jezebel_52.out','r') as input_file:
        count = 1
        for line in input_file:
            if count == 1566:
                keff = float(line[27:34])
            count = count+1

    if keff < 1.0:
        input_radius = input_radius + radius_step
    if keff > 1.0:
        input_radius = input_radius - radius_step
    radius_step = radius_step / 2.0
