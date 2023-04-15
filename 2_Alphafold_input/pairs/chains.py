from sys import argv
import pandas as pd

#f = argv[1]
f = 'report.csv'
f = pd.read_csv(f)
f.fillna(method='ffill',inplace = True)
#raw_report = raw_report.set_index('Entry ID')
print (f.columns)


chain_dic = {}
uniques={}
for ID,info in f.iterrows():
      entry = f.loc[ID,'Entry ID']
      if entry not in chain_dic:
            if f.loc[ID,'Entity Polymer Type']=='Protein':
                  uniques[entry]=[f.loc[ID,'Entity ID']]
                  chain_dic[entry]=[f.loc[ID,'Auth Asym ID']]
      else:
            if f.loc[ID,'Entity Polymer Type']=='Protein' and f.loc[ID,'Entity ID'] not in uniques[entry]:
                  uniques[entry].append(f.loc[ID,'Entity ID'])
                  chain_dic[entry].append(f.loc[ID,'Auth Asym ID'])

#print (len(chain_dic['5LE5']))

output=open('output_pairs.txt','w')
for i in chain_dic:
      for c1 in range(len(chain_dic[i])):
            for c2 in range(c1,len(chain_dic[i])):
                  output.write(i+':'+chain_dic[i][c1]+'/'+chain_dic[i][c2]+'\n')
output.close()
                  
