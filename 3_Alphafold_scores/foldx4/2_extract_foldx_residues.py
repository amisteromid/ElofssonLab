from sys import argv
import pandas as pd
import numpy as np


# python3 extract_foldx.py /home/omid/Downloads/foldx4/output/*/Interaction_* /home/omid/Downloads/foldx4/output/


data = argv[1]
data_output = argv[2]

print(data)
# open each output file and extract line 9 and 10
with open(data) as f:
	line=f.readlines()[10].rstrip()

# Split the residues
data = line.split('\t')
B=[]
C=[]
for each in data:
	if each[1] == 'B':
		B.append(each[2:])
	else:
		C.append(each[2:])


with open(data_output+'.txt','w') as f:
	f.write(','.join(B)+'\n')
	f.write(','.join(C)+'\n')
