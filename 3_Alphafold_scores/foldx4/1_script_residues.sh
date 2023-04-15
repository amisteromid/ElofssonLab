# loops through all directories in chains folder and run the FOLDX for each pdb file


for pdb in /home/omid/Desktop/chains/*; do
	pdb=$(echo $pdb |cut -d'/' -f6)
	pair=$(echo $pdb |cut -d'/' -f6 |cut -d'.' -f1)
	#sed -e "s|pdb_file|$pdb|g;s|pair|$pair|g" config.cfg > modified_config.cfg
	#mkdir output/$pair
	#./foldx_20231231 -f modified_config.cfg
	python3 /home/omid/Downloads/2_extract_foldx_residues.py /home/omid/Downloads/foldx4/output/$pair/Interface_* /home/omid/Downloads/foldx4/output/$pair
done

