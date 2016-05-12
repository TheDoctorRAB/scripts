#!/bin/bash
mv insert.column_th.content.inp 92233/
mv mcnpx_insert.column.py 92233/
cd 92233
python mcnpx_insert.column.py 92233.mass_interpolated.out insert.column_th.content.inp
mv mcnpx_insert.column.py insert.column_th.content.inp ../94238/
cd ../94238
python mcnpx_insert.column.py 94238.mass_interpolated.out insert.column_th.content.inp
mv mcnpx_insert.column.py insert.column_th.content.inp ../94239/
cd ../94239
python mcnpx_insert.column.py 94239.mass_interpolated.out insert.column_th.content.inp
mv mcnpx_insert.column.py insert.column_th.content.inp ../94240/
cd ../94240
python mcnpx_insert.column.py 94240.mass_interpolated.out insert.column_th.content.inp
mv mcnpx_insert.column.py insert.column_th.content.inp ../94242/
cd ../94242
python mcnpx_insert.column.py 94242.mass_interpolated.out insert.column_th.content.inp
rm mcnpx_insert.column.py insert.column_th.content.inp
