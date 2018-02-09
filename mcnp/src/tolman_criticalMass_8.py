import os
import shutil

name_array = ["Be","Ni","Graph","Steel","Lead"]
rho_array = ["-1.848","9.1322E-02", "-1.70", "-7.82", "-11.35"]
zaid_array = ["4009 -1.0", "28000.42c -1.0", "6012 -1.0", "6012 -0.005  26000 -0.995", "82000 -1.0"]
output_line_array = [1551, 1550, 1547, 1548, 1545]

with open("cm_8_Total.out",'w') as total_output_file:
    for n in range(len(name_array)):
        file_name = "cm_8_%s"%(name_array[n])
        
        lower_bound = 3.000000
        upper_bound = 9.000000
        lower_tolerance = 0.9997
        upper_tolerance = 1.0003
        
        radius_step = (upper_bound - lower_bound) / 4.0
        
        keff = 0
        input_radius = lower_bound + radius_step * 2.0
        shell_radius = input_radius + 0.1
        
        while keff > upper_tolerance or keff < lower_tolerance:
        #while keff == 0:
            with open('%s.inp'%(file_name),'r') as input_file, open('temp.inp','w') as output_file:
                count = 1
                for line in input_file:
                    if count == 26:
                        output_file.write("101    2 %s     10 -11   imp:n=1    $%s shell\n"%(rho_array[n],
                            name_array[n]))
                    elif count == 39:
                        output_file.write("10     SPH  %.6f    $plutonium sphere\n"%(input_radius))
                    elif count == 41:
                        output_file.write("11     SPH  %.6f    $nickel shell\n"%(shell_radius)) 
                    elif count == 70:
                        output_file.write("M2     %s\n"%(zaid_array[n]))
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
                    if count == output_line_array[n]:
                        keff = float(line[27:34])
                        total_output_line = line
                    count = count+1
        
            if keff < 1.0:
                input_radius = input_radius + radius_step
            if keff > 1.0:
                input_radius = input_radius - radius_step
            shell_radius = input_radius + 0.1
            radius_step = radius_step / 2.0

        total_output_file.write("Output from %s:\n              problem        keff     standard deviation       68%% confidence         95%% confidence         99%% confidence\n%sFinal sphere radius: %.6f\n\n\n"%(name_array[n],total_output_line,input_radius))
