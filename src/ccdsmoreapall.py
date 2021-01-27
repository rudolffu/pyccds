#!/usr/bin/env python
import glob
from pyraf import iraf
import json
from sys import argv

objlist = argv[1]

with open('myccds.json') as file:
    settings = json.loads(file.read())
side = settings['mysettings']['side']
if side == "Blue":
    print("Settings for blue side will be used.")
    disp_axis = 1
elif side == "Red":
    print("Settings for red side will be used.")
    disp_axis = 1
else:
    disp_axis = str(raw_input("Dispersion axis: 1 for line; 2 for column."))

print('Loading IRAF packages ...')
iraf.imred()
iraf.ccdred()
iraf.twodspec()
iraf.apextract()

print('unlearning previous settings...')
iraf.ccdred.unlearn()
iraf.ccdred.ccdproc.unlearn()
iraf.ccdred.combine.unlearn()
iraf.apextract.apall.unlearn()
iraf.apextract.dispaxis = disp_axis
iraf.apextract.verbose = 'no'

print('Extracting object aperture spectrum...')
iraf.apextract.apall.unlearn()
iraf.apextract.apall.readnoise = 3.5
iraf.apextract.apall.gain = 1.5
iraf.apextract.apall.format = 'multispec'
iraf.apextract.apall.interac = True
iraf.apextract.apall.find = True
iraf.apextract.apall.recente = True
iraf.apextract.apall.resize = True
iraf.apextract.apall.edit = True
iraf.apextract.apall.trace = True
iraf.apextract.apall.fittrac = True
iraf.apextract.apall.extract = True
iraf.apextract.apall.extras = True
iraf.apextract.apall.review = True
iraf.apextract.apall.background = 'fit'
iraf.apextract.apall.pfit = 'fit2d'
iraf.apextract.apall.weights = 'variance'
iraf.apextract.apall(input='crf_//@'+objlist, output='acrf_//@'+objlist)

print('--- DONE ---')
