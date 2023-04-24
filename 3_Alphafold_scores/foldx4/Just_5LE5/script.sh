# loops through all directories in chains folder and run the FOLDX for each pdb file


for pdb in /home/omid/Desktop/5LE5_pairs/*; do
	for each_pdb in $pdb/*; do
		pair=$(echo $each_pdb |cut -d'/' -f6)
		rank=$(echo $each_pdb |cut -d'/' -f7)
		sed -e "s|pdb_file|$rank|g;s|pp|$pair|g;s|subfolder|$pair|g" config.cfg > modified_config.cfg
		mkdir output/5LE5_pairs/$pair
		./foldx_20231231 -f modified_config.cfg
	done
done

