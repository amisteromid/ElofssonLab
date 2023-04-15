from sys import argv
import pandas as pd
import os

# python3 merge_results.py /home/omid/Downloads/foldx4/output/

foldx_path=argv[1]

all_data = pd.DataFrame()
for each in os.listdir(foldx_path):
	if each.endswith('.csv'):
		filepath= os.path.join(foldx_path,each)
		data = pd.read_csv(filepath)
		all_data = pd.concat([all_data,data], ignore_index=True)
		
all_data.to_csv('all_foldx.csv',index=False)


