#!/usr/bin/env python3

import sys
import re
from subprocess import check_output

installed = str(check_output(["R", "-e installed.packages()[,1]"]))
installed = re.findall('"[A-Za-z0-9]*"', installed)
installed = [name.strip('"') for name in installed]

try:
    sys.argv[1]
except IndexError:
    fname = str(input("Filename: "))
else:
    fname = str(sys.argv[1])
    
rfile = open(fname, 'r')
ftext = rfile.read()
rfile.close()
rLibs = re.findall('(?<=library\()["\'A-Za-z0-9]*', ftext)
rReq = re.findall('(?<=require\()["\'A-Za-z0-9]*', ftext)
rLibs = rLibs + rReq
rLibs = [name.strip("'") for name in rLibs]
rLibs = [name.strip('"') for name in rLibs]
rLibs = list(set(rLibs) - set(installed))

command = 'install.packages(c("' + '","'.join(rLibs) + '"))'
print("Run: \n")
print(command + "\n")
