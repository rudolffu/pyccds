#!/usr/bin/env python
import glob
from pyraf import iraf
from astropy.io import fits
import json
import sys
import os
import re

basepath = os.path.dirname(sys.argv[0])
myonedstds = os.path.join(basepath, '../iraf_data/onedstds')
with open('myccds.json') as file:
    settings = json.loads(file.read())
side = settings['mysettings']['side']
if side == "Blue":
    midname = 'blue'
elif side == "Red":
    midname = 'red'
else:
    print("Error detected.")

extinct = 'onedstds$kpnoextinct.dat'
inputlist = glob.glob('a*fits')

iraf.twodspec()
iraf.twodspec.longslit()
print('Copy to onedspec...')
iraf.twodspec.longslit.scopy.unlearn()
olist3 = glob.glob('J*MDM_b.fits')
for obj in olist3:
    objind = str(olist3.index(obj) + 1)
    objname = re.sub('\.fits$', '', obj) + '_' + "CCDS"
    iraf.twodspec.longslit.scopy(input=obj, output=objname, bands=1,
                                 format='onedspec')
print('---DONE---')
