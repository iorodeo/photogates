from py2scad import *

x,y,z = 1.0*INCH2MM, 0.6*INCH2MM, 0.0625*INCH2MM
radius = 0.1*INCH2MM

sensorWidth = 0.32*INCH2MM 
sensorOffsetX = 0.08*INCH2MM
sensorHoleSep = 0.335*INCH2MM
sensorHoleDiam = (0.14*INCH2MM, 0.185*INCH2MM)
sensorHoleRelPosX = (-0.5*sensorHoleSep,0.5*sensorHoleSep)

mountHoleDiam = 0.116*INCH2MM
mountHoleSep = 0.75*INCH2MM

holeList = []

# Create sensor mount holes
for diam, relPosX  in zip(sensorHoleDiam, sensorHoleRelPosX):
    posX = sensorOffsetX + relPosX 
    posY = -0.5*y + 0.5*sensorWidth
    hole = (posX, posY, diam)
    holeList.append(hole)


# Create plate mount holes

for i in (-1,1):
    posX = 0.5*i*mountHoleSep
    posY = 0.5*y - 1.3*mountHoleDiam
    hole = (posX, posY, mountHoleDiam)
    holeList.append(hole)

plate = plate_w_holes(x,y,z,holes=holeList,radius=radius)

prog = SCAD_Prog()
prog.fn = 100
prog.add(plate)
prog.write('mount_plate.scad')

proj = SCAD_Prog()
proj.fn = 100
proj.add(Projection(plate))
proj.write('mount_plate_proj.scad')





