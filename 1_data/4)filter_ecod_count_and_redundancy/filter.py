from sys import argv
import pandas as pd

# python3 filter.py ../3\)add_ecod_id_and_counts/final_report.csv

if __name__ == "__main__":
	final_report = argv[1]
	final_report = pd.read_csv(final_report)
	#print (final_report)
	
	
	final_dic = {} #1st ecod, 2nd ecod_count, 3rd protein_entity_count, 4th resolution
	for id,info in final_report.iterrows():
		pdb_id = final_report.loc[id,'Entry ID']
		if pdb_id in final_dic:
			if final_report.loc[id,'Entity Polymer Type'] == 'Protein': final_dic[pdb_id][2] += final_report.loc[id,'Total Number of polymer Entity Instances (Chains) per Entity']
		else:
			final_dic[pdb_id] = [final_report.loc[id,'ecod_id'], final_report.loc[id,'ecod_count'],0,final_report.loc[id,'Resolution (Å)']]
			if final_report.loc[id,'Entity Polymer Type'] == 'Protein': final_dic[pdb_id][2] += final_report.loc[id,'Total Number of polymer Entity Instances (Chains) per Entity'] 
	
	for each in list(final_dic):
		if final_dic[each][1] < final_dic[each][2] or final_dic[each][1] < 4:
			del final_dic[each]
	#print (final_dic)
	

	#remove redundancy
	dic2 = {}
	for pdb in final_dic:
		if (final_dic[pdb][0],final_dic[pdb][1]) not in dic2:
			dic2[(final_dic[pdb][0],final_dic[pdb][1])] = [pdb,final_dic[pdb][-1]]
		else:
			if dic2[(final_dic[pdb][0],final_dic[pdb][1])][1] > final_dic[pdb][-1]:
				dic2[(final_dic[pdb][0],final_dic[pdb][1])] = [pdb,final_dic[pdb][-1]]
				
	final_final = {}
	for each in dic2:
		final_final[dic2[each][0]] = list(each)
	for n in final_final:
		print (n,'-------->',final_final[n])
