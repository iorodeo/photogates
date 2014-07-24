from __future__ import print_function
import dxfgrabber
import matplotlib.pyplot as plt


dwg = dxfgrabber.readfile('body.dxf')

for entity in dwg.entities:
    print(entity.dxftype)
    print(entity.layer)
    print(entity.color)
    print()


plt.show()
