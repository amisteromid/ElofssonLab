from pymol import cmd

def check_identical(seq1, seq2):
	if len(seq1) != len(seq2): return False
	for i in range(len(seq1)):
		if seq1[i] != seq2[i]:
			if seq1[i] != '?' and seq2[i] != '?' :
				return False
	return True

def supermultimer(target,mobile,verbose=False):
	rmsds=[]
	# Get the sequence of each chain
	seq_dict = {}
	for obj in [target,mobile]:
		for chain in cmd.get_chains(obj):
			seq = cmd.get_fastastr(f"{obj} and chain {chain}").split('\n')[1:]
			remained=True
			seq = ''.join(seq)
			if len(seq_dict) == 0:
				seq_dict[seq] = []
				seq_dict[seq].append(f"{obj} and chain {chain}")
				remained = False
			else:
				for s in seq_dict:
					if check_identical(s,seq) and remained:
						seq_dict[s].append(f"{obj} and chain {chain}")
						remained = False
				if remained == True:
					seq_dict[seq] = []
					seq_dict[seq].append(f"{obj} and chain {chain}")
					remained = False

	# Color the chains based on their sequence
	color_list = ['red', 'blue', 'white', 'orange', 'forest', 'yellow', 'purple', 'pink', 'gray70','slate', 'sand', 'dirtyviolet']
	for i, seq in enumerate(seq_dict.keys()):
		color = color_list[i % len(color_list)]
		for sel in seq_dict[seq]:
			cmd.color(color, sel)
	for i, seq in enumerate(seq_dict.keys()):
		if len(seq_dict[seq])>1:
			cmd.super(seq_dict[seq][0],seq_dict[seq][1])
			break
	for i, seq in enumerate(seq_dict.keys()):
		if len(seq_dict[seq])==1:
			if verbose == True:
				print ('%s counterpart does not exist'%seq_dict[seq][0])
			else:
				return
		else:
			cmd.super(seq_dict[seq][0],seq_dict[seq][1], cycles=0, transform=0, object= 'aln%d'%i )[0]
			rmsd=cmd.rms_cur(seq_dict[seq][0]+' and aln%d'%i, seq_dict[seq][1]+' and aln%d'%i, matchmaker=-1)
			rmsds.append(rmsd)
			if verbose == True:
				print ('RMSD of ',seq_dict[seq][0],' & ',seq_dict[seq][1],' is: ',rmsd)
	return max(rmsds)
	
cmd.extend('supermultimer', supermultimer)
