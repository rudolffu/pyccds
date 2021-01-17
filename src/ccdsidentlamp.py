#!/usr/bin/env python
import glob
from pyraf import iraf
from astropy.io import fits
import json

iraf.onedspec()
iraf.onedspec.identify.unlearn()
iraf.onedspec.identify.fwidth = 10
with open('myccds.json') as file:
    settings = json.loads(file.read())
side = settings['mysettings']['side']
if side == "Blue":
    iraf.onedspec.identify.coordli = 'linelists$henear.dat'
elif side == "Red":
    iraf.onedspec.identify.coordli = 'linelists$xenon_ccds.dat'
else:
    print("Error detected.")
iraf.onedspec.identify(images='af*fits')
