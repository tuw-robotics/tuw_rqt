#!/usr/bin/env python

import sys

from rqt_emergency_stop.emergency_stop import EmergencyStopPlugin
from rqt_gui.main import Main

plugin = 'rqt_emergency_stop'
main = Main(filename=plugin)
sys.exit(main.main(standalone=plugin))
