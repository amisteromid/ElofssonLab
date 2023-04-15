from sys import argv
import pandas as pd

# python3 ecod_count.py ecod_db.txt raw_report.csv


if __name__ == "__main__":
	
	ecod_db = argv[1]
	ecod_db = open(ecod_db)
	
	raw_report = argv[2]
	raw_report = pd.read_csv(raw_report)
	raw_report.fillna(method='ffill',inplace = True)
	raw_report = raw_report.set_index('Entry ID')
	raw_report.drop(['Unnamed: 5'], axis=1,inplace = True)
	#print (set(raw_report.index))
	
	#count number of ecods for each pdb id in database
	ecod_count_dic = {}
	line = ecod_db.readline()
	while line:
		identifier = line[:4].lower()
		ecod = line.split('|')[1]
		chain = line.split('|')[2].split(':')[0]
		if identifier in ecod_count_dic:
			if chain in ecod_count_dic[identifier]:
				ecod_count_dic[identifier][chain].append(ecod)
			else:
				ecod_count_dic[identifier][chain]=[ecod]
		else :
			ecod_count_dic[identifier] = {chain:[ecod]}
		line = ecod_db.readline()
	
	# Add the counts and ecod identifier to the report file	
	ecod_count_list = [0 for x in raw_report.index]
	raw_report['ecod_count'] = ecod_count_list
	ecod_id_list = [[] for x in raw_report.index]
	raw_report['ecod_id'] = ecod_id_list
	for ID,info in raw_report.iterrows():
		if ID.lower() in ecod_count_dic:
			raw_report.loc[ID,'ecod_count'] = len(ecod_count_dic[ID.lower()])
			raw_report.loc[ID,'ecod_id'] = ','.join(list(ecod_count_dic[ID.lower()].values())[0])
		else:
			raw_report.loc[ID,'ecod_count'] = 0
		
	
	raw_report.to_csv('final_report.csv', index=True, header=True)
