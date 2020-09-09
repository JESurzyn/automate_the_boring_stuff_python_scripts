#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 18:53:43 2020

@author: jordan
"""

#DESCRIPTION
    #NAME: gapFinder.py
    #PURPOSE: a program that finds files with a specific prefix and if there
    #is a gap in numbers, rename files to close the gap
  
import os, shutil, re
from pathlib import *

#TODO: identify files that match the prefix
prefix = 'spam'
suffix = '.txt'
p = Path('/home/jordan/spamfiles')
spamList = list(p.glob('spam???.txt'))


#TODO:order the files in alphanum order
stems = [fullPath.stem for fullPath in spamList]

regexOb = re.compile(r'spam(\d\d\d)')

stemNum = []
for i in stems:
    
#TODO:isolate number

#TODO:compare to an enumeration through a range


#TODO: find gap