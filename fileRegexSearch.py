#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 21:36:51 2020

@author: jordan
"""

import re
from pathlib import *

#Create User Input for Regex Expression

regexUser = input('input a regex pattern to match:\n')
regexPattern = re.compile(regexUser)

#Create User Input for folder path
pathString = input('\ninput a file path to search\n')
searchPath = Path(pathString)

#Search for .txt files within folder and place into a list
matchedFiles = list(searchPath.glob('*.txt'))
if len(matchedFiles) == 0:
    print('no text files found')
    
else:
    #for each file
    for i in range(len(matchedFiles)):
        #print file name
        print('\n\n\n'+matchedFiles[i].name +'\n')
        #open the file, create read object
        openObject = open(matchedFiles[i],'r')
        #read through lines
        sentenceList = openObject.readlines()
        if len(sentenceList) == 0:
            continue
        else:
            
 
        #search through read object for regex matches       
            moList = []
            for x in range(len(sentenceList)):
                regMatchList = regexPattern.findall(sentenceList[x])
                if len(regMatchList) == 0:
                    continue
                else:
                    print(f'Line {x+1}:')
                    for y in range(len(regMatchList)):
                        print('    '+regMatchList[y])
                        
                        
print('\n\n\n\n*******DONE*********')                        
        
        
    
        #print results to screen