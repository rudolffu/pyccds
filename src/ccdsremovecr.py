#!/usr/bin/env python
import glob
from pyraf import iraf
import multiprocessing as mp
import sys
import os
import json

basepath = os.path.dirname(sys.argv[0])
lacos_im = os.path.join(basepath, '../iraf_tasks/lacos_im.cl')

# with open('myccds.json') as file:
#     settings = json.loads(file.read())
# side = settings['mysettings']['side']

gain = 1.5
readnoise = 3.5

objall = []
with open('objall.list') as file:
    for line in file:
        line = line.strip('.fits\n')
        objall.append(line)


iraf.task(lacos_im=lacos_im)
print('Loading IRAF packages ...')
iraf.stsdas()
iraf.lacos_im.gain = gain
iraf.lacos_im.readn = readnoise


def rmcrimg(obj):
    iraf.lacos_im(input='f_' + obj, output='crf_' + obj,
                  outmask='mask' + obj,
                  sigclip=4.5,
                  niter=4,
                  verbose='No')
    print(obj + ' finished.')


pool = mp.Pool(1)
pool.map(rmcrimg, objall)
