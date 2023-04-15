#!/bin/bash

### This script iterate through all pairs; make 1) observed file 2) predicted file using different scores

source myenv/bin/activate

# Define the directory paths (CHANGE THE DIRECTORIES)
desktop_dir="/proj/berzelius-2021-29/users/x_omimo"
output_dir="/proj/berzelius-2021-29/users/x_omimo/contacts" #output
af_result_dir="/proj/berzelius-2021-29/users/x_omimo/utils" # directory for python scripts

# Loop through each chain pair directory (CHANGE THE REGEX)
while read -r line; do
    chain_dir="/proj/berzelius-2021-29/users/x_omimo/output/extracted_pairs/$line"
#for chain_dir in $desktop_dir/output/extracted_pairs/*; do
    # Extract the pdb id, chain A, and chain B from the directory name
    pdb_id=$(echo "$chain_dir" | cut -d "/" -f8 | cut -d'_' -f1)
    chain_a=$(echo "$chain_dir" | cut -d "/" -f8 | cut -d'_' -f2)
    chain_b=$(echo "$chain_dir" | cut -d "/" -f8 | cut -d'_' -f4)

    # Create a directory for the pdb id on the desktop
    pdb_dir="$output_dir/$pdb_id"
    mkdir -p "$pdb_dir"

    # Download the pdb file for the chain pair
    wget -nc "https://files.rcsb.org/download/${pdb_id}.cif" -P "$pdb_dir"

    # Run the contact.py script for the downloaded pdb file and save the result in observed.txt
    cd "$af_result_dir"
    if [ ! -e $pdb_dir/observed.txt ]; then python3 chaincontacts.py -c $pdb_dir/*.cif -C 8 > "$pdb_dir/observed.txt"; fi

    # Run the contact.py, pdockq1.py, and pdockq2.py scripts for each chain pair and save the results in predicted.txt
    echo "${pdb_id}_${chain_a}_${pdb_id}_${chain_b}" >> "$pdb_dir/predicted.txt"
    python3 chaincontacts.py -p $chain_dir/*.pdb -C 8 >> "$pdb_dir/predicted.txt"
    python3 pDockQ2.py -p $chain_dir/*.pdb -C 8 >> "$pdb_dir/predicted.txt"
    python3 pdockqi_calc.py -pkl $chain_dir/*.pkl -pdb $chain_dir/*.pdb -dist 8 >> "$pdb_dir/predicted.txt"
    cat $chain_dir/ptm.txt >> "$pdb_dir/predicted.txt"
    echo >> "$pdb_dir/predicted.txt"
done < not_in_all_result.txt
#done

# Concatenate all of the predicted.txt files into dockq.txt
#cat "$chains_dir"/*/predicted.txt > "$desktop_dir/dockq.txt"
