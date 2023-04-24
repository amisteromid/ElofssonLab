for i in /home/omid/Downloads/foldx4/output/5LE5_pairs/*/Interface_*; do
	#echo $i
	python3 5LE5_residues.py $i /home/omid/Desktop/5LE5_residues.txt
	
done
