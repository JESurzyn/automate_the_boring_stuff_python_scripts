#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 12:58:45 2020

@author: jordan
"""
#DESCRIPTION:
    #NAME: renameDates.py
    #PURPOSE: Renames files with American MM-DD-YYYY date format to European
    #DD-MM-YYYY

#MODULE IMPORTS
import shutil, os, re

###---Search through file names in cwd for American Dates---###
#1. establish regex pattern to id American dates, it is known that all files,
#if they have a date, are in the american format
datePattern = re.compile(r'''
    ^(.*?)              #all text before the date
    ((0|1)?\d)-         #one or two digits for the month
    ((0|1|2|3)?\d)-     #one or two digits for the day
    ((19|20)\d\d)       #four digits for the year
    (.*?)$              #all text after the date
                         ''',re.VERBOSE)
 #2. use listdir to find all files in working directory
#TODO: Loop over the files in the working directory
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
#TODO: Skip files without a date
    if mo == None:
        continue
#TODO: Get the different parts of the filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

#TODO: Form the European-style filename.
euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + \
    afterPart
#TODO: Get the full, absolute file paths.
absWorkingDir = os.path.abspath('.')
amerFileName = os.path.join(absWorkingDir, amerFilename)
euroFileName = os.path.join(absWorkingDir, euroFilename)
#TODO: Rename the files                          
print(f'Renaming "{amerFilename}" to "{euroFilename}"...')
#shutil.move(amerFilename, euroFilename) #uncomment after testing