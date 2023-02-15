#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
dir = "userdata/analysis"
import glob 
import os
import json
import cgi
print('Content-Type: text-plain; charset=utf-8\r\n\r\n')

dataurl = cgi.FieldStorage()
locfile = dataurl.getvalue('analysis')
fic = dir+'/'+locfile
try:
    handle = open(fic, "r")
    infos = handle.read()
    lines = infos.split('\n')
    handle.close()
except:
    print('fichier '+fic+' non trouvé')

json_str = json.dumps(lines)
print(json_str)