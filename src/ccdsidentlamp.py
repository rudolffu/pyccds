#!/usr/bin/env python
import glob
from pyraf import iraf
from astropy.io import fits
import json
import sys
import os
import glob

basepath = os.path.dirname(sys.argv[0])
linepath = os.path.join(basepath, '../iraf_data/linelists/')

iraf.onedspec()
iraf.onedspec.identify.unlearn()
iraf.onedspec.identify.fwidth = 10
with open('myccds.json') as file:
    settings = json.loads(file.read())
side = settings['mysettings']['side']
# if side == "Blue":
#     iraf.onedspec.identify.coordli = 'linelists$henear.dat'
# elif side == "Red":
#     iraf.onedspec.identify.coordli = 'linelists$xenon_ccds.dat'
# else:
#     print("Error detected.")
onedlamps = glob.glob("af*fits")
onedarxe = []
onednehgne = []
for lamp in onedlamps:
    lname = fits.getheader(lamp)['OBJECT']
    if lname == "ArXe":
        onedarxe.append(lamp)
    elif lname == "NeHgNe":
        onednehgne.append(lamp)
    else:
        print("Lamp object name not understood.")

for lamp in onedarxe:
    iraf.onedspec.identify.coordli = linepath+'argon.dat'
    iraf.onedspec.identify(images=lamp)

for lamp in onednehgne:
    iraf.onedspec.identify.coordli = linepath+'hgne.dat'
    iraf.onedspec.identify(images=lamp)
