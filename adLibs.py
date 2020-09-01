#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 19:14:18 2020

@author: jordan
"""

madLibs = open('adLibs.txt','r')
readItem = madLibs.read()
madLibs.close()
wordList = readItem.split()

def partOfSpeech(y):
    if y == 'ADJECTIVE':
        return input('Enter an adjective:\n')
    elif y == 'NOUN':
        return input('Enter a noun:\n')
    elif y == 'VERB':
        return input('Enter a verb:\n')
    else:
        return y

for x in range(len(wordList)):
    if wordList[x].endswith('.'):
        endWord = wordList[x].strip('.')
        wordList[x] = partOfSpeech(endWord) + '.'
    elif x == 0:
        z = partOfSpeech(wordList[x]).lower()
        zTitle = z[0].upper()
        wordList[x] = zTitle + z[1:]
    elif wordList[x-1].endswith('.'):
        z = partOfSpeech(wordList[x]).lower()
        zTitle = z[0].upper()
        wordList[x] = zTitle + z[1:]
    else:
       wordList[x] = partOfSpeech(wordList[x])
       
newText = open('madLibsAnswer.txt', 'w')
newText.write(' '.join(wordList))
newText.close()
print('\nAnswers copied, look for new file')