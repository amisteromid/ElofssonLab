from sys import argv
import pandas as pd

# python3 filter.py rcsb_pdb_custom_report_..... 


if __name__ == "__main__":
	
	raw_report = argv[1]
	raw_report = pd.read_csv(raw_report)
	raw_report.fillna(method='ffill',inplace = True)
	#raw_report = raw_report.set_index('Entry ID')
	#print (set(raw_report.index))
	
	#remove non protein polymers or short chains
	filtered = {}
	unique_chain_count = {}
	for ID,info in raw_report.iterrows():
		entry = raw_report.loc[ID,'Entry ID']
		if entry not in filtered:
			filtered[entry] = raw_report.loc[ID,'Total Number of Polymer Instances (Chains)']
			unique_chain_count[entry]=0
			if (raw_report.loc[ID,'Polymer Entity Sequence Length'] < 20) | (raw_report.loc[ID,'Entity Polymer Type'] != 'Protein'):
				filtered[entry] -= raw_report.loc[ID,'Total Number of polymer Entity Instances (Chains) per Entity']
			else:
				unique_chain_count[entry] += 1
		else:
			if (raw_report.loc[ID,'Polymer Entity Sequence Length'] < 20) | (raw_report.loc[ID,'Entity Polymer Type'] != 'Protein'):
				filtered[entry] -= raw_report.loc[ID,'Total Number of polymer Entity Instances (Chains) per Entity']
			else:
				unique_chain_count[entry] += 1
	for i in list(filtered):
		if filtered[i] <4 or unique_chain_count[i] <2:
			del filtered[i]
	with open("final.txt", 'a') as f: 
		for key, value in filtered.items(): 
			f.write('%s,%s\n' % (key, value))
			
