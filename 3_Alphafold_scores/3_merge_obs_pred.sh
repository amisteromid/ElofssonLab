
source myenv/bin/activate
echo 'pdb_id,chain1,chain2,obs_contact,pred_contact,pdockq1,pdockq2,ptm_iptm' >> result.txt
for pdb in /proj/berzelius-2021-29/users/x_omimo/contacts/*; do
	echo $pdb
	python3 merge_obs_pred.py $pdb/predicted.txt $pdb/observed.txt contacts/chain_map.json >> result.txt
done
