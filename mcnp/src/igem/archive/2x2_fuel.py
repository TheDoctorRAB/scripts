# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

w = 20.32 #width of the cooling plates
h1 = 165 #Total plate height
thk = 1.5 #plate thickness
r1 = 0.25 #inner radius of the cooling tubes
r2 = 0.3 #outer radius of the cooling tubes
distt = (w-thk)/8 #half the distance between cooling cylinders, used in defining torus radii
distc = distt*2 #distance between cooling cylinders
tspace = 165 - 157.4 #height to top of the cooling plate beyond the height of the the cooling tubes, not including the torus
h2 = 157.4 #Height of cylinders
'''
all densities in g/cc
'''

mat1 = 1 #al
dens1 = 1
mat2 = 2 #fuel
dens2 = 1
mat3 = 3 #fluid
dens3 = 1
mat4 = 4 #pipe
dens4 = 1
mat5 = 5 #atmosphere
dens5 = 1 

ycord1 = thk+(w-thk)/8
xcord1 = ycord1




'''
Begin code to generate spacing material cells at each corner
'''
cel = 1
print('c')    
print('c - Begin Cell cards')
crnr = 11

print('c')    
print('c - Corner spacers')
while (cel<10): 
    print(cel, mat1, -dens1, 1, -4, crnr, -crnr-3, 401, -403, 'imp:n=1'  )
    print(cel+1, mat1, -dens1, 2, -5, crnr, -crnr-3, 401, -403, 'imp:n=1'  )
    print(cel+2, mat1, -dens1, 3, -6, crnr, -crnr-3, 401, -403, 'imp:n=1'  )
    crnr = crnr + 1
    cel=cel+3
print('c')    
'''
End code to generate spacing material cells at each corner
'''


'''
Begin code to generate fuel array cells
'''
print('c - Fuel arrays')
cel = 10 # cell set to ten to allow up to 9 cells for 9 spacers needed in 2x2
print(cel, mat2, -dens2, 14, -12, 4, -2, 401, -403, 'imp:n=1'  )
cel = cel+1
print(cel, mat2, -dens2, 15, -13, 4, -2, 401, -403, 'imp:n=1'  )
cel = cel+1
print(cel, mat2, -dens2, 14, -12, 5, -3, 401, -403, 'imp:n=1'  )
cel = cel+1
print(cel, mat2, -dens2, 15, -13, 5, -3, 401, -403, 'imp:n=1'  )
'''
End code to generate fuel array cells
'''


'''
Begin code to generate the cooling tube cells
'''
print('c')    
print('c cooling tubes running parallel to the x-axis' )
print('c')  

cel = 15 # cell set to 15 to allow up to 4 cells for 4 fuel arrays in 2x2
cyl = 80 # First surface selection for cell iterations runs through the first layer of cylinders
while (cel<63):  
    #first layer of cylinders
    print(cel, mat3, -dens3, -cyl,  401, -402, 'imp:n=1'  )
    print(cel+1, mat4, -dens3, cyl, -cyl -1, 401, -402, 'imp:n=1'  )
    print('c')
    #second layer of cylinders
    print(cel+2, mat3, -dens3, -cyl - 20,  401, -402, 'imp:n=1'  )
    print(cel+3, mat4, -dens3, cyl + 20, -cyl -21, 401, -402, 'imp:n=1'  )
    print('c')
    #third layer of cylinders
    print(cel+4, mat3, -dens3, -cyl - 40,  401, -402, 'imp:n=1'  )
    print(cel+5, mat4, -dens3, cyl + 40, -cyl -41, 401, -402, 'imp:n=1'  )
    print('c')
    cel = cel + 6
    cyl = cyl + 2


print('c')    
print('c cooling tubes running parallel to the y-axis' )
print('c')  

'''
Need to account for 48 tubes, cells 15 through 63
'''

cel = 63 #couter resets

