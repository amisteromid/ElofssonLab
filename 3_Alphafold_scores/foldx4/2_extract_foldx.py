from sys import argv
import pandas as pd
import numpy as np


# python3 extract_foldx.py /home/omid/Downloads/foldx4/output/*/Interaction_* /home/omid/Downloads/foldx4/output/


data = argv[1]
data_output = argv[2]

# open each output file and extract line 9 and 10
with open(data) as f:
	lines=f.readlines()[8:10]

# some RegEx stuff
data = [line.strip().split('\t') for line in lines]
data[0][0]='pdb_id'
data[0][1]='chain1'
data[0][2]='chain2'
data[1][0]=data[1][0].split('/')[5]
data[1][1]=data[1][0].split('_')[1]
data[1][2]=data[1][0].split('_')[3]
data[1][0]=data[1][0].split('_')[0]

with open(data_output+'.csv','w') as f:
	f.write(','.join(data[0])+'\n')
	f.write(','.join(data[1])+'\n')
