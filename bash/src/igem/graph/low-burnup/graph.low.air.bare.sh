#!/bin/bash
pushd 0wt/
echo
echo $PWD
echo
pushd dat/dose-rate/
python ~/github/plot/src/igem/neutronics/air/bare/air-backfill/0wt/plot_all.in.one_cask.thickness_dose.rate_l3030_west.py single.assembly_7815_west.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/air/bare/air-backfill/0wt/plot_all.in.one_cask.thickness_dose.rate_l3030_east.py single.assembly_7815_east.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/air/bare/air-backfill/0wt/plot_all.in.one_cask.thickness_dose.rate_l3030_south.py single.assembly_7815_south.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/air/bare/air-backfill/0wt/plot_all.in.one_cask.thickness_dose.rate_l3030_north.py single.assembly_7815_north.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/air/bare/air-backfill/0wt/plot_all.in.one_cask.thickness_dose.rate_l3030_cap.py single.assembly_7815_cap_dose.rate.out
python ~/github/plot/src/igem/neutronics/air/bare/air-backfill/0wt/plot_all.in.one_cask.thickness_dose.rate_l3030_plug.py single.assembly_7815_plug_dose.rate.out
mv *.png ../../plt/
popd
popd
pushd 10wt/
echo
echo $PWD
echo
pushd dat/dose-rate/
python ~/github/plot/src/igem/neutronics/air/bare/air-backfill/10wt/plot_all.in.one_cask.thickness_dose.rate_l3030_west.py single.assembly_7815_west.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/air/bare/air-backfill/10wt/plot_all.in.one_cask.thickness_dose.rate_l3030_east.py single.assembly_7815_east.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/air/bare/air-backfill/10wt/plot_all.in.one_cask.thickness_dose.rate_l3030_south.py single.assembly_7815_south.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/air/bare/air-backfill/10wt/plot_all.in.one_cask.thickness_dose.rate_l3030_north.py single.assembly_7815_north.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/air/bare/air-backfill/10wt/plot_all.in.one_cask.thickness_dose.rate_l3030_cap.py single.assembly_7815_cap_dose.rate.out
python ~/github/plot/src/igem/neutronics/air/bare/air-backfill/10wt/plot_all.in.one_cask.thickness_dose.rate_l3030_plug.py single.assembly_7815_plug_dose.rate.out
mv *.png ../../plt/
popd
popd
pushd 25wt/
echo
echo $PWD
echo
pushd dat/dose-rate/
python ~/github/plot/src/igem/neutronics/air/bare/air-backfill/25wt/plot_all.in.one_cask.thickness_dose.rate_l3030_west.py single.assembly_7815_west.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/air/bare/air-backfill/25wt/plot_all.in.one_cask.thickness_dose.rate_l3030_east.py single.assembly_7815_east.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/air/bare/air-backfill/25wt/plot_all.in.one_cask.thickness_dose.rate_l3030_south.py single.assembly_7815_south.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/air/bare/air-backfill/25wt/plot_all.in.one_cask.thickness_dose.rate_l3030_north.py single.assembly_7815_north.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/air/bare/air-backfill/25wt/plot_all.in.one_cask.thickness_dose.rate_l3030_cap.py single.assembly_7815_cap_dose.rate.out
python ~/github/plot/src/igem/neutronics/air/bare/air-backfill/25wt/plot_all.in.one_cask.thickness_dose.rate_l3030_plug.py single.assembly_7815_plug_dose.rate.out
mv *.png ../../plt/
popd
popd
pushd 50wt/
echo
echo $PWD
echo
pushd dat/dose-rate/
python ~/github/plot/src/igem/neutronics/air/bare/air-backfill/50wt/plot_all.in.one_cask.thickness_dose.rate_l3030_west.py single.assembly_7815_west.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/air/bare/air-backfill/50wt/plot_all.in.one_cask.thickness_dose.rate_l3030_east.py single.assembly_7815_east.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/air/bare/air-backfill/50wt/plot_all.in.one_cask.thickness_dose.rate_l3030_south.py single.assembly_7815_south.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/air/bare/air-backfill/50wt/plot_all.in.one_cask.thickness_dose.rate_l3030_north.py single.assembly_7815_north.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/air/bare/air-backfill/50wt/plot_all.in.one_cask.thickness_dose.rate_l3030_cap.py single.assembly_7815_cap_dose.rate.out
python ~/github/plot/src/igem/neutronics/air/bare/air-backfill/50wt/plot_all.in.one_cask.thickness_dose.rate_l3030_plug.py single.assembly_7815_plug_dose.rate.out
mv *.png ../../plt/
popd
popd
pushd 5wt/
echo
echo $PWD
echo
pushd dat/dose-rate/
python ~/github/plot/src/igem/neutronics/air/bare/air-backfill/5wt/plot_all.in.one_cask.thickness_dose.rate_l3030_west.py single.assembly_7815_west.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/air/bare/air-backfill/5wt/plot_all.in.one_cask.thickness_dose.rate_l3030_east.py single.assembly_7815_east.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/air/bare/air-backfill/5wt/plot_all.in.one_cask.thickness_dose.rate_l3030_south.py single.assembly_7815_south.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/air/bare/air-backfill/5wt/plot_all.in.one_cask.thickness_dose.rate_l3030_north.py single.assembly_7815_north.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/air/bare/air-backfill/5wt/plot_all.in.one_cask.thickness_dose.rate_l3030_cap.py single.assembly_7815_cap_dose.rate.out
python ~/github/plot/src/igem/neutronics/air/bare/air-backfill/5wt/plot_all.in.one_cask.thickness_dose.rate_l3030_plug.py single.assembly_7815_plug_dose.rate.out
mv *.png ../../plt/
popd
popd
pushd 75wt/
echo
echo $PWD
echo
pushd dat/dose-rate/
python ~/github/plot/src/igem/neutronics/air/bare/air-backfill/75wt/plot_all.in.one_cask.thickness_dose.rate_l3030_west.py single.assembly_7815_west.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/air/bare/air-backfill/75wt/plot_all.in.one_cask.thickness_dose.rate_l3030_east.py single.assembly_7815_east.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/air/bare/air-backfill/75wt/plot_all.in.one_cask.thickness_dose.rate_l3030_south.py single.assembly_7815_south.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/air/bare/air-backfill/75wt/plot_all.in.one_cask.thickness_dose.rate_l3030_north.py single.assembly_7815_north.plate_dose.rate.out
python ~/github/plot/src/igem/neutronics/air/bare/air-backfill/75wt/plot_all.in.one_cask.thickness_dose.rate_l3030_cap.py single.assembly_7815_cap_dose.rate.out
python ~/github/plot/src/igem/neutronics/air/bare/air-backfill/75wt/plot_all.in.one_cask.thickness_dose.rate_l3030_plug.py single.assembly_7815_plug_dose.rate.out
mv *.png ../../plt/
popd
popd
