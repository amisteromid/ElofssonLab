# make dataset from 5LE5_residues.txt

from sys import argv
import pandas as pd
import numpy as np


data = argv[1]

import pandas as pd

# create empty lists for each column
chain1 = []
chain2 = []
rank = []
res1 = []
res2 = []

# iterate through the data and add to the lists
with open(data, 'r') as f:
    lines = f.readlines()
    for i in range(0, len(lines), 3):
        chain1.append(lines[i].split('_')[1])
        chain2.append(lines[i].split('_')[3])
        rank.append(lines[i].split('_')[4].rstrip())
        res1.append(lines[i+1].rstrip().split(','))
        res2.append(lines[i+2][:-1].rstrip().split(','))

# create a dataframe from the lists
df = pd.DataFrame({
    'chain1': chain1,
    'chain2': chain2,
    'rank': rank,
    'res1': res1,
    'res2': res2
})

# convert data types
df['rank'] = df['rank'].astype(int)

df.to_csv('5LE5_residues_dataframe.txt', index=False)

print('Dataframe saved to output.csv.')

