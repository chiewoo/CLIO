import numpy as np
import scipy as sp
from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.metrics.cluster import mutual_info_score
from scipy.stats import pearsonr

f=np.loadtxt('1034657674_scatter_maxPearson_norm.txt')
g=np.loadtxt('1034657674_scatter_norm.txt_maxMIC.txt')

print 'Correlation Comparision for 1034657674_scatter_maxPearsonR_norm.txt'

print 'Correlation Indices for NO time-shifted between SEIS and CLIO_GW:'
print 'PearsonR =', pearsonr(f.T[0],f.T[1])
print 'Normalized MIC =', normalized_mutual_info_score(f.T[0],f.T[1])


print 'Correlation Indices for 5s time-shifted between SEIS and CLIO_GW:'
print 'PearsonR =', pearsonr(f.T[0][5:],f.T[1][:-5])
print 'Normalized MIC =', normalized_mutual_info_score(f.T[0][5:],f.T[1][:-5])

print 'Correlation Indices for 11s time-shifted between SEIS and CLIO_GW:'
print 'PearsonR =', pearsonr(f.T[0][11:],f.T[1][:-11])
print 'Normalized MIC =', normalized_mutual_info_score(f.T[0][11:],f.T[1][:-11])

print 'Correlation Comparision for 1034657674_scatter_norm.txt_maxMIC.txt'

print 'Correlation Indices for NO time-shifted between SEIS and CLIO_GW:'
print 'PearsonR =', pearsonr(g.T[0],g.T[1])
print 'Normalized MIC =', normalized_mutual_info_score(g.T[0],g.T[1])


print 'Correlation Indices for 5s time-shifted between SEIS and CLIO_GW:'
print 'PearsonR =', pearsonr(g.T[0][5:],g.T[1][:-5])
print 'Normalized MIC =', normalized_mutual_info_score(g.T[0][5:],g.T[1][:-5])

print 'Correlation Indices for 11s time-shifted between SEIS and CLIO_GW:'
print 'PearsonR =', pearsonr(g.T[0][11:],g.T[1][:-11])
print 'Normalized MIC =', normalized_mutual_info_score(g.T[0][11:],g.T[1][:-11])


print 'ALL JOBS DONE!'
