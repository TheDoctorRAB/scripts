#!/bin/bash
pushd 0wt/
echo
echo $PWD
echo
pushd dat/dose-rate/
python ~/github/plot/src/igem/neutronics/water/container/water-backfill/15cm/0wt/plot_all.in.one_cask.thickness_dose.rate_h5060_bottom.py single.assembly_7815_container.bottom_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/container/water-backfill/15cm/0wt/plot_all.in.one_cask.thickness_dose.rate_h5060_surface.py single.assembly_7815_container.surface_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/container/water-backfill/15cm/0wt/plot_all.in.one_cask.thickness_dose.rate_h5060_top.py single.assembly_7815_container.top_dose.rate.out
mv *.png ../../plt/
popd
popd
pushd 10wt/
echo
echo $PWD
echo
pushd dat/dose-rate/
python ~/github/plot/src/igem/neutronics/water/container/water-backfill/15cm/10wt/plot_all.in.one_cask.thickness_dose.rate_h5060_bottom.py single.assembly_7815_container.bottom_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/container/water-backfill/15cm/10wt/plot_all.in.one_cask.thickness_dose.rate_h5060_surface.py single.assembly_7815_container.surface_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/container/water-backfill/15cm/10wt/plot_all.in.one_cask.thickness_dose.rate_h5060_top.py single.assembly_7815_container.top_dose.rate.out
mv *.png ../../plt/
popd
popd
pushd 25wt/
echo
echo $PWD
echo
pushd dat/dose-rate/
python ~/github/plot/src/igem/neutronics/water/container/water-backfill/15cm/25wt/plot_all.in.one_cask.thickness_dose.rate_h5060_bottom.py single.assembly_7815_container.bottom_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/container/water-backfill/15cm/25wt/plot_all.in.one_cask.thickness_dose.rate_h5060_surface.py single.assembly_7815_container.surface_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/container/water-backfill/15cm/25wt/plot_all.in.one_cask.thickness_dose.rate_h5060_top.py single.assembly_7815_container.top_dose.rate.out
mv *.png ../../plt/
popd
popd
pushd 50wt/
echo
echo $PWD
echo
pushd dat/dose-rate/
python ~/github/plot/src/igem/neutronics/water/container/water-backfill/15cm/50wt/plot_all.in.one_cask.thickness_dose.rate_h5060_bottom.py single.assembly_7815_container.bottom_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/container/water-backfill/15cm/50wt/plot_all.in.one_cask.thickness_dose.rate_h5060_surface.py single.assembly_7815_container.surface_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/container/water-backfill/15cm/50wt/plot_all.in.one_cask.thickness_dose.rate_h5060_top.py single.assembly_7815_container.top_dose.rate.out
mv *.png ../../plt/
popd
popd
pushd 5wt/
echo
echo $PWD
echo
pushd dat/dose-rate/
python ~/github/plot/src/igem/neutronics/water/container/water-backfill/15cm/5wt/plot_all.in.one_cask.thickness_dose.rate_h5060_bottom.py single.assembly_7815_container.bottom_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/container/water-backfill/15cm/5wt/plot_all.in.one_cask.thickness_dose.rate_h5060_surface.py single.assembly_7815_container.surface_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/container/water-backfill/15cm/5wt/plot_all.in.one_cask.thickness_dose.rate_h5060_top.py single.assembly_7815_container.top_dose.rate.out
mv *.png ../../plt/
popd
popd
pushd 75wt/
echo
echo $PWD
echo
pushd dat/dose-rate/
python ~/github/plot/src/igem/neutronics/water/container/water-backfill/15cm/75wt/plot_all.in.one_cask.thickness_dose.rate_h5060_bottom.py single.assembly_7815_container.bottom_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/container/water-backfill/15cm/75wt/plot_all.in.one_cask.thickness_dose.rate_h5060_surface.py single.assembly_7815_container.surface_dose.rate.out
python ~/github/plot/src/igem/neutronics/water/container/water-backfill/15cm/75wt/plot_all.in.one_cask.thickness_dose.rate_h5060_top.py single.assembly_7815_container.top_dose.rate.out
mv *.png ../../plt/
popd
popd
