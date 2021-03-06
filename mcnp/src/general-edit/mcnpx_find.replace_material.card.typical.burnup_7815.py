#######
# @TheDoctorRAB
#######
#
# edits a given set of lines in the input file
# number of spaces is important because MCNP is FORTRAN
# probably not the most elegant
#
#######
#
# imports
#
from sys import argv
script,mcnp_input=argv
#
#######
#
# set the lines to be edited
#
new_lines1='''M2     1003.70c      -2.258600e-08
       2003.70c      -4.727100e-08
       2004.70c      -3.865600e-06
       92234.70c     -1.685300e-04
       92235.70c     -8.311500e-03
       92236.70c     -5.415200e-03
       92238.70c     -9.270600e-01
       93237.70c     -6.576200e-04
       94238.70c     -2.280400e-04
       94239.70c     -6.058200e-03
       94240.70c     -2.356300e-03
       94241.70c     -7.382500e-04
       94242.70c     -8.092700e-04
       94244.70c     -9.103400e-08
       95241.70c     -1.208700e-03
       95242.70c     -3.713700e-07
       95243.70c     -1.806800e-04
       96243.70c     -2.841000e-07
       96244.70c     -3.590200e-05
       96245.70c     -4.919300e-06
       96246.70c     -5.554400e-07
       32072.70c     -1.157400e-08
       32073.70c     -2.721800e-08
       32074.70c     -7.119700e-08
       33075.70c     -1.696000e-07
       32076.70c     -4.528500e-07
       34077.70c     -1.058400e-06
       34078.70c     -3.093700e-06
       34079.70c     -6.502600e-06
       34080.70c     -1.713300e-05
       35081.70c     -2.815800e-05
       34082.70c     -4.492700e-05
       36082.70c     -1.087000e-06
       36083.70c     -5.294800e-05
       36084.70c     -1.494900e-04
       36085.70c     -9.550400e-06
       37085.70c     -1.563100e-04
       36086.70c     -2.480700e-04
       38086.70c     -7.248000e-07
       37087.70c     -3.260500e-04
       38088.70c     -4.534900e-04
       39089.70c     -6.050100e-04
       38090.70c     -4.520900e-04
       39090.70c     -1.146800e-07
       40090.70c     -2.942700e-04
       40091.70c     -7.911600e-04
       40092.70c     -8.634100e-04
       40093.70c     -9.534200e-04
       40094.70c     -1.029300e-03
       42094.70c     -1.070100e-08
       42095.70c     -1.025700e-03
       40096.70c     -1.091500e-03
       42096.70c     -4.801300e-05
       42097.70c     -1.086300e-03
       42098.70c     -1.127800e-03
       43099.70c     -1.061700e-03
       44099.70c     -1.082700e-07
       42100.70c     -1.275600e-03
       44100.70c     -1.548600e-04
       44101.70c     -1.050900e-03
       44102.70c     -1.107000e-03
       45103.70c     -6.594300e-04
       44104.70c     -7.753300e-04
       46104.70c     -3.048400e-04
       46105.70c     -4.969800e-04
       46106.70c     -5.769000e-04
       46107.70c     -3.097000e-04
       46108.70c     -2.062700e-04
       47109.70c     -1.069600e-04
       46110.70c     -6.883300e-05
       48110.70c     -5.607300e-05
       48111.70c     -3.406800e-05
       48112.70c     -1.762900e-05
       48113.70c     -1.542700e-07
       48114.70c     -2.037300e-05
       49115.70c     -2.263800e-06
       50115.70c     -3.279000e-07
       48116.70c     -7.508100e-06
       50116.70c     -4.859300e-06
       50117.70c     -6.821800e-06
       50118.70c     -6.378600e-06
       50119.70c     -6.286800e-06
       50120.70c     -6.359300e-06
       50121.70c     -3.637500e-07
       51121.70c     -6.107900e-06
       50122.70c     -8.089400e-06
       52122.70c     -5.420600e-07
       51123.70c     -7.902200e-06
       50124.70c     -1.280500e-05
       52124.70c     -4.287000e-07
       51125.70c     -9.658900e-08
       52125.70c     -1.695300e-05
       50126.70c     -2.791700e-05
       52126.70c     -7.215600e-07
       53127.70c     -5.853900e-05
       52128.70c     -1.301000e-04
       54128.70c     -4.290500e-06
       53129.70c     -2.121200e-04
       54129.70c     -3.310600e-08
       52130.70c     -5.141700e-04
       54130.70c     -9.529400e-06
       54131.70c     -5.539900e-04
       54132.70c     -1.530900e-03
       55133.70c     -1.491900e-03
       54134.70c     -2.075800e-03
       55134.70c     -2.787700e-07
       56134.70c     -2.646700e-04
       55135.70c     -2.882600e-04
       56135.70c     -2.955700e-07
       54136.70c     -3.384200e-03
       56136.70c     -1.983900e-05
       55137.70c     -1.066300e-03
       56137.70c     -6.518600e-04
       56138.70c     -1.769600e-03
       57138.70c     -2.083000e-08
       57139.70c     -1.654800e-03
       58140.70c     -1.728700e-03
       59141.70c     -1.501100e-03
       58142.70c     -1.541200e-03
       60142.70c     -2.847500e-05
       60143.70c     -1.053000e-03
       60144.70c     -1.817700e-03
       60145.70c     -8.916900e-04
       60146.70c     -9.637200e-04
       61147.70c     -1.335400e-06
       62147.70c     -3.056300e-04
       60148.70c     -5.189600e-04
       62148.70c     -1.740500e-04
       62149.70c     -6.677600e-06
       60150.70c     -2.438800e-04
       62150.70c     -4.486400e-04
       62151.70c     -1.374600e-05
       63151.70c     -2.294300e-06
       62152.70c     -1.305500e-04
       64152.70c     -1.375700e-08
       63153.70c     -1.587100e-04
       62154.70c     -5.704500e-05
       63154.70c     -7.709800e-06
       64154.70c     -3.235900e-05
       63155.70c     -6.396700e-07
       64155.70c     -1.120000e-05
       64156.70c     -1.330000e-04
       64157.70c     -2.576900e-07
       64158.70c     -3.067300e-05
       65159.70c     -3.576900e-06
       64160.70c     -1.538300e-06
       66160.70c     -3.917200e-07
       66161.70c     -5.154000e-07
       66162.70c     -3.704800e-07
       66163.70c     -3.087100e-07
       66164.70c     -7.612700e-08
       67165.70c     -1.335200e-07
       68166.70c     -4.313400e-08'''
#
# new_lines2='SP1    1 1319R'
#
###
#
old_lines1='M2     2004.70c      -2.192800e-06'
#
# old_lines2='SP1    1 1444R'
#
#######
#
# open the mcnp deck and read
# this is ok because the input files for mcnp are small for memory
#
mcnp_tempfile=open(mcnp_input,'r').read()
#
#######
#
# replace
#
mcnp_tempfile=mcnp_tempfile.replace(old_lines1,new_lines1)
# mcnp_tempfile=mcnp_tempfile.replace(old_lines2,new_lines2)
#
#######
#
# write the file
#
open(mcnp_input,'w').write(mcnp_tempfile)
#
#######
#
# EOF
#
#######
