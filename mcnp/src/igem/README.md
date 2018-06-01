# IGEM

Scripts here are directly related to the used fuel cooling cask. Because the geometry is very complex and there are a lot of surfaces included, the scripts are needed to compute all the positions; e.g., location of the pipes, thickness of the gap, lattice size, etc.  
***
Files in the archive directory were the original scripting created by Seth Dustin. These just had the fuel as a block, surrounding by the cooling plates and welds. These scripts computed all the surface positions and created the cells. This model was limited to two cooling loops per plate. 
***
The current directory contains the cask designs used for the IGEM cask modeling and simulation. The fuel is modeled as an assembly (lattice) surrounded by a gas gap; air, He, etc. This increases the length, width of the cooling plates. Scripts compute all the positions of the surfaces and accounts for the addition of cooling pipes per plate. The output file produces a list of the surface ID, type, and position such that it can be edited directly into the corresponding mcnp input file. 
