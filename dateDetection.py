#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 13:21:01 2020

@author: jordan
"""

import re

dateMatch = re.compile(r'''(
    
    (0[1-9]|[1-2][0-9]|3[0-1])     #DD
    /                              #/
    (0[1-9]|1[0-2])                #MM 
    /                              #/
    ([1-2][0-9][0-9][0-9])         #YYYY
    )''', re.VERBOSE)
    
testString = '31/02/2020'

mo = dateMatch.search(testString)
'''
print(mo.groups())
print(mo.group())
print(mo.group(1))
print(mo.group(2))
print(mo.group(3))
print(mo.group(4))
'''
mo2 = dateMatch.findall('''The regular expression doesn’t have to detect 
correct days for each month or for leap years; it will accept nonexistent 
dates like 29/02/2020 or 31/04/2021. Then store these strings into variables 
named month, day, and year, and write additional code that can detect if it is
 a valid date. April, June, September, and November have 30 days, February has
 28 days, and the rest of the months 29/02/2021 have 31 days. February has 29 days in 
 leap years. Leap years are every year evenly divisible by 4, except for years
 evenly divisible by 100, unless the 08/07/2020 year is  also evenly divisible by 400. 
 Note how this calculation makes it impossible to make a reasonably sized 
 regular expression that can detect a valid date.''')
    
print(mo2)



def validDate(matchObject):
    for i in range(len(matchObject)):
        validStatus = True
        
        #sort sections into day, month, year variables
        day = matchObject[i][1]
        month = matchObject[i][2]
        year = matchObject[i][3]
        
        #30 day check
        if month in ['04', '06', '09', '11'] and int(day) > 30:
            validStatus = False
        
        #leap year check
        leapYearStatus = False
        if int(year) % 4 == 0: 
            if int(year) % 100 == 0 and int(year) % 400 != 0:
                leapYearStatus = False
            elif int(year) % 100 == 0 and int(year) % 400 == 0:
                leapYearStatus = True
            else:
                leapYearStatus = True
        
        #feb check
        if leapYearStatus == True:
            if month == '02' and int(day) > 29:
                validStatus = False
        else:
            if month == '02' and int(day) > 28:
                validStatus = False
        
        print(matchObject[i][0]+' Valid Date Status: '+str(validStatus))

validDate(mo2)
        
        
        
            
                
                

'''
for i in range(len(mo2)):
    day = mo2[i][1]
    month = mo2[i][2]
    year = mo2[i][3]
    print(day)
    print(month)
    print(year)
'''