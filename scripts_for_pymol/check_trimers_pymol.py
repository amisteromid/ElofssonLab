from sys import argv
import json
import os
from pymol import cmd
from supermultimer import supermultimer

df = {}
for subdir, dirs, files in os.walk('/home/omid/Desktop/5LE5_predictions/extracted_5le5_trimers'):
	if len(files)==0: continue
	trimer = subdir.split('/')[-1]
	trimer = trimer.replace('a','M')
	trimer = trimer.replace('b','N')
	
	for f in files:
		if f.endswith('.pdb'): pdb_file = os.path.join(subdir,f)
		elif f.endswith('.txt'): ptm_score = open(os.path.join(subdir,f)).read().rstrip()
		
	
	cmd.fetch('5le5')
	cmd.remove('5le5 and not chain %s and not chain %s and not chain %s' %(trimer[0], trimer[1], trimer[2]))
	cmd.remove('not polymer.protein')
	cmd.load(pdb_file)
	rmsd=supermultimer('5le5',pdb_file.split('/')[-1][:-4])
	cmd.delete('all')
	
	df[trimer]=[rmsd,ptm_score]
	print(trimer,rmsd,ptm_score)
	
#print(df)

with open('/home/omid/Desktop/5LE5_predictions/extracted_5le5_trimers/rmsds.txt','w') as f:
	for trimer in df:
		f.write(trimer+','+str(df[trimer][0])+','+str(df[trimer][1])+'\n')


