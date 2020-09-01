#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 16:33:23 2020

@author: jordan
"""

import pyinputplus as pyip
import random, time

numberOfQuestions = 10
numberCorrect = 0

for i in range(numberOfQuestions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    
    prompt = '#{} {} x {} ='.format(i+1, num1, num2)
    try:
        pyip.inputStr(prompt, allowRegexes=['^{}'.format(num1*num2)],
                      blockRegexes=[('.*','Incorrect!')],
                      timeout= 8, limit = 3
                      )
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print('Correct')
        numberCorrect += 1
    time.sleep(1)
    
print('Score: {}/{}'.format(numberCorrect, numberOfQuestions))