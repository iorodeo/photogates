from __future__ import print_function
import os 
import sys
from py2gcode import gcode_cmd
from py2gcode import cnc_dxf

if len(sys.argv) < 2:
    fileName = 'body_in.dxf'
else:
    fileName = sys.argv[1]

feedrate = 50.0

prog = gcode_cmd.GCodeProg()
prog.add(gcode_cmd.GenericStart())
prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.FeedRate(feedrate))

param = { 
        'fileName'    : fileName,
        'layers'      : ['drill_4-40_tap'],
        'dxfTypes'    : ['CIRCLE'],
        'startZ'      : 0.00,
        'stopZ'       : -0.3,
        'safeZ'       : 0.3,
        'stepZ'       : 0.02,
        'startDwell'  : 0.5,
        }
drill = cnc_dxf.DxfDrill(param)
prog.add(drill)

prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.End(),comment=True)
baseName, dummy = os.path.splitext(__file__)
fileName = '{0}.ngc'.format(baseName)
print('generating: {0}'.format(fileName))
prog.write(fileName)