cyl = 20  # First surface selection for cell iterations runs through the first layer of cylinders
while (cel<111): #up to 111 
    #first layer of cylinders
    print(cel, mat3, -dens3, -cyl,  401, -402, 'imp:n=1'  )
    print(cel+1, mat4, -dens3, cyl, -cyl -1, 401, -402, 'imp:n=1'  )
    print('c')
    #second layer of cylinders
    print(cel+2, mat3, -dens3, -cyl - 20,  401, -402, 'imp:n=1'  )
    print(cel+3, mat4, -dens3, cyl + 20, -cyl -21, 401, -402, 'imp:n=1'  )
    print('c')
    #third layer of cylinders
    print(cel+4, mat3, -dens3, -cyl - 40,  401, -402, 'imp:n=1'  )
    print(cel+5, mat4, -dens3, cyl + 40, -cyl -41, 401, -402, 'imp:n=1'  )
    print('c')
    cel = cel + 6
    cyl = cyl + 2
print('c')    

'''
End code to generate the cooling tube cells
'''


'''
Begin code to generate the cooling tube torus cells
'''
print('c')    
print('c cooling torus running parallel to the y-axis' )
print('c')  
cel = 111
tor=201

while (cel<132): 
    print(cel, mat3, -dens3, -tor, 402, 'imp:n=1'  )
    print(cel+1, mat4, -dens3, tor, -tor -1, 402, 'imp:n=1'  )
    cel = cel + 2
    tor = tor + 2
    print(cel, mat3, -dens3, -tor, 402, 'imp:n=1'  )
    print(cel+1, mat4, -dens3, tor, -tor -1, 402, 'imp:n=1'  )
    cel = cel + 2
    tor = tor + 2
    print(cel, mat3, -dens3, -tor, 402, 'imp:n=1'  )
    print(cel+1, mat4, -dens3, tor, -tor -1, 402, 'imp:n=1'  )
    cel = cel + 2
    tor = tor + 2
    print(cel, mat3, -dens3, -tor, 402, 'imp:n=1'  )
    print(cel+1, mat4, -dens3, tor, -tor -1, 402, 'imp:n=1'  )
    cel = cel + 2
    tor = tor + 4
    print('c')

print('c')    
print('c cooling torus running parallel to the x-axis' )
print('c')  


cel = 135
tor = 301 #reset torus counter
while (cel<158): 
    print(cel, mat3, -dens3, -tor, 402, 'imp:n=1'  )
    print(cel+1, mat4, -dens3, tor, -tor -1, 402, 'imp:n=1'  )

    cel = cel + 2
    tor = tor + 2
    print(cel, mat3, -dens3, -tor, 402, 'imp:n=1'  )
    print(cel+1, mat4, -dens3, tor, -tor -1, 402, 'imp:n=1'  )
    cel = cel + 2
    tor = tor + 2
    print(cel, mat3, -dens3, -tor, 402, 'imp:n=1'  )
    print(cel+1, mat4, -dens3, tor, -tor -1, 402, 'imp:n=1'  )
    cel = cel + 2
    tor = tor + 2
    print(cel, mat3, -dens3, -tor, 402, 'imp:n=1'  )
    print(cel+1, mat4, -dens3, tor, -tor -1, 402, 'imp:n=1'  )
    cel = cel + 2
    tor = tor + 4
    print('c')
print('c')    

'''
End code to generate the cooling tube torus cells
'''



'''
Begin code to generate aluminum plates
'''
cel = 159

sury1=11 #begin y surface counter for iteration


