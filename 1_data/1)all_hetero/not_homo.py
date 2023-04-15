from sys import argv
import pandas as pd
import re


# python3 not_homo.py rcsb_pdb_custom_report_24772805b0c0d9d87f782b42626243be_0001-2500.csv

if __name__ == "__main__":
	pdb_ids = []
	db = argv[1]
	db = pd.read_csv(db)
	db.drop(['Unnamed: 2'], axis=1,inplace = True)
	db.fillna(method='ffill',inplace = True)
	for id,info in db.iterrows():
		olig = db.loc[id,'Oligomeric State']
		if olig.find('Hetero') != -1:
			numbers = re.findall(r'\b\d+',olig)
			numbers = list(filter(lambda x: int(x)>3,numbers))
			if len(numbers)>0:
				pdb_ids.append(db.loc[id,'Entry ID'])
	
	f = open('pdb_ids.txt','a')
	for i in set(pdb_ids):
		f.write(i+'\n')
	f.close()
