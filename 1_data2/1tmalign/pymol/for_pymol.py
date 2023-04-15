from tmalign import tmalign
from sys import argv


# ignores the chains with less than 10 residues
# stops calculating the scores for following pairs if any of them goes below 0.4
# Stops when find a chain longer than 2000 residues (this code is added after PDB entry 6JIU)


pdb = argv[3]
cmd.fetch(pdb)
scores = []
cmd.remove("byres polymer and name P")  # to remove any nucleotide chain
cmd.remove("not polymer")  # to remove not polymer
chains= cmd.get_chains(pdb)

too_long_chain = False
error = False
kill = False
for ch1 in range(len(chains)-1):
	if len(cmd.get_model("%s and chain %s" %(pdb,chains[ch1])).get_residues()) > 2000:
		error = True
		too_long_chain = True
		break
	for ch2 in range(ch1+1, len(chains)):
		if len(cmd.get_model("%s and chain %s" %(pdb,chains[ch1])).get_residues()) < 10\
		or len(cmd.get_model("%s and chain %s" %(pdb,chains[ch2])).get_residues()) < 10:
			continue
		try:
			s = tmalign("%s and chain %s" %(pdb,chains[ch1]),"%s and chain %s" %(pdb,chains[ch2]))
			scores.append(s)
			if s<0.4:
				kill = True
				break
		except:
			error = True
			kill = True
			break
	if kill == True:
		break

if error == True:
	if too_long_chain == True:
		f = open('scilifelab.txt','a')
		f.write(pdb+','+'too_long'+'\n')
		f.close()
	else:
		f = open('scilifelab.txt','a')
		f.write(pdb+','+'error'+'\n')
		f.close()
else:
	f = open('scilifelab.txt','a')
	f.write(pdb+','+str(min(scores))+'\n')
	f.close()
