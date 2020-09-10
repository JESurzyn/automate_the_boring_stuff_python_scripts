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
  
import os, shutil, re, sys
from pathlib import *

#TODO: identify files that match the prefix
prefix = 'spam'
suffix = '.txt'
p = Path('/home/jordan/spamfiles')
spamList = list(p.glob('spam???.txt'))

#TODO:order the files in alphanum order and convert to paths to strings
spamList.sort()
spamListAsString = [i.as_posix() for i in spamList]


#renaming function
def reNameAndMove(startingNumParam, itemAfterGapListParam):
    #create a list of the new integers
    newNumbersList = []
    newNumbersList.append(startingNumParam)
    for i in range(len(itemAfterGapListParam)):
        startingNumParam += 1
        newNumbersList.append(startingNumParam)
        
    for i in range(len(newNumbersList)):
        strConvert = str(newNumbersList[i])
        if len(strConvert) == 1:
            strConvert = '/home/jordan/spamfiles/spam00' + strConvert + '.txt'
        elif len(strConvert) ==2:
            strConvert = '/home/jordan/spamfiles/spam0' + strConvert + '.txt'
        else:
            strConvert = '/home/jordan/spamfiles/spam' + strConvert + '.txt'
        
        newNumbersList[i] = strConvert
        
    for n in range(len(itemAfterGapListParam)):
        shutil.move(itemAfterGapListParam[n], newNumbersList[n])    


#TODO:find gap
regexOb = re.compile(r'(spam)(\d{3})(\.txt)')

for i in range(len(spamListAsString)):
    basenameSpam = os.path.basename(spamListAsString[i])
    mo = regexOb.search(basenameSpam)
    num = int(mo.group(2))
    if i+1 != num:
        itemAfterGapList = spamListAsString[i:]
        #renaming the files starting with gap
        #SCENARIOS TO ACCOUNT FOR:
            #1. if the first file doesn't start with spam001
        
        if i == 0:
            startingNum = 1
            reNameAndMove(startingNum, itemAfterGapList)
            sys.exit()
                
            
        else:
            priorBaseName = os.path.basename(spamListAsString[i-1])
            mo2 = regexOb.search(priorBaseName)
            startingNum = int(mo2.group(2))+1
            #create code for renaming
            reNameAndMove(startingNum, itemAfterGapList)
            sys.exit()
            
            
  



