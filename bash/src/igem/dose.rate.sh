python ~/github/scripts/mcnp/src/output/mcnp_compute.dose.py single.assembly_7815_west.plate.out
python ~/github/scripts/mcnp/src/output/mcnp_compute.dose.py single.assembly_7815_east.plate.out 
python ~/github/scripts/mcnp/src/output/mcnp_compute.dose.py single.assembly_7815_south.plate.out 
python ~/github/scripts/mcnp/src/output/mcnp_compute.dose.py single.assembly_7815_north.plate.out 
python ~/github/scripts/mcnp/src/output/mcnp_compute.dose.py single.assembly_7815_cap.out 
python ~/github/scripts/mcnp/src/output/mcnp_compute.dose.py single.assembly_7815_plug.out
mv *dose* ../dose-rate
cd ../../../

