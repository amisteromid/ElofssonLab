#!/bin/bash

# Create the header row for the CSV file
echo "id,chain1,chain2,numbers" > output.txt

# Loop through each subfolder in the 'output' directory
for subfolder in /home/omid/Downloads/foldx4/output/*; do
	if [ -d "$subfolder" ]; then
		echo $subfolder | cut -d'/' -f7
		# Extract the 'id', 'chain1', and 'chain2' from the subfolder name
		id=$(echo $subfolder | cut -d'/' -f7 | cut -d'_' -f1)
		chain1=$(echo $subfolder | cut -d'/' -f7 | cut -d'_' -f2)
		chain2=$(echo $subfolder | cut -d'/' -f7 | cut -d'_' -f4)

		# Extract the 'numbers' from the Interface_Residues.txt file in the subfolder
		interface_residues_file=$(find $subfolder -name "Interface_Residues*")
		numbers=$(sed -n '11p' $interface_residues_file)

		# Add the data to the CSV file
		echo "$id,$chain1,$chain2,$numbers" >> output.txt
    fi
done