tor = 111
sury1=14 #begin x surface counter for iteration
print('c - plates parallel to y axis') 
cyl = 63 
# plates parallel to y axis
cel= 159 #reset cell counter 
while (cel<165): 
    print(cel, ' ', mat1,' ', -dens3,' ', 1,' ', -4,' ', sury1,' ', -sury1 + 2,' ',  401,' ', -403,' ', '\n',
          '     ', "#", cyl,' ', "#",cyl+1,' ', "#",cyl+12,' ', "#",cyl+13,' ', "#",cyl+24,' ', "#",cyl+25,' ', "#",cyl+36,' ', "#", cyl+37,' ','\n',
          '     ', "#", tor, ' ', "#",tor+1,' ', "#",tor+2, ' ',"#",tor+3, ' ','\n',
          '     ', 'imp:n=1', sep ='')
    print('c')  
    cyl=cyl+2
    cel = cel + 1  
    tor = tor + 8  
    print(cel, ' ', mat1,' ', -dens3,' ', 2,' ', -5,' ', sury1,' ', -sury1 + 2,' ',  401,' ', -403,' ', '\n',
          '     ', "#", cyl,' ', "#",cyl+1,' ', "#",cyl+12,' ', "#",cyl+13,' ', "#",cyl+24,' ', "#",cyl+25,' ', "#",cyl+36,' ', "#", cyl+37,' ','\n',
          '     ', "#", tor, ' ', "#",tor+1,' ', "#",tor+2, ' ',"#",tor+3, ' ','\n',
          '     ', 'imp:n=1', sep ='')
    print('c')  
    cyl=cyl+2
    cel = cel + 1  
    tor = tor + 8  
    print(cel, ' ', mat1,' ', -dens3,' ', 3,' ', -6,' ', sury1,' ', -sury1 + 2,' ',  401,' ', -403,' ', '\n',
          '     ', "#", cyl,' ', "#",cyl+1,' ', "#",cyl+12,' ', "#",cyl+13,' ', "#",cyl+24,' ', "#",cyl+25,' ', "#",cyl+36,' ', "#", cyl+37,' ','\n',
          '     ', "#", tor, ' ', "#",tor+1,' ', "#",tor+2, ' ',"#",tor+3, ' ','\n',
          '     ', 'imp:n=1', sep ='')
    cel = cel + 1 
    sury1 = sury1 +1
    cyl = 69
    tor = 115

cel = 165
tor = 135
sury1=4
cyl = 15 
print('c - plates parallel to x axis') 
# plates parallel to x axis
while (cel<171): #  
    print(cel, ' ', mat1,' ', -dens3,' ', 11,' ', -14,' ', sury1,' ', -sury1 + 2,' ',  401,' ', -403,' ', '\n',
          '     ', "#", cyl,' ', "#",cyl+1,' ', "#",cyl+12,' ', "#",cyl+13,' ', "#",cyl+24,' ', "#",cyl+25,' ', "#",cyl+36,' ', "#", cyl+37,' ','\n',
          '     ', "#", tor, ' ', "#",tor+1,' ', "#",tor+2, ' ',"#",tor+3, ' ','\n',
          '     ', 'imp:n=1', sep ='')
    print('c')  
    cyl=cyl+2
    cel = cel + 1  
    tor = tor + 8  
    print(cel, ' ', mat1,' ', -dens3,' ', 12,' ', -15,' ', sury1,' ', -sury1 + 2,' ',  401,' ', -403,' ', '\n',
          '     ', "#", cyl,' ', "#",cyl+1,' ', "#",cyl+12,' ', "#",cyl+13,' ', "#",cyl+24,' ', "#",cyl+25,' ', "#",cyl+36,' ', "#", cyl+37,' ','\n',
          '     ', "#", tor, ' ', "#",tor+1,' ', "#",tor+2, ' ',"#",tor+3, ' ','\n',
          '     ', 'imp:n=1', sep ='')
    print('c')  
    cyl=cyl+2
    cel = cel + 1  
    tor = tor + 8  
    print(cel, ' ', mat1,' ', -dens3,' ', 13,' ', -16,' ', sury1,' ', -sury1 + 2,' ',  401,' ', -403,' ', '\n',
          '     ', "#", cyl,' ', "#",cyl+1,' ', "#",cyl+12,' ', "#",cyl+13,' ', "#",cyl+24,' ', "#",cyl+25,' ', "#",cyl+36,' ', "#", cyl+37,' ','\n',
          '     ', "#", tor, ' ', "#",tor+1,' ', "#",tor+2, ' ',"#",tor+3, ' ','\n',
          '     ', 'imp:n=1', sep ='')
    cel = cel + 1 
    sury1 = sury1 +1
    cyl = 21
    tor = 139


