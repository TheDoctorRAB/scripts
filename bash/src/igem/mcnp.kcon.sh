#!/bin/bash
pushd 0wt/10wt/1.5cm/out/
echo
echo $PWD
echo
python ~/github/scripts/mcnp/src/tally/mcnp_kcon.py single.assembly_7815.keff.inp.o
popd
pushd 0wt/10wt/30cm/out/
echo
echo $PWD
echo
python ~/github/scripts/mcnp/src/tally/mcnp_kcon.py single.assembly_7815.keff.inp.o
popd
pushd 0wt/30wt/1.5cm/out/
echo
echo $PWD
echo
python ~/github/scripts/mcnp/src/tally/mcnp_kcon.py single.assembly_7815.keff.inp.o
popd
pushd 0wt/30wt/30cm/out/
echo
echo $PWD
echo
python ~/github/scripts/mcnp/src/tally/mcnp_kcon.py single.assembly_7815.keff.inp.o
popd
pushd 75wt/10wt/1.5cm/out/
echo
echo $PWD
echo
python ~/github/scripts/mcnp/src/tally/mcnp_kcon.py single.assembly_7815.keff.inp.o
popd
pushd 75wt/10wt/30cm/out/
echo
echo $PWD
echo
python ~/github/scripts/mcnp/src/tally/mcnp_kcon.py single.assembly_7815.keff.inp.o
popd
pushd 75wt/30wt/1.5cm/out/
echo
echo $PWD
echo
python ~/github/scripts/mcnp/src/tally/mcnp_kcon.py single.assembly_7815.keff.inp.o
popd
pushd 75wt/30wt/30cm/out/
echo
echo $PWD
echo
python ~/github/scripts/mcnp/src/tally/mcnp_kcon.py single.assembly_7815.keff.inp.o
popd
echo
echo $PWD
echo
