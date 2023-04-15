from sys import argv
import pandas as pd

# python3 morefilter.py


if __name__ == "__main__":
	
	raw_report = argv[1]
	raw_report = pd.read_csv(raw_report)
	raw_report.fillna(method='ffill',inplace = True)
	#raw_report = raw_report.set_index('Entry ID')
	#print (set(raw_report.index))
	
	#remove non protein polymers or short chains
	filtered = {}
	size={}
	for ID,info in raw_report.iterrows():
		entry = raw_report.loc[ID,'Entry ID']
		if entry not in filtered:
			filtered[entry] = raw_report.loc[ID,'Total Number of Polymer Instances (Chains)']
			size[entry]=[]
			if (raw_report.loc[ID,'Entity Polymer Type'] == 'Protein'):
				size[entry].append([raw_report.loc[ID,'Polymer Entity Sequence Length'], raw_report.loc[ID,'Total Number of polymer Entity Instances (Chains) per Entity']])
		else:
			if (raw_report.loc[ID,'Entity Polymer Type'] == 'Protein'):
				size[entry].append([raw_report.loc[ID,'Polymer Entity Sequence Length'], raw_report.loc[ID,'Total Number of polymer Entity Instances (Chains) per Entity']])
	
	for i in list(filtered):
		counter=0
		for ii in size[i]:
			if ii[0]/ max([x[0] for x in size[i]]) <1/2:
				filtered[i] -= ii[1]
			else:
				counter += 1
		if counter < 2:
			del filtered[i]
		
	for i in list(filtered):
		if filtered[i] <4:
			del filtered[i]
			
	with open("final.txt", 'w') as f: 
		for key, value in filtered.items(): 
			f.write('%s,%s\n' % (key, value))