print('c')
'''
End code to generate aluminum plates
'''
'''
Begin code to generate top and bottom aluminum plates
'''
print('c - top and bottom plate')


print( cel, mat1, -dens1, 1, -6, 11, -16, 403, -404, 'imp:n=1'  )
cel = cel + 1
print( cel, mat1, -dens1, 1, -6, 11, -16, 400, -401, 'imp:n=1'  )

'''
End code to generate top and bottom aluminum plates
'''

# exterior void
cel = cel + 1
print( cel, mat5, -dens5, '-1:6:-11:16:-400:404',  'imp:n=1'  )

'''
Begin Surface generation
'''


'''
Begin code to generate X and Y planes
'''
print()
print('c - Begin Surface cards')
xsur1 = 0
xsur2 = thk
sur = 1
for sur in range (1,4):
    print(sur, 'px', xsur1 ) #xplanes, iterate for 6 entries
    sur = sur + 1
    xsur1 = xsur1 + w
    
print('c')
for sur in range (4,7):
    print(sur, 'px', xsur2 ) #xplanes, iterate for 6 entries
    sur = sur + 1
    xsur2 = xsur2 + w
print('c')


ysur1 = 0
ysur2 = thk
sur = 1
for sur in range (11,14):
    print(sur, 'py', ysur1 ) #yplanes, iterate for 6 entries
    sur = sur + 1
    ysur1 = ysur1 + w
    
print('c')
for sur in range (14,17):
    print(sur, 'py', ysur2 ) #yplanes, iterate for 6 entries
    sur = sur + 1
    ysur2 = ysur2 + w
print('c')    

'''
End code to generate X and Y planes
'''

'''
Begin code to generate cylinders parallel to the y and x axes, orthogonal to the z

'''

print('c level 1 parallel to y cylinders')

print('c')
ycoord1 = ycord1
ycoord2 = ycoord1 + w


sur = 20

while (sur < 36):
    print(sur, 'c/z', thk/2, ycoord1, r1 ) # inner cylinder
    print(sur + 1, 'c/z', thk/2, ycoord1, r2 ) #outer cylinder
    print(sur + 2, 'c/z', thk/2, ycoord2, r1 ) # inner cylinder
    print(sur + 3, 'c/z', thk/2, ycoord2, r2 ) #outer cylinder
    ycoord2 = ycoord2 + distc
    ycoord1 = ycoord1 + distc
    sur = sur + 4
print('c')

print('c level 2 parallel to y cylinders')

print('c')
ycoord1 = ycord1
ycoord2 = ycoord1 + w

sur = 40

while (sur < 56):
    print(sur, 'c/z', thk/2 + w, ycoord1, r1 ) # inner cylinder
    print(sur + 1, 'c/z', thk/2 + w, ycoord1, r2 ) #outer cylinder
    print(sur + 2, 'c/z', thk/2 + w, ycoord2, r1 ) # inner cylinder
    print(sur + 3, 'c/z', thk/2 + w, ycoord2, r2 ) #outer cylinder
    ycoord2 = ycoord2 + distc
    ycoord1 = ycoord1 + distc
    sur = sur + 4
print('c')

print('c level 3 parallel to y cylinders')

print('c')
ycoord1 = ycord1
ycoord2 = ycoord1 + w

sur = 60

