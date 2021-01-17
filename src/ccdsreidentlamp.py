#!/usr/bin/env python
import glob
from pyraf import iraf
from astropy.io import fits
import json
import os
import sys
from shutil import copy2
import re

CWD = os.getcwd()
dbpath = os.path.join(os.path.dirname(sys.argv[0]), '../database')

with open('myccds.json') as file:
    settings = json.loads(file.read())
side = settings['mysettings']['side']
if side == "Blue":
    print("Settings for blue will be used.")
    lamplist = [os.path.basename(x) for x in glob.glob(
        dbpath + '/nehgne*fits')]
elif teles == "Red":
    print("Settings for red will be used.")
    lamplist = [os.path.basename(x) for x in glob.glob(
        dbpath + '/arxe*fits')]
else:
    print("Error detected.")

print('Possible lamp spectrum(a) for references:\n' +
      ", ".join(p for p in lamplist))
refspec = str(
    raw_input("Enter filename of the lamp spectrum you want to use: "))
refspec1 = re.sub('\.fits$', '', refspec)+".fits"
copy2(dbpath + '/' + refspec1, CWD)
copy2(dbpath + '/id' + re.sub('\.fits$', '', refspec), CWD + '/database')
iraf.onedspec()
iraf.onedspec.reidentify.unlearn()
# iraf.onedspec.reidentify.fwidth = 10
iraf.onedspec.reidentify.coordli = 'linelists$henear.dat'
iraf.onedspec.reidentify(reference=refspec1,
                         images='af*fits')

iraf.onedspec.identify.unlearn()
iraf.onedspec.identify.fwidth = 10
iraf.onedspec.identify.coordli = 'linelists$henear.dat'
iraf.onedspec.identify(images='af*fits')
print('---DONE---')
