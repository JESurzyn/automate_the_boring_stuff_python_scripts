#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 16:46:48 2020

@author: jordan
"""

def spam():
    bacon()
    
def bacon():
    raise Exception('This is the error message')
    
spam()