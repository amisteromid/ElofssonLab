cat ../pdb_ids.txt| while read p; do pymol -cq for_pymol.py $p; done
