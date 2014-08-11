from __future__ import print_function
import os 
import sys
from py2gcode import gcode_cmd
from py2gcode import cnc_dxf

feedrate = 30.0

prog = gcode_cmd.GCodeProg()
prog.add(gcode_cmd.GenericStart())
prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.FeedRate(feedrate))

param = { 
        'fileName'    : 'sensor_mount_holes.dxf',
        'dxfTypes'    : ['CIRCLE'],
        'startZ'      : 0.0,
        'stopZ'       : -0.4,
        'safeZ'       : 0.5,
        'stepZ'       : 0.02,
        'startDwell'  : 2.0,
        }
drill = cnc_dxf.DxfDrill(param)
prog.add(drill)


prog.add(gcode_cmd.RapidMotion(x=10.0,y=0.0,z=2.0))

prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.End(),comment=True)
baseName, dummy = os.path.splitext(__file__)
fileName = '{0}.ngc'.format(baseName)
print('generating: {0}'.format(fileName))
prog.write(fileName)
