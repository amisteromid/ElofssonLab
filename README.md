# Elofsson-Lab
My master thesis at SciLifeLab in Stockholm

The aim of this project was to develop a method for predicting the interaction graph of large protein complexes with homologous chains, based on AlphaFold multimer. The prediction process involved two general steps.

1) A regression model was used to calculate an overall score indicating the likelihood of a pair of chains interacting. To achieve this, four different tools/scores were employed, including FoldX, pDockQ-v1, pDockQ-v2, and the ptm+iptm score from AlphaFold output.

2) An unsupervised clustering method was utilized to group the interfaces of the predicted protein pairs.
