from sys import argv
import pandas as pd

# python3 filter.py raw_tm_report.txt


if __name__ == "__main__":
	f = argv[1]
	f = open(f)
	
	filtered= {}
	line = f.readline()
	while line:
		line=line.split(',')
		pdb=line[0]
		score=line[1][:-1]
		print (pdb,score)
		if score not in ['error','too_long']:
			if float(score) > 0.60:
				filtered[pdb]= score
		line = f.readline()
	
	with open("tm_report.txt", 'w') as f: 
		for key, value in filtered.items(): 
			f.write('%s,%s\n' % (key, value))
