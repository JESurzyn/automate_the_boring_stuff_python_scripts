#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 15:29:57 2020

@author: jordan
"""

import pyinputplus as pyip

###   Sandwich Maker ####
'''
Requirements:
    1. Bread type
    2. Protein type
    3. Cheese -yes or no
        -if yes, type
    4. Mayo
    5. Mustard
    6. Lettuce
    7. tomato
    8. How many sandwiches
    9. Total Price
'''
###PRICES
sandwichPrice = 5.00
#Ingredients Price Dictionaries
bread = {'wheat': 0, 'white':0, 'sourdough':0.50}
protein = {'chicken':1, 'turkey':1, 'ham':1.25, 'tofu': 1.50}
cheese = {'chedder':0.5, 'swiss':0.5, 'mozzarella': 0.75}
orderRecap = []

orderTotal = 0

#BREAD
breadList = ['wheat', 'white', 'sourdough']
breadChoice = pyip.inputMenu(breadList, numbered=True)
orderTotal = sandwichPrice + bread[breadChoice]
orderRecap.append(breadChoice)

#PROTEIN
proteinList = ['chicken', 'turkey', 'ham', 'tofu']
proteinChoice = pyip.inputMenu(proteinList, numbered=True)
orderTotal += protein[proteinChoice]
orderRecap.append(proteinChoice)

#CHEESE
cheeseList = ['chedder', 'swiss', 'mozzarella']
cheeseYN = pyip.inputYesNo(prompt='Would you like cheese on your sandwich?')

if cheeseYN == 'yes':
    cheeseChoice = pyip.inputMenu(cheeseList, numbered=True)
    orderTotal += cheese[cheeseChoice]
    orderRecap.append(cheeseChoice)

#EXTRAS
mayo = pyip.inputYesNo(prompt='Mayo?')
if mayo == 'yes':
    orderRecap.append('mayo')
    
mustard = pyip.inputYesNo(prompt='Mustard?')
if mustard == 'yes':
    orderRecap.append('mustard')
    
lettuce = pyip.inputYesNo(prompt='Lettuce?')
if lettuce == 'yes':
    orderRecap.append('lettuce')

tomato = pyip.inputYesNo(prompt='Tomato?')
if tomato == 'yes':
    orderRecap.append('tomato')

#How many sandwiches
howMany = pyip.inputInt(prompt='How many would you like?', greaterThan=1)

print('To recap your order:')
for i in orderRecap:
    print(i)
print(f'x{howMany}')

orderTotal *= howMany
print(f'Your total price will be {orderTotal}')

