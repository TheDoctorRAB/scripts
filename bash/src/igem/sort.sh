ll:qpython ~/github/scripts/mcnp/src/tally/mcnp_final.tally.py ../../10wt/1.5cm/out/single.assembly_7815.inp.o ../../30wt/1.5cm/out/single.assembly_7815.inp.o ../../50wt/1.5cm/out/single.assembly_7815.inp.o ../../70wt/1.5cm/out/single.assembly_7815.inp.o ../../90wt/1.5cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally.py ../../10wt/3cm/out/single.assembly_7815.inp.o ../../30wt/3cm/out/single.assembly_7815.inp.o ../../50wt/3cm/out/single.assembly_7815.inp.o ../../70wt/3cm/out/single.assembly_7815.inp.o ../../90wt/3cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally.py ../../10wt/6cm/out/single.assembly_7815.inp.o ../../30wt/6cm/out/single.assembly_7815.inp.o ../../50wt/6cm/out/single.assembly_7815.inp.o ../../70wt/6cm/out/single.assembly_7815.inp.o ../../90wt/6cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally.py ../../10wt/12cm/out/single.assembly_7815.inp.o ../../30wt/12cm/out/single.assembly_7815.inp.o ../../50wt/12cm/out/single.assembly_7815.inp.o ../../70wt/12cm/out/single.assembly_7815.inp.o ../../90wt/12cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally.py ../../10wt/18cm/out/single.assembly_7815.inp.o ../../30wt/18cm/out/single.assembly_7815.inp.o ../../50wt/18cm/out/single.assembly_7815.inp.o ../../70wt/18cm/out/single.assembly_7815.inp.o ../../90wt/18cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/tally/mcnp_final.tally.py ../../10wt/30cm/out/single.assembly_7815.inp.o ../../30wt/30cm/out/single.assembly_7815.inp.o ../../50wt/30cm/out/single.assembly_7815.inp.o ../../70wt/30cm/out/single.assembly_7815.inp.o ../../90wt/30cm/out/single.assembly_7815.inp.o
python ~/github/scripts/mcnp/src/output/mcnp_compute.dose.py single.assembly_7815_west.plate.out
python ~/github/scripts/mcnp/src/output/mcnp_compute.dose.py single.assembly_7815_east.plate.out 
python ~/github/scripts/mcnp/src/output/mcnp_compute.dose.py single.assembly_7815_south.plate.out 
python ~/github/scripts/mcnp/src/output/mcnp_compute.dose.py single.assembly_7815_north.plate.out 
python ~/github/scripts/mcnp/src/output/mcnp_compute.dose.py single.assembly_7815_cap.out 
python ~/github/scripts/mcnp/src/output/mcnp_compute.dose.py single.assembly_7815_plug.out
mv *dose* ../dose-rate
cd ../../../

mv ou single.assembly_7815.inp.o
mv single.assembly_7815.inp.o out/

