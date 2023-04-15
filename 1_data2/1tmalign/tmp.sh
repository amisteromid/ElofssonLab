cut -d',' -f1 scilifelab.txt >checked.txt
sort -o checked.txt checked.txt 
comm -13 checked.txt pdb_ids0.txt >pdb_ids.txt


#errors are the one that contains nucleic polymer
awk -F, '$2=="error"' tm_report.txt |cut -d',' -f1>comp_ids.txt

