from pymol import cmd

cmd.fetch('5le5')
cmd.remove('not polymer.protein')
#cmd.remove('5le5 and not chain C and not chain I and not chain J')
cmd.remove('5le5 and not chain G and not chain B and not chain A and not chain I and not chain H')
#cmd.remove('5le5 and not chain N and not chain G and not chain A and not chain B and not chain C and not chain D and not chain E and not chain F and not chain H and not chain I and not chain J and not chain K and not chain L and not chain M')
#cmd.load('~/Desktop/5LE5_predictions/extracted_5le5_trimers/IJC/unrelaxed_model_5_multimer_v3_pred_3.pdb')
cmd.load('~/Desktop/5LE5_predictions/5LE5_5_merA_noTMP/ranked_0_NOTMP.pdb')
import supermultimer
supermultimer.supermultimer('ranked_0_NOTMP', '5le5',verbose=True)
#cmd.align('5le5 and chain H', 'unrelaxed_model_4_multimer_v3_pred_1 and chain C', cycles=0, transform=0, object= 'aln' )
#cmd.rms_cur('5le5 and chain H and aln', 'unrelaxed_model_4_multimer_v3_pred_1 and chain C and aln', matchmaker=-1)
