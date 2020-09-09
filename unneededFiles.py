#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 15:20:16 2020

@author: jordan
"""

#DESCRIPTION:
    #NAME: unneededFiles.py
    #PURPOSE: delete files under a certain path
    
import os

from pathlib import *


walkPath = Path.home()
#if os.path.getsize() > 1000000
for currentFolder, subFolder, fileNames in os.walk(walkPath):
    if os.path.getsize(currentFolder) > 1000000:
        print(currentFolder)
    for i in fileNames:
        fullPath = currentFolder + '/' + i
        if Path(fullPath).exists() == True:
            if os.path.getsize(fullPath) > 1000000:
                print(fullPath)
