#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 15:37:58 2020

@author: jordan
"""

import re

#fail length
testPassword1 = 'Abcdef7'

#fail uppercase
testPassword2 = 'abcdefg7'

#fail lowercase
testPassword3 = 'ABCDEFGE7'

#fail digit
testPassword4 = 'ABCDefgh'

#strong password
strongPassword = 'ABcdefg89'

passTestList = [testPassword1, testPassword2, testPassword3, testPassword4,
                strongPassword, 'abcdef7', 'abcdef']


#8 character pattern
character8 = re.compile(r'\S{8,}') #anythng valid but space character
#1 or more uppercase
upperChar = re.compile(r'[A-Z]+')
#1 or more lowercase
lowerChar = re.compile(r'[a-z]+')
#1 or more digit
digitChar = re.compile(r'\d+')

'''
mo = character8.search(testPassword1)
print(type(mo))

if mo is None:
    print('Must have at least 8 characters')
    
    
    
'''



##TO DO: Write out as function

def strongPasswordCheck(password):
    ###ESTABLISH CRITERIA REGEX PATTERNS
    #8 character pattern
    character8 = re.compile(r'\S{8,}') #anythng valid but space character
    #1 or more uppercase
    upperChar = re.compile(r'[A-Z]+')
    #1 or more lowercase
    lowerChar = re.compile(r'[a-z]+')
    #1 or more digit
    digitChar = re.compile(r'\d+')
    
    passwordStatuses = []
    if character8.search(password) is None:
        passwordStatuses.append('Must be at least 8 characters')
    if upperChar.search(password) is None:
        passwordStatuses.append('Must have at least 1 uppercase character')
    if lowerChar.search(password) is None:
        passwordStatuses.append('Must have at least 1 lowercase character')
    if digitChar.search(password) is None:
        passwordStatuses.append('Must have at least 1 numerical digit')
        
    if len(passwordStatuses) == 0:
        print('Valid Password')
    else:
        print('Please create stronger password')
        for i in range(len(passwordStatuses)):
            print(passwordStatuses[i])

for i in range(len(passTestList)):
    strongPasswordCheck(passTestList[i])
    print('\n')