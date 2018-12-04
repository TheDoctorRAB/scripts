#!/bin/bash
cd 0wt/dat/dose-rate
python ~/github/scripts/mcnp/src/output/mcnp_maxmin.py single.assembly_7815_container.bottom_dose.rate.out
python ~/github/scripts/mcnp/src/output/mcnp_maxmin.py single.assembly_7815_container.surface_dose.rate.out
python ~/github/scripts/mcnp/src/output/mcnp_maxmin.py single.assembly_7815_container.top_dose.rate.out
cd ../../../10wt/dat/dose-rate

python ~/github/scripts/mcnp/src/output/mcnp_maxmin.py single.assembly_7815_container.bottom_dose.rate.out
python ~/github/scripts/mcnp/src/output/mcnp_maxmin.py single.assembly_7815_container.surface_dose.rate.out
python ~/github/scripts/mcnp/src/output/mcnp_maxmin.py single.assembly_7815_container.top_dose.rate.out
cd ../../../25wt/dat/dose-rate

python ~/github/scripts/mcnp/src/output/mcnp_maxmin.py single.assembly_7815_container.bottom_dose.rate.out
python ~/github/scripts/mcnp/src/output/mcnp_maxmin.py single.assembly_7815_container.surface_dose.rate.out
python ~/github/scripts/mcnp/src/output/mcnp_maxmin.py single.assembly_7815_container.top_dose.rate.out
cd ../../../50wt/dat/dose-rate

python ~/github/scripts/mcnp/src/output/mcnp_maxmin.py single.assembly_7815_container.bottom_dose.rate.out
python ~/github/scripts/mcnp/src/output/mcnp_maxmin.py single.assembly_7815_container.surface_dose.rate.out
python ~/github/scripts/mcnp/src/output/mcnp_maxmin.py single.assembly_7815_container.top_dose.rate.out
cd ../../../5wt/dat/dose-rate

python ~/github/scripts/mcnp/src/output/mcnp_maxmin.py single.assembly_7815_container.bottom_dose.rate.out
python ~/github/scripts/mcnp/src/output/mcnp_maxmin.py single.assembly_7815_container.surface_dose.rate.out
python ~/github/scripts/mcnp/src/output/mcnp_maxmin.py single.assembly_7815_container.top_dose.rate.out
cd ../../../75wt/dat/dose-rate

python ~/github/scripts/mcnp/src/output/mcnp_maxmin.py single.assembly_7815_container.bottom_dose.rate.out
python ~/github/scripts/mcnp/src/output/mcnp_maxmin.py single.assembly_7815_container.surface_dose.rate.out
python ~/github/scripts/mcnp/src/output/mcnp_maxmin.py single.assembly_7815_container.top_dose.rate.out
cd ../../../../

