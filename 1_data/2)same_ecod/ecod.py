from sys import argv

# python3 ecod.py ecod_db.txt pdb_ids.txt	

def ecod_collector(db, pdb_id):
	# takes as input database and pdb id -------> checks whether all chains have same id/ids or not 
	# ===> print the pdb id and add it to the list if true
	ecod_ids = {}
	
	line = db.readline()
	while line:
		line = line.split("|")
		domain = line[0]
		ecod = line[1]
		chain = line[2].split(':')[0]
		if pdb_id.lower() == domain.lower()[0:4]:
			if chain not in ecod_ids:
				ecod_ids[chain] = [ecod]
			else:
				ecod_ids[chain].append(ecod)
		line = db.readline()
	#print (ecod_ids)
	ok = True
	if len(ecod_ids)>1:
		first = sorted(list(ecod_ids.values())[0])
		for v in list(ecod_ids.values()):
			if first != sorted(v):
				ok = False
	if ok == True and len(ecod_ids)>1:
		print (pdb_id)
		final_ids.append(pdb_id)
		
		
		
		
if __name__ == "__main__":
	ecod_database = argv[1]
	ecod_database = open(ecod_database,"r")
	
	pdb_ids = argv[2]
	pdb_ids = open(pdb_ids,"r")
	pdb_ids = pdb_ids.read().split('\n')[:-1]
	

	final_ids = []
	for pdb_id in pdb_ids:
		ecod_database.seek(0)
		ecod_collector(ecod_database, pdb_id)
	print (final_ids)
	'''
	df = pd.DataFrame.from_dict(final_ids, orient='index')
	df.columns = ['ecod']
	df.to_csv('ids.csv', index=True, header=True)
	#print (find_chain_ids(ecod_database,'6rgq'))
	'''
	
	
	
	
	
	
	
	
	
	
	
