import numpy as np
import scipy as sp
from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.metrics.cluster import mutual_info_score
from scipy.stats import pearsonr

f=np.loadtxt('1034657674_scatter_maxPearson_norm.txt')

print 'Correlation Indices between SEIS and CLIO_GW:'
print 'PearsonR =', pearsonr(f.T[0],f.T[1])
print 'Normalized MIC =', normalized_mutual_info_score(f.T[0],f.T[1])

