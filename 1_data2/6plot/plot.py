import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sys import argv


f = argv[1]
pdb,count=np.loadtxt(f, delimiter=',', usecols=(0, 1), unpack=True, dtype=str)
count = [float(x) for x in count if float(x)<75]

ax = sns.violinplot(x=list(map(lambda a: float(a),count)))
plt.show()
