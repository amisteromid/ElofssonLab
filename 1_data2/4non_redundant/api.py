import requests
from sys import argv
import pandas as pd
import numpy as np


# python3 api.py ../3hetero4PLUS/final_comp.txt


def get_similar_ids(pdb_id):
    # write the query using the PBD ID passed as input to this function
    my_query = '''
{
  "query": {
    "type": "terminal",
    "service": "structure",
    "parameters": {
      "operator": "strict_shape_match",
      "value": {
        "entry_id": "%s",
        "assembly_id": "1"
      }
    }
  },
  "return_type": "assembly",
  "request_options": {
    "paginate": {
      "start": 0,
      "rows": 25
    },
    "results_content_type": [
      "experimental"
    ],
    "sort": [
      {
        "sort_by": "score",
        "direction": "desc"
      }
    ],
    "scoring_strategy": "combined"
  }
}
''' % pdb_id

    r = requests.get('https://search.rcsb.org/rcsbsearch/v2/query?json=%s' % requests.utils.requote_uri(my_query))
    j = r.json()
    return (j['result_set'])

def get_resolution(pdb):
	a=requests.get('https://data.rcsb.org/rest/v1/core/entry/%s'%pdb)
	a=a.json()
	return a['pdbx_vrpt_summary']['pdbresolution']


if __name__ == "__main__":
	pdb_ids = argv[1]
	pdb_ids,chain_counts = np.loadtxt(pdb_ids, delimiter=',', usecols=(0, 1), unpack=True, dtype=np.str)
	pdb_ids = dict(zip(pdb_ids, chain_counts))
	
	
	final_pdb_ids={}
	redundants=[]
	
	for pdb_id in pdb_ids:
		if pdb_id not in redundants:
			try:                                         # sometimes we have NMR structures with no resolution
				tmp={pdb_id: get_resolution(pdb_id)}
			except:
				tmp={pdb_id: 5}
			print (pdb_id)
			similars = get_similar_ids(pdb_id)
			for similar in similars: 
				if similar['score']>0.15:
					try:
						tmp[similar['identifier'][:-2]]=get_resolution(similar['identifier'][:-2])
					except:
						tmp[similar['identifier'][:-2]]=5

			chosen = min(tmp, key=tmp.get)
			while chosen not in pdb_ids:       # sometimes the similar one is not even in our all-homologous pdb list
				del tmp[chosen]
				chosen = min(tmp, key=tmp.get)
			final_pdb_ids[chosen] = pdb_ids[chosen]

			for each in tmp:
				redundants.append(each)
					
	with open("final_final.txt", 'w') as f: 
		for key, value in final_pdb_ids.items(): 
			f.write('%s,%s\n' % (key, value))
















