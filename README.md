# Elofsson-Lab
My master thesis at SciLifeLab in Stockholm under the supervision of Prof. Arne Elofsson


![DynamicGT concept workflow]()

## _**Abstract**_
Protein complexes consist of two or more polypeptide chains. However, predicting the entire complex and the order of chains poses a challenge. In some cases, the complexes are too large to be processed by structure prediction software like AlphaFold. Additionally, when chains are homologous (having a common evolutionary origin), the software struggles to distinguish between them.

In this project, we aimed to generate predictions for all possible pairs of chains (dimers) within protein structures. Subsequently, we developed a model to classify interacting and non-interacting pairs, enabling us to progressively construct the complete complex in the correct order.

Our model focuses on the human 20s Proteasome protein complex (PDB ID:5LE5), which consists of 14 distinct chains.

## Dataset
The dataset is sourced from the PDB database and comprises 298 protein complexes. Each complex contains only homologous chains, which can range from 2 to 14 types. By considering all possible combinations of pairs within the complexes, we generated 1400 pairs and predicted their structures and interactions using AlphaFold-multimer.

For each prediction, three types of data were extracted:
1. Scores indicating the confidence of the structure and interaction.
2. Information about the residues involved in the interaction (the binding mode/interface of each chain in the dimer).
3. The quality of the prediction, measuring the similarity between the predicted and actual pairs for interacting pairs.

### Challenge
Our target variable is the number of residues in contact for the actual pairs. The number of residues in contact indicates the proximity and interaction between the chains. Determining how many residues are sufficient for a pair to be considered interacting is challenging, as it depends on multiple factors. A constant number cannot be universally applied to all complexes.

## **Workflow** 
### Data processing and filtering. 
1. Redundancy was eliminated using the PDB filter.
2. Scores irrelevant to interaction classification are removed.
3. The train-test split was performed based on structures rather than pairs. This approach prevents learning leakage from pairs in the training set that belong to the same structure as pairs in the test set.
4. Scaling/Normalization: Various scaling and normalization techniques were examined, as outlined below:
    1. A MinMax scale was fit to the training data and applied to both the training and test sets.
    2. The MinMax scale was applied to pairs within each structure individually, where each structure has its maximum and minimum values.
    3. The MinMax scale was applied within each structure, but the scores were ranked before scaling. This approach neutralizes differences, ensuring that scores such as 0.1, 0.2, and 0.8 are considered equivalent to 0.8, 0.9, and 0.91.
    
  >*Among these approaches, the third method demonstrated the best performance.*


### Model building 
Due to the challenge of using a continuous, non-binary target variable for binary classification, both classification and regression models were explored:
1. A threshold of a minimum of 10 residues was set to classify pairs as interacting. This threshold was chosen based on the specific context of the human 20s proteasome, which is the final goal of the project. The target variable "obs_contact" was converted to binary form.
2. A two-step approach was implemented:
    1. Unsupervised clustering, along with the elbow method, was utilized on the information about residues involved in interaction (interface residues) to group the pairs.
    2. A regression model was created without converting the target variable to binary, yielding a final score indicating the likelihood of a pair being classified as interacting.
 
  Finally, the regression model was used to rank the pairs within each cluster. The first-ranked pair was classified as interacting, while the others were classified as non-interacting.
>*The second approach demonstrated the best performance*

### Conclusion.
The final results aim to address the following questions: 
1. Can we construct the interaction graph of the complex based on pairwise predictions?
2. Does this interaction graph accurately represent the correct structure?

