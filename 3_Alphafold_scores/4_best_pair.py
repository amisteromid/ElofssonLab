import pandas as pd
from sys import argv
import json

### this code would extract the pair with the most contact and remove others

#result = argv[1]
#chain_map = argv[2]

with open('chain_map.json') as f:
      mapping = json.load(f)


df1 = pd.read_csv('result.txt')

pair = []

for ID,info in df1.iterrows():
      pdb_id = df1.loc[ID,'pdb_id']
      chain1 = df1.loc[ID,'chain1']
      chain2 = df1.loc[ID,'chain2']
      alter1=mapping[pdb_id][chain1]
      alter2=mapping[pdb_id][chain2]
      l = [alter1, alter2]
      l.sort()
      pair.append(pdb_id+'_'+l[0]+'_'+pdb_id+'_'+l[1])

df1['pair']=pair
df = df1.drop(['pdb_id','chain1', 'chain2'], axis=1, inplace=True)

idx = df1.groupby('pair')['obs_contact'].idxmax()
df_filtered = df1.loc[idx]

df_filtered = df_filtered.set_index('pair')


df_filtered.to_csv('new_results.csv')
      

