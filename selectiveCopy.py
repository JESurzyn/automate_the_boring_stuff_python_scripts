#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 18:32:25 2020

@author: jordan
"""

#DESCRIPTION:
    #NAME: selectiveCopy.py
    #PURPOSE: for a specific folder tree, copy all files of a type into a new
    #folder
    
import shutil, os
from pathlib import *

#copy py
#search home folder for python files and copy into new folder called "allpyfiles"

#Path.mkdir(Path.home()/'class_notebooks_only')
destinPath = Path.home()/'class_notebooks_only'
walkPath = Path.home()/'inferential_stat_analysis'

for currentFolder, subFolders, currentFiles in os.walk(walkPath):    
    for i in currentFiles:
        if '.ipynb' in i:
            fullName = currentFolder + '/'+ i
            shutil.move(fullName, destinPath)
            
            