#!/usr/bin/env python
import glob
from pyraf import iraf
from astropy.io import fits
import json
import os
import sys
from shutil import copy2
import re
import glob

CWD = os.getcwd()
dbpath = os.path.join(os.path.dirname(sys.argv[0]), '../database')
basepath = os.path.dirname(sys.argv[0])
linepath = os.path.join(basepath, '../iraf_data/linelists/')

with open('myccds.json') as file:
    settings = json.loads(file.read())
side = settings['mysettings']['side']
# if side == "Blue":
#     print("Settings for blue will be used.")
#     lamplist = [os.path.basename(x) for x in glob.glob(
#         dbpath + '/nehgne*fits')]
# elif teles == "Red":
#     print("Settings for red will be used.")
#     lamplist = [os.path.basename(x) for x in glob.glob(
#         dbpath + '/arxe*fits')]
# else:
#     print("Error detected.")
lamplist_a = [os.path.basename(x) for x in glob.glob(
    dbpath + '/arxe*fits')]
lamplist_b = [os.path.basename(x) for x in glob.glob(
    dbpath + '/nehgne*fits')]

print('Possible ArXe lamp spectrum(a) for references:\n' +
      ", ".join(p for p in lamplist_a))
refspec_ain = str(
    raw_input("Enter filename of the lamp spectrum you want to use: "))
refspec_a = re.sub('\.fits$', '', refspec_ain)+".fits"
copy2(dbpath + '/' + refspec_a, CWD)
copy2(dbpath + '/id' + re.sub('\.fits$', '', refspec_ain), CWD + '/database')

print('Possible nehgne lamp spectrum(a) for references:\n' +
      ", ".join(p for p in lamplist_b))
refspec_bin = str(
    raw_input("Enter filename of the lamp spectrum you want to use: "))
refspec_b = re.sub('\.fits$', '', refspec_bin)+".fits"
copy2(dbpath + '/' + refspec_b, CWD)
copy2(dbpath + '/id' + re.sub('\.fits$', '', refspec_bin), CWD + '/database')

iraf.onedspec()
iraf.onedspec.reidentify.unlearn()
# iraf.onedspec.reidentify.fwidth = 10

iraf.onedspec.identify.unlearn()
iraf.onedspec.identify.fwidth = 10

onedlamps = glob.glob("af*fits")
for lamp in onedlamps:
    lname = fits.getheader(lamp)['OBJECT']
    if lname == "ArXe":
        iraf.onedspec.reidentify.coordli = linepath+'argon.dat'
        iraf.onedspec.identify.coordli = linepath+'argon.dat'
        ref = refspec_a
    elif lname == "NeHgNe":
        iraf.onedspec.reidentify.coordli = linepath+'hgne.dat'
        iraf.onedspec.identify.coordli = linepath+'hgne.dat'
        ref = refspec_b
    else:
        print("Lamp object name not understood.")
    iraf.onedspec.reidentify(reference=ref,
                             images=lamp)
    iraf.onedspec.identify(images=lamp)