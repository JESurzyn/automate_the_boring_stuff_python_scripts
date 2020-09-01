#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 17:38:43 2020

@author: jordan
"""
import re

def regStrip(inputString, specifiedCharacters = ''):
    #if no specific strip characters id'd strip whitespace
    if specifiedCharacters ==  '':
        blankEnds = re.compile(r'\s*([\S]+)\s*')  #whitespace strip regex
        mo = blankEnds.search(inputString)
        if mo is not None:
            return mo.group(1)
    else:
        for i in range(len(inputString)):
            if inputString[i] not in specifiedCharacters:
                frontStopIndex = i
                break
        
        for i,k in enumerate(reversed(inputString)):
            if k not in specifiedCharacters:
                revBackStopIndex = i
                break
    
        backStopIndex = len(inputString)-revBackStopIndex
        strippedString = inputString[frontStopIndex:backStopIndex]
        return strippedString



#whitespace strip test
print(regStrip('    Te*))(sty  '))

#specified character strip test
print(regStrip('x3y3xTesty3x', 'xy3'))


'''
blankEnds = re.compile(r'\s*([\S]+)\s*') 
testString = '    Te*))(sty  '


mo = blankEnds.search(testString)
if mo is not None:
    print(mo.group(1))
    print(len(mo.group(1)))

print(testString)

testString = 'x3y3xTesty3x'
stripCharacters = 'xy3'

#print(testString[0])


for i in range(len(testString)):
    if testString[i] not in stripCharacters:
        frontStopIndex = i
        break
print(frontStopIndex)


for i,k in enumerate(reversed(testString)):
    if k not in stripCharacters:
        revBackStopIndex = i
        break
print(revBackStopIndex)

print(backStopIndex)

'''


