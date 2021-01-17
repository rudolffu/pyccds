#!/usr/bin/env bash
BASEDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
SRCDIR=$BASEDIR/src
python $SRCDIR/ccdsmakezero.py
python $SRCDIR/ccdsccdotz.py
python $SRCDIR/ccdsmakeflat.py
python $SRCDIR/ccdsmakereflat.py
python $SRCDIR/ccdsdivideflat.py
python $SRCDIR/ccdsremovecr.py
python $SRCDIR/ccdsdoapall.py
python $SRCDIR/ccdsidentlamp.py
python $SRCDIR/ccdswavecal.py
