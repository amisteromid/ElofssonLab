# extract 5LE5 pairs residues


from sys import argv
import pandas as pd
import numpy as np


# python3 5LE5_residues.py /home/omid/Downloads/foldx4/output/5LE5_pairs/*/Interface_* /home/omid/Desktop/5LE5_residues.txt

data = argv[1]

pair_name = data.split('/')[7]
file_name = data.split('/')[8]
rank_name = pair_name + '_' +file_name.split('_')[3]
print (rank_name)

# open each output file and extract line 9 and 10
with open(data) as f:
	line=f.readlines()[10].rstrip()
data = line.split('\t')
B=[]
C=[]
for each in data:
	if each[1] == 'B':
		B.append(each[2:])
	else:
		C.append(each[2:])


# write the file
data_output = argv[2]

with open(data_output,'a') as f:
	f.write(rank_name+'\n')
	f.write(','.join(B)+'\n')
	f.write(','.join(C)+'\n')