while (sur < 76):
    print(sur, 'c/z', thk/2 + w*2, ycoord1, r1 ) # inner cylinder
    print(sur + 1, 'c/z', thk/2 + w*2, ycoord1, r2 ) #outer cylinder
    print(sur + 2, 'c/z', thk/2 + w*2, ycoord2, r1 ) # inner cylinder
    print(sur + 3, 'c/z', thk/2 + w*2, ycoord2, r2 ) #outer cylinder
    ycoord2 = ycoord2 + distc
    ycoord1 = ycoord1 + distc
    sur = sur + 4
print('c')

print('c level 1 parallel to x cylinders')

print('c')
xcoord1 = xcord1
xcoord2 = xcoord1 + w

sur = 80

while (sur < 96):
    print(sur, 'c/z', xcoord1, thk/2, r1 ) # inner cylinder
    print(sur + 1, 'c/z', xcoord1, thk/2, r2 ) #outer cylinder
    print(sur + 2, 'c/z', xcoord2, thk/2, r1 ) # inner cylinder
    print(sur + 3, 'c/z',xcoord2, thk/2, r2 ) #outer cylinder
    xcoord2 = xcoord2 + distc
    xcoord1 = xcoord1 + distc
    sur = sur + 4
print('c')

print('c level 2 parallel to x cylinders')

print('c')
xcoord1 = xcord1
xcoord2 = xcoord1 + w

sur = 100

while (sur < 116):
    print(sur, 'c/z', xcoord1, thk/2 + w, r1 ) # inner cylinder
    print(sur + 1, 'c/z', xcoord1, thk/2 + w, r2 ) #outer cylinder
    print(sur + 2, 'c/z', xcoord2, thk/2 + w, r1 ) # inner cylinder
    print(sur + 3, 'c/z',xcoord2, thk/2 + w , r2 ) #outer cylinder
    xcoord2 = xcoord2 + distc
    xcoord1 = xcoord1 + distc
    sur = sur + 4
print('c')

print('c level 3 parallel to x cylinders')

print('c')
xcoord1 = xcord1
xcoord2 = xcoord1 + w

sur = 120

while (sur < 136):
    print(sur, 'c/z', xcoord1, thk/2 + w*2, r1 ) # inner cylinder
    print(sur + 1, 'c/z', xcoord1, thk/2 + w*2, r2 ) #outer cylinder
    print(sur + 2, 'c/z', xcoord2, thk/2 + w*2, r1 ) # inner cylinder
    print(sur + 3, 'c/z',xcoord2, thk/2 + w*2, r2 ) #outer cylinder
    xcoord2 = xcoord2 + distc
    xcoord1 = xcoord1 + distc
    sur = sur + 4



'''
End code to generate cylinders parallel to the y and x axes, orthogonal to the z

'''  

'''
Begin code to generate taurus' parallel to the y and x axes

'''   
    
ycoord1 = ycord1
ycoord2 = ycoord1 + w
xcoord1 = xcord1
xcoord2 = xcoord1 + w

print('c')

print('c level 1 parallel to x torus')

print('c')

tl1ay = thk + ( w - thk )/4
tl1by = thk + ( w - thk ) * 3 / 4
sur = 200

while (sur < 208):  
    print(sur + 1, 'TX', thk/2, tl1ay, h2, distt, r1, r1 ) #outer cylinder
    print(sur + 2, 'TX', thk/2, tl1ay, h2, distt, r2, r2 )
    print(sur + 3, 'TX', thk/2, tl1by, h2, distt, r1, r1 ) #outer cylinder
    print(sur + 4, 'TX', thk/2, tl1by, h2, distt, r2, r2 )
    sur = sur + 4
    tl1ay = tl1ay + w
    tl1by = tl1by + w


print('c')

print('c level 2 parallel to x torus')

print('c')

tl2ay = thk + ( w - thk )/4
tl2by = thk + ( w - thk ) * 3 / 4
sur = 210

