#!/bin/bash
pushd 0wt/
echo
echo $PWD
echo
pushd dat/raw
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally_cylinder.py ../../10wt/1.5cm/out/single.assembly_7815.inp.o ../../30wt/1.5cm/out/single.assembly_7815.inp.o ../../50wt/1.5cm/out/single.assembly_7815.inp.o ../../70wt/1.5cm/out/single.assembly_7815.inp.o ../../90wt/1.5cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally_cylinder.py ../../10wt/3cm/out/single.assembly_7815.inp.o ../../30wt/3cm/out/single.assembly_7815.inp.o ../../50wt/3cm/out/single.assembly_7815.inp.o ../../70wt/3cm/out/single.assembly_7815.inp.o ../../90wt/3cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally_cylinder.py ../../10wt/6cm/out/single.assembly_7815.inp.o ../../30wt/6cm/out/single.assembly_7815.inp.o ../../50wt/6cm/out/single.assembly_7815.inp.o ../../70wt/6cm/out/single.assembly_7815.inp.o ../../90wt/6cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally_cylinder.py ../../10wt/12cm/out/single.assembly_7815.inp.o ../../30wt/12cm/out/single.assembly_7815.inp.o ../../50wt/12cm/out/single.assembly_7815.inp.o ../../70wt/12cm/out/single.assembly_7815.inp.o ../../90wt/12cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally_cylinder.py ../../10wt/18cm/out/single.assembly_7815.inp.o ../../30wt/18cm/out/single.assembly_7815.inp.o ../../50wt/18cm/out/single.assembly_7815.inp.o ../../70wt/18cm/out/single.assembly_7815.inp.o ../../90wt/18cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally_cylinder.py ../../10wt/30cm/out/single.assembly_7815.inp.o ../../30wt/30cm/out/single.assembly_7815.inp.o ../../50wt/30cm/out/single.assembly_7815.inp.o ../../70wt/30cm/out/single.assembly_7815.inp.o ../../90wt/30cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/output/mcnp_compute.dose.py single.assembly_7815_container.surface.out
python ~/github/scripts/mcnp/src/output/mcnp_compute.dose.py single.assembly_7815_container.top.out
python ~/github/scripts/mcnp/src/output/mcnp_compute.dose.py single.assembly_7815_container.bottom.out
mv *dose* ../dose-rate
popd
popd
pushd 10wt/
echo
echo $PWD
echo
pushd dat/raw
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally_cylinder.py ../../10wt/1.5cm/out/single.assembly_7815.inp.o ../../30wt/1.5cm/out/single.assembly_7815.inp.o ../../50wt/1.5cm/out/single.assembly_7815.inp.o ../../70wt/1.5cm/out/single.assembly_7815.inp.o ../../90wt/1.5cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally_cylinder.py ../../10wt/3cm/out/single.assembly_7815.inp.o ../../30wt/3cm/out/single.assembly_7815.inp.o ../../50wt/3cm/out/single.assembly_7815.inp.o ../../70wt/3cm/out/single.assembly_7815.inp.o ../../90wt/3cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally_cylinder.py ../../10wt/6cm/out/single.assembly_7815.inp.o ../../30wt/6cm/out/single.assembly_7815.inp.o ../../50wt/6cm/out/single.assembly_7815.inp.o ../../70wt/6cm/out/single.assembly_7815.inp.o ../../90wt/6cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally_cylinder.py ../../10wt/12cm/out/single.assembly_7815.inp.o ../../30wt/12cm/out/single.assembly_7815.inp.o ../../50wt/12cm/out/single.assembly_7815.inp.o ../../70wt/12cm/out/single.assembly_7815.inp.o ../../90wt/12cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally_cylinder.py ../../10wt/18cm/out/single.assembly_7815.inp.o ../../30wt/18cm/out/single.assembly_7815.inp.o ../../50wt/18cm/out/single.assembly_7815.inp.o ../../70wt/18cm/out/single.assembly_7815.inp.o ../../90wt/18cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally_cylinder.py ../../10wt/30cm/out/single.assembly_7815.inp.o ../../30wt/30cm/out/single.assembly_7815.inp.o ../../50wt/30cm/out/single.assembly_7815.inp.o ../../70wt/30cm/out/single.assembly_7815.inp.o ../../90wt/30cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/output/mcnp_compute.dose.py single.assembly_7815_container.surface.out
python ~/github/scripts/mcnp/src/output/mcnp_compute.dose.py single.assembly_7815_container.top.out
python ~/github/scripts/mcnp/src/output/mcnp_compute.dose.py single.assembly_7815_container.bottom.out
mv *dose* ../dose-rate
popd
popd
pushd 25wt/
echo
echo $PWD
echo
pushd dat/raw
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally_cylinder.py ../../10wt/1.5cm/out/single.assembly_7815.inp.o ../../30wt/1.5cm/out/single.assembly_7815.inp.o ../../50wt/1.5cm/out/single.assembly_7815.inp.o ../../70wt/1.5cm/out/single.assembly_7815.inp.o ../../90wt/1.5cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally_cylinder.py ../../10wt/3cm/out/single.assembly_7815.inp.o ../../30wt/3cm/out/single.assembly_7815.inp.o ../../50wt/3cm/out/single.assembly_7815.inp.o ../../70wt/3cm/out/single.assembly_7815.inp.o ../../90wt/3cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally_cylinder.py ../../10wt/6cm/out/single.assembly_7815.inp.o ../../30wt/6cm/out/single.assembly_7815.inp.o ../../50wt/6cm/out/single.assembly_7815.inp.o ../../70wt/6cm/out/single.assembly_7815.inp.o ../../90wt/6cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally_cylinder.py ../../10wt/12cm/out/single.assembly_7815.inp.o ../../30wt/12cm/out/single.assembly_7815.inp.o ../../50wt/12cm/out/single.assembly_7815.inp.o ../../70wt/12cm/out/single.assembly_7815.inp.o ../../90wt/12cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally_cylinder.py ../../10wt/18cm/out/single.assembly_7815.inp.o ../../30wt/18cm/out/single.assembly_7815.inp.o ../../50wt/18cm/out/single.assembly_7815.inp.o ../../70wt/18cm/out/single.assembly_7815.inp.o ../../90wt/18cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally_cylinder.py ../../10wt/30cm/out/single.assembly_7815.inp.o ../../30wt/30cm/out/single.assembly_7815.inp.o ../../50wt/30cm/out/single.assembly_7815.inp.o ../../70wt/30cm/out/single.assembly_7815.inp.o ../../90wt/30cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/output/mcnp_compute.dose.py single.assembly_7815_container.surface.out
python ~/github/scripts/mcnp/src/output/mcnp_compute.dose.py single.assembly_7815_container.top.out
python ~/github/scripts/mcnp/src/output/mcnp_compute.dose.py single.assembly_7815_container.bottom.out
mv *dose* ../dose-rate
popd
popd
pushd 50wt/
echo
echo $PWD
echo
pushd dat/raw
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally_cylinder.py ../../10wt/1.5cm/out/single.assembly_7815.inp.o ../../30wt/1.5cm/out/single.assembly_7815.inp.o ../../50wt/1.5cm/out/single.assembly_7815.inp.o ../../70wt/1.5cm/out/single.assembly_7815.inp.o ../../90wt/1.5cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally_cylinder.py ../../10wt/3cm/out/single.assembly_7815.inp.o ../../30wt/3cm/out/single.assembly_7815.inp.o ../../50wt/3cm/out/single.assembly_7815.inp.o ../../70wt/3cm/out/single.assembly_7815.inp.o ../../90wt/3cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally_cylinder.py ../../10wt/6cm/out/single.assembly_7815.inp.o ../../30wt/6cm/out/single.assembly_7815.inp.o ../../50wt/6cm/out/single.assembly_7815.inp.o ../../70wt/6cm/out/single.assembly_7815.inp.o ../../90wt/6cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally_cylinder.py ../../10wt/12cm/out/single.assembly_7815.inp.o ../../30wt/12cm/out/single.assembly_7815.inp.o ../../50wt/12cm/out/single.assembly_7815.inp.o ../../70wt/12cm/out/single.assembly_7815.inp.o ../../90wt/12cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally_cylinder.py ../../10wt/18cm/out/single.assembly_7815.inp.o ../../30wt/18cm/out/single.assembly_7815.inp.o ../../50wt/18cm/out/single.assembly_7815.inp.o ../../70wt/18cm/out/single.assembly_7815.inp.o ../../90wt/18cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally_cylinder.py ../../10wt/30cm/out/single.assembly_7815.inp.o ../../30wt/30cm/out/single.assembly_7815.inp.o ../../50wt/30cm/out/single.assembly_7815.inp.o ../../70wt/30cm/out/single.assembly_7815.inp.o ../../90wt/30cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/output/mcnp_compute.dose.py single.assembly_7815_container.surface.out
python ~/github/scripts/mcnp/src/output/mcnp_compute.dose.py single.assembly_7815_container.top.out
python ~/github/scripts/mcnp/src/output/mcnp_compute.dose.py single.assembly_7815_container.bottom.out
mv *dose* ../dose-rate
popd
popd
pushd 5wt/
echo
echo $PWD
echo
pushd dat/raw
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally_cylinder.py ../../10wt/1.5cm/out/single.assembly_7815.inp.o ../../30wt/1.5cm/out/single.assembly_7815.inp.o ../../50wt/1.5cm/out/single.assembly_7815.inp.o ../../70wt/1.5cm/out/single.assembly_7815.inp.o ../../90wt/1.5cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally_cylinder.py ../../10wt/3cm/out/single.assembly_7815.inp.o ../../30wt/3cm/out/single.assembly_7815.inp.o ../../50wt/3cm/out/single.assembly_7815.inp.o ../../70wt/3cm/out/single.assembly_7815.inp.o ../../90wt/3cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally_cylinder.py ../../10wt/6cm/out/single.assembly_7815.inp.o ../../30wt/6cm/out/single.assembly_7815.inp.o ../../50wt/6cm/out/single.assembly_7815.inp.o ../../70wt/6cm/out/single.assembly_7815.inp.o ../../90wt/6cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally_cylinder.py ../../10wt/12cm/out/single.assembly_7815.inp.o ../../30wt/12cm/out/single.assembly_7815.inp.o ../../50wt/12cm/out/single.assembly_7815.inp.o ../../70wt/12cm/out/single.assembly_7815.inp.o ../../90wt/12cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally_cylinder.py ../../10wt/18cm/out/single.assembly_7815.inp.o ../../30wt/18cm/out/single.assembly_7815.inp.o ../../50wt/18cm/out/single.assembly_7815.inp.o ../../70wt/18cm/out/single.assembly_7815.inp.o ../../90wt/18cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally_cylinder.py ../../10wt/30cm/out/single.assembly_7815.inp.o ../../30wt/30cm/out/single.assembly_7815.inp.o ../../50wt/30cm/out/single.assembly_7815.inp.o ../../70wt/30cm/out/single.assembly_7815.inp.o ../../90wt/30cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/output/mcnp_compute.dose.py single.assembly_7815_container.surface.out
python ~/github/scripts/mcnp/src/output/mcnp_compute.dose.py single.assembly_7815_container.top.out
python ~/github/scripts/mcnp/src/output/mcnp_compute.dose.py single.assembly_7815_container.bottom.out
mv *dose* ../dose-rate
popd
popd
pushd 75wt/
echo
echo $PWD
echo
pushd dat/raw
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally_cylinder.py ../../10wt/1.5cm/out/single.assembly_7815.inp.o ../../30wt/1.5cm/out/single.assembly_7815.inp.o ../../50wt/1.5cm/out/single.assembly_7815.inp.o ../../70wt/1.5cm/out/single.assembly_7815.inp.o ../../90wt/1.5cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally_cylinder.py ../../10wt/3cm/out/single.assembly_7815.inp.o ../../30wt/3cm/out/single.assembly_7815.inp.o ../../50wt/3cm/out/single.assembly_7815.inp.o ../../70wt/3cm/out/single.assembly_7815.inp.o ../../90wt/3cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally_cylinder.py ../../10wt/6cm/out/single.assembly_7815.inp.o ../../30wt/6cm/out/single.assembly_7815.inp.o ../../50wt/6cm/out/single.assembly_7815.inp.o ../../70wt/6cm/out/single.assembly_7815.inp.o ../../90wt/6cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally_cylinder.py ../../10wt/12cm/out/single.assembly_7815.inp.o ../../30wt/12cm/out/single.assembly_7815.inp.o ../../50wt/12cm/out/single.assembly_7815.inp.o ../../70wt/12cm/out/single.assembly_7815.inp.o ../../90wt/12cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally_cylinder.py ../../10wt/18cm/out/single.assembly_7815.inp.o ../../30wt/18cm/out/single.assembly_7815.inp.o ../../50wt/18cm/out/single.assembly_7815.inp.o ../../70wt/18cm/out/single.assembly_7815.inp.o ../../90wt/18cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally_cylinder.py ../../10wt/30cm/out/single.assembly_7815.inp.o ../../30wt/30cm/out/single.assembly_7815.inp.o ../../50wt/30cm/out/single.assembly_7815.inp.o ../../70wt/30cm/out/single.assembly_7815.inp.o ../../90wt/30cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/output/mcnp_compute.dose.py single.assembly_7815_container.surface.out
python ~/github/scripts/mcnp/src/output/mcnp_compute.dose.py single.assembly_7815_container.top.out
python ~/github/scripts/mcnp/src/output/mcnp_compute.dose.py single.assembly_7815_container.bottom.out
mv *dose* ../dose-rate
popd
popd
