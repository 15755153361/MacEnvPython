import numpy as np; np.random.seed(0)
import seaborn as sns; sns.set()
import time
uniform_data = np.random.rand(10,12)
ax = sns.heatmap(uniform_data)
time.sleep(6)
