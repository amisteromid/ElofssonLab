import pandas as pd
import numpy as np

res1=[]
res2=[]

df = pd.read_csv('output.txt')

for i, row in df.iterrows():
	tmp1=[]
	tmp2=[]
	if type(row['numbers'])==float:
		print(type(row['numbers']))
		print(row['id'], row['numbers'], row['chain1'], row['chain2'])
	else:
		num=row['numbers'].split()
		for each in num:
			if each[1]=='B':
				tmp1.append(each[2:])
			if each[1]=='C':
				tmp2.append(each[2:])
	res1.append(tmp1)
	res2.append(tmp2)
df['res1']=res1
df['res2']=res2
df.to_csv('output2.txt', index=False)
