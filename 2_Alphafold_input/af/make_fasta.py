from sys import argv
import pandas as pd

# python3 make_fasta.py output_pairs.txt report_with_seq.csv

if __name__ == "__main__":
	
	# prepare a dictionary of chains
	pairs = open(argv[1])
	dic={}
	line = pairs.readline()[:-1]
	while line:
		line = line.split('_')
		if line[0] not in dic:
			dic[line[0]]= [line[1]]
			if line[2] not in dic[line[0]]:
				dic[line[0]].append(line[2])
		else:
			if line[1] not in dic[line[0]]:
				dic[line[0]].append(line[1])
			if line[2] not in dic[line[0]]:
				dic[line[0]].append(line[2])
		line = pairs.readline()[:-1]
	print (dic['5LE5'])
	
	
	# extract the sequence of those chains and make a fasta file out of each chain
	report = argv[2]
	report = pd.read_csv(report)
	report.fillna(method='ffill',inplace = True)
	#print (report)
	for ID,info in report.iterrows():
		entry = report.loc[ID,'Entry ID']
		chain = report.loc[ID,'Auth Asym ID']
		seq = report.loc[ID,'Sequence']
		if chain in dic[entry]:
			with open('chains_fasta/'+entry+'_'+chain+'.fasta','w')as f:
				f.write('>'+entry+'_'+chain+'\n')
				f.write(seq)
			
	#extract the sequence of those chains and make a fasta file out of entire chains
	for ID,info in report.iterrows():
		entry = report.loc[ID,'Entry ID']
		chain = report.loc[ID,'Auth Asym ID']
		seq = report.loc[ID,'Sequence']
		if chain in dic[entry]:
			with open('entire_fasta/'+entry+'.fasta','a')as f:
				f.write('>'+entry+'_'+chain+'\n')
				f.write(seq+'\n')
			
	#extract the sequence of those chains and make a fasta file out of pairs of chains
	pairs = open(argv[1])
	line = pairs.readline()[:-1]
	print (line)
	while line:
		line = line.split('_')
		id = line[0]
		first = line[1]
		second = line[2]
		with open('pairs_fasta/'+id+'_'+first+'_'+id+'_'+second+'.fasta','w')as f:
			for each in [first,second]:
				with open('chains_fasta/'+id+'_'+each+'.fasta') as infile:
					f.write(infile.read())
				f.write("\n")
		line = pairs.readline()[:-1]
	
		
			
			
			
			
			
			
			
			
			
			
			
			
