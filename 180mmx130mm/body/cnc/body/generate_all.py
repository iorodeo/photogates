from __future__ import print_function
import os
import sys
import glob
import subprocess

if len(sys.argv) < 2:
    dxfFileName = 'body_in.dxf'
else:
    dxfFileName = sys.argv[1]

fileList = glob.glob('*.py')
fileList.remove(__file__)

for fileName in fileList:
    subprocess.call(['python', fileName, dxfFileName]) 

