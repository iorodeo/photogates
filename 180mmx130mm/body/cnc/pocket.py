from __future__ import print_function
import os 
import sys
import dxfgrabber
from py2gcode import gcode_cmd
from py2gcode import cnc_dxf

if len(sys.argv) < 2:
    fileName = 'body_in.dxf'
else:
    fileName = sys.argv[1]

feedrate = 120.0
startZ = 0.0
safeZ = 0.5
toolDiam = 0.25 
overlap = 0.5
overlapFinish = 0.6
maxCutDepth = 0.04
direction = 'ccw'
startDwell = 2.0

prog = gcode_cmd.GCodeProg()
prog.add(gcode_cmd.GenericStart())
prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.FeedRate(feedrate))


# Tube clamp pockets
# Quick cheesy fix as this didn't work with arrayed parts
dwg = dxfgrabber.readfile(fileName)
tubeClampPocketLayers = [x.name for x in dwg.layers if 'tube_clamp_pocket' in x.name]
for layer in tubeClampPocketLayers:
    param = {
            'fileName'       : fileName,
            'layers'         : [layer],
            'depth'          : 0.05,
            'startZ'         : startZ,
            'safeZ'          : safeZ,
            'overlap'        : overlap,
            'overlapFinish'  : overlapFinish,
            'maxCutDepth'    : maxCutDepth,
            'toolDiam'       : toolDiam,
            'cornerCut'      : False,
            'direction'      : direction,
            'startDwell'     : startDwell,
            }
    pocket = cnc_dxf.DxfRectPocketFromExtent(param)
    prog.add(pocket)


# Cable slot
param = {
        'fileName'    : fileName,
        'layers'      : ['cable_slot_center'],
        'depth'       : 0.125,
        'startZ'      : startZ,
        'safeZ'       : safeZ,
        'toolDiam'    : toolDiam,
        'cutterComp'  : None,
        'maxCutDepth' : maxCutDepth,
        'startDwell'  : startDwell,
        'startCond'   : 'minX',
        }
boundary = cnc_dxf.DxfBoundary(param)
prog.add(boundary)


prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.End(),comment=True)
baseName, dummy = os.path.splitext(__file__)
fileName = '{0}.ngc'.format(baseName)
print('generating: {0}'.format(fileName))
prog.write(fileName)
