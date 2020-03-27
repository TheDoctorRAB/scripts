#!/bin/bash
pushd 0wt/10wt/1.5cm/inp/
echo
echo $PWD
echo
sub_mcnpx_2.7.0 -i single.assembly_7815.keff.inp -w 02:00:00 -n16 -P iuc
popd
pushd 0wt/10wt/30cm/inp/
echo
echo $PWD
echo
sub_mcnpx_2.7.0 -i single.assembly_7815.keff.inp -w 02:00:00 -n16 -P iuc
popd
pushd 0wt/30wt/1.5cm/inp/
echo
echo $PWD
echo
sub_mcnpx_2.7.0 -i single.assembly_7815.keff.inp -w 02:00:00 -n16 -P iuc
popd
pushd 0wt/30wt/30cm/inp/
echo
echo $PWD
echo
sub_mcnpx_2.7.0 -i single.assembly_7815.keff.inp -w 02:00:00 -n16 -P iuc
popd
pushd 75wt/10wt/1.5cm/inp/
echo
echo $PWD
echo
sub_mcnpx_2.7.0 -i single.assembly_7815.keff.inp -w 02:00:00 -n16 -P iuc
popd
pushd 75wt/10wt/30cm/inp/
echo
echo $PWD
echo
sub_mcnpx_2.7.0 -i single.assembly_7815.keff.inp -w 02:00:00 -n16 -P iuc
popd
pushd 75wt/30wt/1.5cm/inp/
echo
echo $PWD
echo
sub_mcnpx_2.7.0 -i single.assembly_7815.keff.inp -w 02:00:00 -n16 -P iuc
popd
pushd 75wt/30wt/30cm/inp/
echo
echo $PWD
echo
sub_mcnpx_2.7.0 -i single.assembly_7815.keff.inp -w 02:00:00 -n16 -P iuc
popd
echo
echo $PWD
echo
