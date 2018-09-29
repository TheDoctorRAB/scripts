#!/bin/bash
python mcnpx_insert.column.py burnup.content.out insert.column_th.content.inp
python mcnpx_insert.column.py burnup.content_interpolated.out insert.column_th.content.inp
python mcnpx_insert.column.py burnup.content_lower.out insert.column_th.content.inp
python mcnpx_insert.column.py burnup.content_upper.out insert.column_th.content.inp
