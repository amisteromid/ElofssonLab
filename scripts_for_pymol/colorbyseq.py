from pymol import cmd

def check_identical(seq1, seq2):
	if len(seq1) != len(seq2): return False
	for i in range(len(seq1)):
		if seq1[i] != seq2[i]:
			if seq1[i] != '?' and seq2[i] != '?' :
				return False
	return True

def colorbyseq():
	# Get the sequence of each chain
	seq_dict = {}
	for obj in cmd.get_names():
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

cmd.extend('colorbyseq', colorbyseq)
