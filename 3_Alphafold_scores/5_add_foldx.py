import pandas as pd
from sys import argv
import json

### gets

#chain_map = argv[1]
#result = argv[2]
#scoring_results = argv[3]

with open('chain_map.json') as f:
      mapping = json.load(f)


df1 = pd.read_csv('all_foldx.csv')

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
df1.drop(['pdb_id','chain1', 'chain2'], axis=1, inplace=True)



df2 = pd.read_csv('new_results.csv')

df3 =pd.merge(df1, df2, on="pair")

df3.to_csv('final.txt', index=False)

