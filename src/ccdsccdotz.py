#!/usr/bin/env python
# Load Python standard modules
import glob
import os
import shutil
from pyraf import iraf
import json

with open('myccds.json') as file:
    settings = json.loads(file.read())

side = settings['mysettings']['side']


print('Loading IRAF packages ...')
iraf.imred()
iraf.ccdred()

print('unlearning previous settings...')
iraf.ccdred.unlearn()
iraf.ccdred.ccdproc.unlearn()

print('Applying Bias, Overscan and pre Trimming...')
iraf.ccdred.ccdproc.ccdtype = ''
iraf.ccdred.ccdproc.noproc = False
iraf.ccdred.ccdproc.fixpix = False
iraf.ccdred.ccdproc.darkcor = False
iraf.ccdred.ccdproc.illumcor = False
iraf.ccdred.ccdproc.fringecor = False
iraf.ccdred.ccdproc.readcor = False
iraf.ccdred.ccdproc.scancor = False
iraf.ccdred.ccdproc.readaxis = 'line'
iraf.ccdred.ccdproc.flatcor = False

if side == "Blue":
    print("Settings for blue side will be used.")
    iraf.ccdred.ccdproc.biassec = '[1205:1230,51:750]'
    iraf.ccdred.ccdproc.trimsec = '[51:960,51:750]'
    iraf.ccdred.ccdproc(images='@flatnall.list', overscan='yes',
                        trim='yes', zerocor='yes', zero='Zero')
elif side == "Red":
    print("Settings for red side will be used.")
    iraf.ccdred.ccdproc.biassec = '[1205:1230,51:750]'
    iraf.ccdred.ccdproc.trimsec = '[11:1180,51:750]'
    iraf.ccdred.ccdproc(images='@flatnall.list', overscan='yes',
                        trim='yes', zerocor='yes', zero='Zero')
else:
    print("Error detected.")

print('--- DONE ---')