while (sur < 218):  
    print(sur + 1, 'TX', thk/2+w, tl2ay, h2, distt, r1, r1 ) #outer cylinder
    print(sur + 2, 'TX', thk/2+w, tl2ay, h2, distt, r2, r2 )
    print(sur + 3, 'TX', thk/2+w, tl2by, h2, distt, r1, r1 ) #outer cylinder
    print(sur + 4, 'TX', thk/2+w, tl2by, h2, distt, r2, r2 )
    sur = sur + 4
    tl2ay = tl2ay + w
    tl2by = tl2by + w
    
print('c')
print('c level 3 parallel to x torus')

print('c')

tl3ay = thk + ( w - thk )/4
tl3by = thk + ( w - thk ) * 3 / 4
sur = 220

while (sur < 228):   
    print(sur + 1, 'TX', thk/2+2*w, tl3ay, h2, distt, r1, r1 ) #outer cylinder
    print(sur + 2, 'TX', thk/2+2*w, tl3ay, h2, distt, r2, r2 )
    print(sur + 3, 'TX', thk/2+2*w, tl3by, h2, distt, r1, r1 ) #outer cylinder
    print(sur + 4, 'TX', thk/2+2*w, tl3by, h2, distt, r2, r2 )
    sur = sur + 4
    tl3ay = tl3ay + w
    tl3by = tl3by + w
    
    print('c')

print('c level 1 parallel to y torus')

print('c')

tl1ax = thk + ( w - thk )/4
tl1bx = thk + ( w - thk ) * 3 / 4
sur = 300

while (sur < 308): 
    print(sur + 1, 'TY', tl1ax, thk/2, h2, distt, r1, r1 ) #outer cylinder
    print(sur + 2, 'TY', tl1ax, thk/2, h2, distt, r2, r2 )
    print(sur + 3, 'TY', tl1bx, thk/2, h2, distt, r1, r1 ) #outer cylinder
    print(sur + 4, 'TY', tl1bx, thk/2, h2, distt, r2, r2 )
    sur = sur + 4
    tl1ax = tl1ax + w
    tl1bx = tl1bx + w


print('c')

print('c level 2 parallel to y torus')

print('c')

tl2ax = thk + ( w - thk )/4
tl2bx = thk + ( w - thk ) * 3 / 4
sur = 310

while (sur < 318): 
    print(sur + 1, 'TY', tl2ax, thk/2+w, h2, distt, r1, r1 ) #outer cylinder
    print(sur + 2, 'TY', tl2ax, thk/2+w, h2, distt, r2, r2 )
    print(sur + 3, 'TY', tl2bx, thk/2+w, h2, distt, r1, r1 ) #outer cylinder
    print(sur + 4, 'TY', tl2bx, thk/2+w, h2, distt, r2, r2 )
    sur = sur + 4
    tl2ax = tl2ax + w
    tl2bx = tl2bx + w
    
print('c')
print('c level 3 parallel to y torus')

print('c')

tl3ax = thk + ( w - thk )/4
tl3bx = thk + ( w - thk ) * 3 / 4
sur = 320

while (sur < 328):  
    print(sur + 1, 'TY', tl3ax, thk/2+2*w, h2, distt, r1, r1 ) #outer cylinder
    print(sur + 2, 'TY', tl3ax, thk/2+2*w, h2, distt, r2, r2 )
    print(sur + 3, 'TY', tl3bx, thk/2+2*w, h2, distt, r1, r1 ) #outer cylinder
    print(sur + 4, 'TY', tl3bx, thk/2+2*w, h2, distt, r2, r2 )
    sur = sur + 4
    tl3ax = tl3ax + w
    tl3bx = tl3bx + w
    
print('c')
print('c')
print('c')
sur = 400
print(sur, 'pz', 0-thk)
sur = sur + 1
print(sur, 'pz', 0)
sur = sur + 1
print(sur, 'pz', h2)
sur = sur + 1
print(sur, 'pz', h1)
sur = sur + 1
print(sur, 'pz', h1+thk)