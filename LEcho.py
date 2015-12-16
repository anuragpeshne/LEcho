#!/usr/bin/python

import fileinput
import subprocess
import os
import urllib2
import json

def transmit(matrix):
    req = urllib2.Request('http://localhost:8000/print')
    req.add_header('Content-Type', 'application/json')

    return urllib2.urlopen(req, json.dumps(matrix))

for line in fileinput.input():
    for char in line.rstrip():
        rawMatrix = subprocess.check_output(\
                os.getcwd() + '/font8X8/converter.py \'' + char + '\'',\
                shell=True\
                ).rstrip()

        jsonMatrix = map(
                lambda x: map(lambda y: int(y, 10), x),
                rawMatrix.split('\n')
                )
        transmit(jsonMatrix)
