#!/bin/bash
pushd 0wt/
echo
echo $PWD
echo
pushd dat/dose-rate/
python ~/github/plot/src/igem/neutronics/water/bare/borosilicate-glass-backfill/0wt/plot_all.in.one_cask.thickness_dose.rate_t4045_west.py single.assembly_7815_west.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/bare/borosilicate-glass-backfill/0wt/plot_all.in.one_cask.thickness_dose.rate_t4045_east.py single.assembly_7815_east.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/bare/borosilicate-glass-backfill/0wt/plot_all.in.one_cask.thickness_dose.rate_t4045_south.py single.assembly_7815_south.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/bare/borosilicate-glass-backfill/0wt/plot_all.in.one_cask.thickness_dose.rate_t4045_north.py single.assembly_7815_north.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/bare/borosilicate-glass-backfill/0wt/plot_all.in.one_cask.thickness_dose.rate_t4045_cap.py single.assembly_7815_cap_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/bare/borosilicate-glass-backfill/0wt/plot_all.in.one_cask.thickness_dose.rate_t4045_plug.py single.assembly_7815_plug_dose.rate.out
mv *.png ../../plt/
popd
popd
pushd 10wt/
echo
echo $PWD
echo
pushd dat/dose-rate/
python ~/github/plot/src/igem/neutronics/water/bare/borosilicate-glass-backfill/10wt/plot_all.in.one_cask.thickness_dose.rate_t4045_west.py single.assembly_7815_west.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/bare/borosilicate-glass-backfill/10wt/plot_all.in.one_cask.thickness_dose.rate_t4045_east.py single.assembly_7815_east.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/bare/borosilicate-glass-backfill/10wt/plot_all.in.one_cask.thickness_dose.rate_t4045_south.py single.assembly_7815_south.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/bare/borosilicate-glass-backfill/10wt/plot_all.in.one_cask.thickness_dose.rate_t4045_north.py single.assembly_7815_north.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/bare/borosilicate-glass-backfill/10wt/plot_all.in.one_cask.thickness_dose.rate_t4045_cap.py single.assembly_7815_cap_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/bare/borosilicate-glass-backfill/10wt/plot_all.in.one_cask.thickness_dose.rate_t4045_plug.py single.assembly_7815_plug_dose.rate.out
mv *.png ../../plt/
popd
popd
pushd 25wt/
echo
echo $PWD
echo
pushd dat/dose-rate/
python ~/github/plot/src/igem/neutronics/water/bare/borosilicate-glass-backfill/25wt/plot_all.in.one_cask.thickness_dose.rate_t4045_west.py single.assembly_7815_west.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/bare/borosilicate-glass-backfill/25wt/plot_all.in.one_cask.thickness_dose.rate_t4045_east.py single.assembly_7815_east.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/bare/borosilicate-glass-backfill/25wt/plot_all.in.one_cask.thickness_dose.rate_t4045_south.py single.assembly_7815_south.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/bare/borosilicate-glass-backfill/25wt/plot_all.in.one_cask.thickness_dose.rate_t4045_north.py single.assembly_7815_north.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/bare/borosilicate-glass-backfill/25wt/plot_all.in.one_cask.thickness_dose.rate_t4045_cap.py single.assembly_7815_cap_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/bare/borosilicate-glass-backfill/25wt/plot_all.in.one_cask.thickness_dose.rate_t4045_plug.py single.assembly_7815_plug_dose.rate.out
mv *.png ../../plt/
popd
popd
pushd 50wt/
echo
echo $PWD
echo
pushd dat/dose-rate/
python ~/github/plot/src/igem/neutronics/water/bare/borosilicate-glass-backfill/50wt/plot_all.in.one_cask.thickness_dose.rate_t4045_west.py single.assembly_7815_west.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/bare/borosilicate-glass-backfill/50wt/plot_all.in.one_cask.thickness_dose.rate_t4045_east.py single.assembly_7815_east.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/bare/borosilicate-glass-backfill/50wt/plot_all.in.one_cask.thickness_dose.rate_t4045_south.py single.assembly_7815_south.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/bare/borosilicate-glass-backfill/50wt/plot_all.in.one_cask.thickness_dose.rate_t4045_north.py single.assembly_7815_north.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/bare/borosilicate-glass-backfill/50wt/plot_all.in.one_cask.thickness_dose.rate_t4045_cap.py single.assembly_7815_cap_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/bare/borosilicate-glass-backfill/50wt/plot_all.in.one_cask.thickness_dose.rate_t4045_plug.py single.assembly_7815_plug_dose.rate.out
mv *.png ../../plt/
popd
popd
pushd 5wt/
echo
echo $PWD
echo
pushd dat/dose-rate/
python ~/github/plot/src/igem/neutronics/water/bare/borosilicate-glass-backfill/5wt/plot_all.in.one_cask.thickness_dose.rate_t4045_west.py single.assembly_7815_west.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/bare/borosilicate-glass-backfill/5wt/plot_all.in.one_cask.thickness_dose.rate_t4045_east.py single.assembly_7815_east.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/bare/borosilicate-glass-backfill/5wt/plot_all.in.one_cask.thickness_dose.rate_t4045_south.py single.assembly_7815_south.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/bare/borosilicate-glass-backfill/5wt/plot_all.in.one_cask.thickness_dose.rate_t4045_north.py single.assembly_7815_north.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/bare/borosilicate-glass-backfill/5wt/plot_all.in.one_cask.thickness_dose.rate_t4045_cap.py single.assembly_7815_cap_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/bare/borosilicate-glass-backfill/5wt/plot_all.in.one_cask.thickness_dose.rate_t4045_plug.py single.assembly_7815_plug_dose.rate.out
mv *.png ../../plt/
popd
popd
pushd 75wt/
echo
echo $PWD
echo
pushd dat/dose-rate/
python ~/github/plot/src/igem/neutronics/water/bare/borosilicate-glass-backfill/75wt/plot_all.in.one_cask.thickness_dose.rate_t4045_west.py single.assembly_7815_west.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/bare/borosilicate-glass-backfill/75wt/plot_all.in.one_cask.thickness_dose.rate_t4045_east.py single.assembly_7815_east.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/bare/borosilicate-glass-backfill/75wt/plot_all.in.one_cask.thickness_dose.rate_t4045_south.py single.assembly_7815_south.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/bare/borosilicate-glass-backfill/75wt/plot_all.in.one_cask.thickness_dose.rate_t4045_north.py single.assembly_7815_north.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/bare/borosilicate-glass-backfill/75wt/plot_all.in.one_cask.thickness_dose.rate_t4045_cap.py single.assembly_7815_cap_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/bare/borosilicate-glass-backfill/75wt/plot_all.in.one_cask.thickness_dose.rate_t4045_plug.py single.assembly_7815_plug_dose.rate.out
mv *.png ../../plt/
popd
popd
