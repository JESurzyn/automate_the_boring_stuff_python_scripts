#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 00:23:51 2020

@author: jordan
"""

import random

heads = 0
for i in range(1, 1001):
    if random.randint(0,1)==1:
        heads = heads + 1
    if i == 500:
        print('Halfway done!')
print('Heads came up ' + str(heads) + ' times.')

