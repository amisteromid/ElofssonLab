#!/usr/bin/env python3

import sys
import numpy as np
import argparse
import re
from Bio.PDB import PDBIO
from Bio.PDB.MMCIFParser import MMCIFParser
from Bio.PDB.PDBParser import PDBParser


# Ny version
#m = np.sqrt(np.sum((a[:,np.newaxis,:] -a[np.newaxis,:,:])**2, axis=2))
#n=np.where(m<=6.0)

#mat = np.append(chi_coords,chj_coords,axis=0)
#a_min_b = (mat[:,np.newaxis,:] -mat[np.newaxis,:,:])
#dists = np.sqrt(np.sum(a_min_b.T ** 2, axis=0))
#contact_dists = dists[l1:,:l1]
#t=8
#contacts = np.argwhere(contact_dists<=t)


def structtonumpy(structure):
    chains={}
    chain_ids=[]
    for model in structure:
        for chain in model:
            ch=chain.get_id()
            chain_ids+=[ch]
            chains[ch] = []
            for residue in chain:
                try:
                    x,y,z=residue['CB'].get_vector()
                    chains[ch].append([x,y,z])
                except:
                    try:
                        x,y,z=residue['CA'].get_vector()
                        chains[ch].append([x,y,z])
                    except:
                        try:
                            x,y,z=residue['N'].get_vector()
                            chains[ch].append([x,y,z])
                        except:
                            i=0
    return (chains,chain_ids)
                

#popt=[7.07140240e-01, 3.88062162e+02, 3.14767156e-02, 3.13182907e-02]

arg_parser = argparse.ArgumentParser(description="Finds conctacts between chains")
group = arg_parser.add_mutually_exclusive_group(required=True)
group.add_argument("-p","--pdb",type=argparse.FileType('r'),help="Input pdb file pLddt values in bfactor columns")
group.add_argument("-c","--cif",type=argparse.FileType('r'),help="Input cif file plddt values in bfactor columns")
arg_parser.add_argument("-v","--verbose", action='store_true', required=False,help="pritn list")
arg_parser.add_argument("-C","--cutoff", type=float,required=False,default=8.0,help="Cutoff for defining distances")
args = arg_parser.parse_args()
cutoff=args.cutoff

args = arg_parser.parse_args()
cutoff=args.cutoff
#cutoff2=3
Name=""
if (args.cif):
    name=args.cif.name
    bio_parser = MMCIFParser()
    structure_file = args.cif
    structure_id = args.cif.name[:-4]
    structure = bio_parser.get_structure(structure_id, structure_file)
        
elif (args.pdb):
    name=args.pdb.name
    bio_parser = PDBParser()
    structure_file = args.pdb
    structure_id = args.pdb.name[:-4]
    structure = bio_parser.get_structure(structure_id, structure_file)

    
CHAINS,IDS=structtonumpy(structure)
#m = np.sqrt(np.sum((CA[:,np.newaxis,:] -CA[np.newaxis,:,:])**2, axis=2))
#n=np.where(m<=cutoff)
#print (len(CHAINS),len(IDS))
#print (CHAINS,IDS)
#print ("Ch1,Ch2,NumContacts")
for n1,i in enumerate(IDS):
    for n2,j in enumerate(IDS):
        if ( j != i) and n2>n1:
            #Get interface
            coords1, coords2 = np.array(CHAINS[i]), np.array(CHAINS[j])
            #Check total length
            #Calc 2-norm
            mat = np.append(coords1, coords2,axis=0)
            a_min_b = mat[:,np.newaxis,:] -mat[np.newaxis,:,:]
            dists = np.sqrt(np.sum(a_min_b.T ** 2, axis=0)).T
            l1 = len(coords1)
            l2 = len(coords2)
            contact_dists = dists[:l1,l1:]
            contacts = np.argwhere(contact_dists<=cutoff)
            if name.count('_')>2: i= name.split('_')[1];j= name.split('_')[3].split('/')[0]; print (len(contacts))
            else: print (str(i)+","+str(j)+","+str(len(contacts)))
            if (args.verbose):
                #print (contacts)
                print("Name,Res1,Res2,Length1,Length2")
                for x in contacts:
                    print (structure_id,",",x[0],",",x[1],",",l1,",",l2)
