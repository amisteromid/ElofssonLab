from sys import argv
import pandas as pd
import numpy as np
import os
import json

### This Python script merge obs and pred data along with the information of pdb_id and chain pairs


# python3 merge_obs_pred.py contacts/5LE5/predicted.txt contacts/5LE5/observed.txt contacts/chain_map.json


pred_file=argv[1]
obs=argv[2]
obs=open(obs)
mapping=argv[3]
with open(mapping) as j:
	mapping = json.load(j)

columns=['pdb_id','chain1','chain2','obs_contact','pred_contact','pdockq1','pdockq2','ptm_iptm']

pdb_id= pred_file.split('/')[-2] ### change here if necessory
line=obs.readline()[:-1]
while line:
	chain1=line.split(',')[0]
	chain2=line.split(',')[1]
	obs_contact=line.split(',')[2]
	line=obs.readline()[:-1]
	
	#print (mapping[pdb_id][chain1])
	associated_pair=pdb_id+'_'+mapping[pdb_id][chain1]+'_'+pdb_id+'_'+mapping[pdb_id][chain2]
	associated_pair_alter=pdb_id+'_'+mapping[pdb_id][chain2]+'_'+pdb_id+'_'+mapping[pdb_id][chain1]
	pred=open(pred_file)
	line2=pred.readline()[:-1]
	while line2:
		#print (associated_pair)
		if line2==associated_pair or line2== associated_pair_alter:
			pred_contact=int(pred.readline()[:-1])
			pdockq1=float(pred.readline()[:-1])
			pdockq2=float(pred.readline()[:-1])
			ptm_iptm=round(float(pred.readline()[:-1]),3)
		line2=pred.readline()[:-1]
	
	print (pdb_id, chain1,chain2,obs_contact,pred_contact,pdockq1,pdockq2,ptm_iptm)
		
	
