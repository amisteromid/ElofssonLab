import os
import json
import shutil


### change the parent_dir and new_dir
### it will extract the best Alphafold model along with its ptm score, pkl file and pdb file


# set the path to the parent directory containing all the subdirectories
parent_dir = "/proj/berzelius-2021-29/users/x_omimo/output/pairs"

# set the path to the new directory where you want to copy the files
new_dir = "/proj/berzelius-2021-29/users/x_omimo/output/extracted_pairs"


# loop through all subdirectories in the parent directory
for subdir in os.listdir(parent_dir):
    sub_path = os.path.join(parent_dir, subdir)

    # check if the subdirectory is actually a directory
    if os.path.isdir(sub_path):
        # set the path to the ranking_debug.json file
        json_path = os.path.join(sub_path, "ranking_debug.json")

        # check if the ranking_debug.json file exists in the subdirectory
        if os.path.exists(json_path):
            # open the ranking_debug.json file and load its contents as a dictionary
            with open(json_path, "r") as f:
                data = json.load(f)

            # get the model with the highest value in the dictionary
            name=max(data['iptm+ptm'],key=data['iptm+ptm'].get)
            score=data['iptm+ptm'][name]
            model=int(name.split('_')[1])
            
            # get the names of the pdb and pkl files based on the key
            pdb_file = 'unrelaxed_model_%d_multimer_v3_pred_0.pdb'%model
            pkl_file = 'result_model_%d_multimer_v3_pred_0.pkl'%model
            
            # set the paths to the pdb and pkl files
            pdb_path = os.path.join(sub_path, pdb_file)
            pkl_path = os.path.join(sub_path, pkl_file)
            
            # check if the pdb and pkl files exist in the subdirectory
            if os.path.exists(pdb_path) and os.path.exists(pkl_path):
                # create the new directory if it doesn't already exist
                if not os.path.exists(new_dir):
                    os.mkdir(new_dir)
                os.mkdir(new_dir+'/'+subdir)
                
                # copy the pdb and pkl files to the new directory
                shutil.copy(pdb_path, os.path.join(new_dir+'/'+subdir, pdb_file))
                shutil.copy(pkl_path, os.path.join(new_dir+'/'+subdir, pkl_file))
                with open(new_dir+'/'+subdir+'/'+'ptm.txt','w') as s:
                    s.write(str(score))

