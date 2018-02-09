########################################################################
# R.A.Borrelli
# @TheDoctorRAB
# rev.13.May.2016
########################################################################
#
# This loads radionuclide content data and sorts selection into a column.
#
########################################################################
#
#
#
#######
#
# imports
#
import numpy
###
#
# command line
from sys import argv
script,radionuclide_datafile0,radionuclide_datafile1,radionuclide_datafile2,radionuclide_datafile3,radionuclide_datafile4,radionuclide_datafile5,radionuclide_datafile6,radionuclide_datafile7,radionuclide_datafile8,radionuclide_datafile9,radionuclide_datafile10,radionuclide_datafile11,radionuclide_datafile12,radionuclide_datafile13,radionuclide_datafile14,radionuclide_datafile15,radionuclide_datafile16,radionuclide_datafile17,radionuclide_datafile18,radionuclide_datafile19=argv #add radionuclide_datafileN for each data file to plot
#
########################################################################
#
#
#
#######
#
# open the radionuclide data file(s)
# add radionuclide_dataN for each radionuclide_datafileN
#
radionuclide_data0=numpy.loadtxt(radionuclide_datafile0,dtype=float)
radionuclide_data1=numpy.loadtxt(radionuclide_datafile1,dtype=float)
radionuclide_data2=numpy.loadtxt(radionuclide_datafile2,dtype=float)
radionuclide_data3=numpy.loadtxt(radionuclide_datafile3,dtype=float)
radionuclide_data4=numpy.loadtxt(radionuclide_datafile4,dtype=float)
radionuclide_data5=numpy.loadtxt(radionuclide_datafile5,dtype=float)
radionuclide_data6=numpy.loadtxt(radionuclide_datafile6,dtype=float)
radionuclide_data7=numpy.loadtxt(radionuclide_datafile7,dtype=float)
radionuclide_data8=numpy.loadtxt(radionuclide_datafile8,dtype=float)
radionuclide_data9=numpy.loadtxt(radionuclide_datafile9,dtype=float)
radionuclide_data10=numpy.loadtxt(radionuclide_datafile10,dtype=float)
radionuclide_data11=numpy.loadtxt(radionuclide_datafile11,dtype=float)
radionuclide_data12=numpy.loadtxt(radionuclide_datafile12,dtype=float)
radionuclide_data13=numpy.loadtxt(radionuclide_datafile13,dtype=float)
radionuclide_data14=numpy.loadtxt(radionuclide_datafile14,dtype=float)
radionuclide_data15=numpy.loadtxt(radionuclide_datafile15,dtype=float)
radionuclide_data16=numpy.loadtxt(radionuclide_datafile16,dtype=float)
radionuclide_data17=numpy.loadtxt(radionuclide_datafile17,dtype=float)
radionuclide_data18=numpy.loadtxt(radionuclide_datafile18,dtype=float)
radionuclide_data19=numpy.loadtxt(radionuclide_datafile19,dtype=float)
#
#######
#
# sort
# need to automate later
#
steps=20
radionuclide_content_sort=numpy.zeros((steps))
#
radionuclide_content_sort[0]=radionuclide_data0[40,3]
radionuclide_content_sort[1]=radionuclide_data1[40,3]
radionuclide_content_sort[2]=radionuclide_data2[40,3]
radionuclide_content_sort[3]=radionuclide_data3[40,3]
radionuclide_content_sort[4]=radionuclide_data4[40,3]
radionuclide_content_sort[5]=radionuclide_data5[40,3]
radionuclide_content_sort[6]=radionuclide_data6[40,3]
radionuclide_content_sort[7]=radionuclide_data7[40,3]
radionuclide_content_sort[8]=radionuclide_data8[40,3]
radionuclide_content_sort[9]=radionuclide_data9[40,3]
radionuclide_content_sort[10]=radionuclide_data10[40,3]
radionuclide_content_sort[11]=radionuclide_data11[40,3]
radionuclide_content_sort[12]=radionuclide_data12[40,3]
radionuclide_content_sort[13]=radionuclide_data13[40,3]
radionuclide_content_sort[14]=radionuclide_data14[40,3]
radionuclide_content_sort[15]=radionuclide_data15[40,3]
radionuclide_content_sort[16]=radionuclide_data16[40,3]
radionuclide_content_sort[17]=radionuclide_data17[40,3]
radionuclide_content_sort[18]=radionuclide_data18[40,3]
radionuclide_content_sort[19]=radionuclide_data19[40,3]
#
#######
#
# write file
#
numpy.savetxt('radionuclide.content.sorted.out',radionuclide_content_sort,fmt='%.3e') 
#
########################################################################
#
# EOF
#
########################################################################
