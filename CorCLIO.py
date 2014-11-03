import numpy as np
import scipy as sp
from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.metrics.cluster import mutual_info_score
from scipy.stats import pearsonr

from os import makedirs
from os.path import isdir, exists
from sys import exit
from optparse import *

parser=OptionParser(usage="Computing MIC and PearsonR with a given data", version="1.000")
parser.add_option("-f","--filename", action="store", type="string", default="NoFile", help="Input data file; Default is NoFile")
#parser.add_option("-o","--output-dir", action="store", type="string", default="output", help="Output directory; Default is output")
parser.add_option("-i","--input-dir", action="store", type="string", default=".", help="Input directory; Default is .")
parser.add_option("-s","--time-shift", action="store", type="int", default="0", help="Time-shift")

(opts,files)=parser.parse_args()
filename   = '.'.join(((opts.filename.split('/'))[-1].split('.'))[:-1])
input_dir = opts.input_dir
input_file = input_dir+'/'+opts.filename
#output_dir = opts.output_dir
ts=opts.time_shift


f=np.loadtxt(input_dir+'/'+filename+'.txt')


print 'Correlation Comparision for '+filename

if ts == 0:
    print 'Correlation Indices for NO time-shifted between SEIS and CLIO_GW:'
    print 'PearsonR =', pearsonr(f.T[0],f.T[1])
    print 'Normalized MIC =', normalized_mutual_info_score(f.T[0],f.T[1])

else:
    print 'Correlation Indices for '+ts+'sec. time-shifted between SEIS and CLIO_GW:'
    print 'PearsonR =', pearsonr(f.T[0][ts:],f.T[1][:-ts])
    print 'Normalized MIC =', normalized_mutual_info_score(f.T[0][ts:],f.T[1][:-ts])

print 'ALL JOBS DONE!'
