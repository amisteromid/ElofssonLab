from sys import argv
import pandas as pd
import json

# python3 make_chain_map_json.py report_with_seq.csv pairs.txt

if __name__ == "__main__":
	raw_dic={}
	pairs=open(argv[2])
	line=pairs.readline()[:-1]
	while line:
		line=line.split('_')
		if line[0] not in raw_dic:
			raw_dic[line[0]]=set()
			raw_dic[line[0]].add(line[1])
			raw_dic[line[0]].add(line[2])
		else: 
			raw_dic[line[0]].add(line[1])
			raw_dic[line[0]].add(line[2])
		line=pairs.readline()[:-1]
	
	dic = {}
	report=argv[1]
	report = pd.read_csv(report)
	report.fillna(method='ffill',inplace = True)
	print (report)
	for ID,info in report.iterrows():
		entry = report.loc[ID,'Entry ID']
		chain = report.loc[ID,'Auth Asym ID']
		entity = report.loc[ID,'Entity ID']
		if entry not in dic:
			dic[entry]={}
			dic[entry][entity]=[chain]
		else:
			if entity not in dic[entry]:
				dic[entry][entity]=[chain]
			else:
				dic[entry][entity].append(chain)
	
	final_dic={}
	for entry in dic:
		final_dic[entry]={}
		for entity in dic[entry]:
			for chain in dic[entry][entity]:
				if chain in raw_dic[entry]:
					representative=chain
			for chain in dic[entry][entity]:
				final_dic[entry][chain]=representative
	
	with open("chain_map.json", "w") as fp:
		json.dump(final_dic,fp)
				
			
			
			
			
			
			
			
			
		
