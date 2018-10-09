From the material backfill directory, use these commands to copy the mcnpfile to the subdirectories
The mcnpfile in the submaster-inp directory should have all the cooling plate cell cards and B10wt%/B4C wt% in the materials cards commented out.
So copy the files into the subdirectories and then uncomment the relevant cards.

echo 5wt/10wt/1.5cm/inp/ 5wt/30wt/1.5cm/inp/ 5wt/50wt/1.5cm/inp/ 5wt/70wt/1.5cm/inp/ 5wt/90wt/1.5cm/inp/ | xargs -n 1 cp ../submaster-inp/1.5cm/single.assembly_7815.inp
echo 10wt/10wt/1.5cm/inp/ 10wt/30wt/1.5cm/inp/ 10wt/50wt/1.5cm/inp/ 10wt/70wt/1.5cm/inp/ 10wt/90wt/1.5cm/inp/ | xargs -n 1 cp ../submaster-inp/1.5cm/single.assembly_7815.inp
echo 25wt/10wt/1.5cm/inp/ 25wt/30wt/1.5cm/inp/ 25wt/50wt/1.5cm/inp/ 25wt/70wt/1.5cm/inp/ 25wt/90wt/1.5cm/inp/ | xargs -n 1 cp ../submaster-inp/1.5cm/single.assembly_7815.inp
echo 50wt/10wt/1.5cm/inp/ 50wt/30wt/1.5cm/inp/ 50wt/50wt/1.5cm/inp/ 50wt/70wt/1.5cm/inp/ 50wt/90wt/1.5cm/inp/ | xargs -n 1 cp ../submaster-inp/1.5cm/single.assembly_7815.inp
echo 75wt/10wt/1.5cm/inp/ 75wt/30wt/1.5cm/inp/ 75wt/50wt/1.5cm/inp/ 75wt/70wt/1.5cm/inp/ 75wt/90wt/1.5cm/inp/ | xargs -n 1 cp ../submaster-inp/1.5cm/single.assembly_7815.inp
echo 5wt/10wt/3cm/inp/ 5wt/30wt/3cm/inp/ 5wt/50wt/3cm/inp/ 5wt/70wt/3cm/inp/ 5wt/90wt/3cm/inp/ | xargs -n 1 cp ../submaster-inp/3cm/single.assembly_7815.inp
echo 10wt/10wt/3cm/inp/ 10wt/30wt/3cm/inp/ 10wt/50wt/3cm/inp/ 10wt/70wt/3cm/inp/ 10wt/90wt/3cm/inp/ | xargs -n 1 cp ../submaster-inp/3cm/single.assembly_7815.inp
echo 25wt/10wt/3cm/inp/ 25wt/30wt/3cm/inp/ 25wt/50wt/3cm/inp/ 25wt/70wt/3cm/inp/ 25wt/90wt/3cm/inp/ | xargs -n 1 cp ../submaster-inp/3cm/single.assembly_7815.inp
echo 50wt/10wt/3cm/inp/ 50wt/30wt/3cm/inp/ 50wt/50wt/3cm/inp/ 50wt/70wt/3cm/inp/ 50wt/90wt/3cm/inp/ | xargs -n 1 cp ../submaster-inp/3cm/single.assembly_7815.inp
echo 75wt/10wt/3cm/inp/ 75wt/30wt/3cm/inp/ 75wt/50wt/3cm/inp/ 75wt/70wt/3cm/inp/ 75wt/90wt/3cm/inp/ | xargs -n 1 cp ../submaster-inp/3cm/single.assembly_7815.inp
echo 5wt/10wt/6cm/inp/ 5wt/30wt/6cm/inp/ 5wt/50wt/6cm/inp/ 5wt/70wt/6cm/inp/ 5wt/90wt/6cm/inp/ | xargs -n 1 cp ../submaster-inp/6cm/single.assembly_7815.inp
echo 10wt/10wt/6cm/inp/ 10wt/30wt/6cm/inp/ 10wt/50wt/6cm/inp/ 10wt/70wt/6cm/inp/ 10wt/90wt/6cm/inp/ | xargs -n 1 cp ../submaster-inp/6cm/single.assembly_7815.inp
echo 25wt/10wt/6cm/inp/ 25wt/30wt/6cm/inp/ 25wt/50wt/6cm/inp/ 25wt/70wt/6cm/inp/ 25wt/90wt/6cm/inp/ | xargs -n 1 cp ../submaster-inp/6cm/single.assembly_7815.inp
echo 50wt/10wt/6cm/inp/ 50wt/30wt/6cm/inp/ 50wt/50wt/6cm/inp/ 50wt/70wt/6cm/inp/ 50wt/90wt/6cm/inp/ | xargs -n 1 cp ../submaster-inp/6cm/single.assembly_7815.inp
echo 75wt/10wt/6cm/inp/ 75wt/30wt/6cm/inp/ 75wt/50wt/6cm/inp/ 75wt/70wt/6cm/inp/ 75wt/90wt/6cm/inp/ | xargs -n 1 cp ../submaster-inp/6cm/single.assembly_7815.inp
echo 5wt/10wt/12cm/inp/ 5wt/30wt/12cm/inp/ 5wt/50wt/12cm/inp/ 5wt/70wt/12cm/inp/ 5wt/90wt/12cm/inp/ | xargs -n 1 cp ../submaster-inp/12cm/single.assembly_7815.inp
echo 10wt/10wt/12cm/inp/ 10wt/30wt/12cm/inp/ 10wt/50wt/12cm/inp/ 10wt/70wt/12cm/inp/ 10wt/90wt/12cm/inp/ | xargs -n 1 cp ../submaster-inp/12cm/single.assembly_7815.inp
echo 25wt/10wt/12cm/inp/ 25wt/30wt/12cm/inp/ 25wt/50wt/12cm/inp/ 25wt/70wt/12cm/inp/ 25wt/90wt/12cm/inp/ | xargs -n 1 cp ../submaster-inp/12cm/single.assembly_7815.inp
echo 50wt/10wt/12cm/inp/ 50wt/30wt/12cm/inp/ 50wt/50wt/12cm/inp/ 50wt/70wt/12cm/inp/ 50wt/90wt/12cm/inp/ | xargs -n 1 cp ../submaster-inp/12cm/single.assembly_7815.inp
echo 75wt/10wt/12cm/inp/ 75wt/30wt/12cm/inp/ 75wt/50wt/12cm/inp/ 75wt/70wt/12cm/inp/ 75wt/90wt/12cm/inp/ | xargs -n 1 cp ../submaster-inp/12cm/single.assembly_7815.inp
echo 5wt/10wt/18cm/inp/ 5wt/30wt/18cm/inp/ 5wt/50wt/18cm/inp/ 5wt/70wt/18cm/inp/ 5wt/90wt/18cm/inp/ | xargs -n 1 cp ../submaster-inp/18cm/single.assembly_7815.inp
echo 10wt/10wt/18cm/inp/ 10wt/30wt/18cm/inp/ 10wt/50wt/18cm/inp/ 10wt/70wt/18cm/inp/ 10wt/90wt/18cm/inp/ | xargs -n 1 cp ../submaster-inp/18cm/single.assembly_7815.inp
echo 25wt/10wt/18cm/inp/ 25wt/30wt/18cm/inp/ 25wt/50wt/18cm/inp/ 25wt/70wt/18cm/inp/ 25wt/90wt/18cm/inp/ | xargs -n 1 cp ../submaster-inp/18cm/single.assembly_7815.inp
echo 50wt/10wt/18cm/inp/ 50wt/30wt/18cm/inp/ 50wt/50wt/18cm/inp/ 50wt/70wt/18cm/inp/ 50wt/90wt/18cm/inp/ | xargs -n 1 cp ../submaster-inp/18cm/single.assembly_7815.inp
echo 75wt/10wt/18cm/inp/ 75wt/30wt/18cm/inp/ 75wt/50wt/18cm/inp/ 75wt/70wt/18cm/inp/ 75wt/90wt/18cm/inp/ | xargs -n 1 cp ../submaster-inp/18cm/single.assembly_7815.inp
echo 5wt/10wt/30cm/inp/ 5wt/30wt/30cm/inp/ 5wt/50wt/30cm/inp/ 5wt/70wt/30cm/inp/ 5wt/90wt/30cm/inp/ | xargs -n 1 cp ../submaster-inp/30cm/single.assembly_7815.inp
echo 10wt/10wt/30cm/inp/ 10wt/30wt/30cm/inp/ 10wt/50wt/30cm/inp/ 10wt/70wt/30cm/inp/ 10wt/90wt/30cm/inp/ | xargs -n 1 cp ../submaster-inp/30cm/single.assembly_7815.inp
echo 25wt/10wt/30cm/inp/ 25wt/30wt/30cm/inp/ 25wt/50wt/30cm/inp/ 25wt/70wt/30cm/inp/ 25wt/90wt/30cm/inp/ | xargs -n 1 cp ../submaster-inp/30cm/single.assembly_7815.inp
echo 50wt/10wt/30cm/inp/ 50wt/30wt/30cm/inp/ 50wt/50wt/30cm/inp/ 50wt/70wt/30cm/inp/ 50wt/90wt/30cm/inp/ | xargs -n 1 cp ../submaster-inp/30cm/single.assembly_7815.inp
echo 75wt/10wt/30cm/inp/ 75wt/30wt/30cm/inp/ 75wt/50wt/30cm/inp/ 75wt/70wt/30cm/inp/ 75wt/90wt/30cm/inp/ | xargs -n 1 cp ../submaster-inp/30cm/single.assembly_7815.inp
