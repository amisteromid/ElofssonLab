from sys import argv
import pandas as pd
import os

# python3 merge_results.py /home/omid/Downloads/foldx4/output/

foldx_path=argv[1]

all_data = {}
for each in os.listdir(foldx_path):
	if each.endswith('.txt'):
		id1,id2= each[:-4].split('_')[1],each[:-4].split('_')[3]
		filepath= os.path.join(foldx_path,each)
		content = open(filepath).read().splitlines()
		chain1_numbers = [int(x) for x in content[0].split(',')]
		chain2_numbers = [int(x) for x in content[0].split(',')]
		all_data[each[:-4]] = {'chain1':chain1_numbers,'chain2':chain2_numbers}
		#all_data = pd.concat([all_data,data], ignore_index=True)

df = pd.DataFrame.from_dict(all_data, orient='index')
df.to_csv('foldx_residues.csv')


