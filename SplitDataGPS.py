import numpy as np

from os import makedirs
from os.path import isdir, exists
from sys import exit
from optparse import *

parser=OptionParser(usage="Data Split by GPS time", version="1.000")
parser.add_option("-f","--filename", action="store", type="string", default="NoFile", help="Input data file; Default is NoFile")
parser.add_option("-o","--output-dir", action="store", type="string", default="output", help="Output directory; Default is output")   
parser.add_option("-i","--input-dir", action="store", type="string", default=".", help="Input directory; Default is .")
parser.add_option("-s","--split-time", action="store", type="int", default="0", help="Split time interval")

(opts,files)=parser.parse_args()
filename = opts.filename
fname   = '_'.join(opts.filename.split('.')[0].split('_')[:-4])
input_dir = opts.input_dir
input_file = input_dir+'/'+opts.filename
output_dir = opts.output_dir                                                                                                          
dt=opts.split_time

if isdir(output_dir):
    print "Directory exists:", output_dir
else:
    print "Creating directory:", output_dir
    makedirs(output_dir)

samp=2048 # sampling rate = 2048Hz

f=np.loadtxt(input_dir+'/'+filename+'.txt')

print 'Splitting data by 1 sec........'

g=open(output_dir+'/'+fname+'_SEI_1s.txt','a')
l=open(output_dir+'/'+fname+'_GW_1s.txt','a')

for i in range(len(f)/samp):
    temp=f.T[0][dt*i*samp:samp+samp*i*dt]
    temp2=f.T[1][dt*i*samp:samp+samp*i*dt]
    for j in range(samp):
        if j==(samp-1):
            g.write(str(temp[j]))
            g.write('\n')
            l.write(str(temp2[j]))
            l.write('\n')
        else:
            g.write(str(temp[j]))
            g.write(' ')
            l.write(str(temp2[j]))
            l.write(' ')
g.close()
l.close()

print 'ALL Jobs done!'
