#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 15:34:28 2020

@author: jordan
"""

#DESCRIPTION:
    #NAME: backupToZip.py
    #PURPOSE: Copies an entire folder and its contents into a ZIP file whose
    #filename increments
    
import zipfile, os

def backupToZip(folder):
    #Back up the entire contents of "folder" into a ZIP file
    
    folder = os.path.abspath(folder)  #make sure folder is absolute
    
    
    #Figure out the filename this code should use based on
    #what files aready exist.
    
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' +str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1
        
   #TODO: create the ZIP file.
    print(f'Creating {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')

   #TODO: walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        # Add th current folder to th ZIP fole
        backupZip.write(foldername)
       
        #Add all the files in this folder to the ZUP file
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue #don't back up the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
        backupZip.close()
        print('Done.')

backupToZip('/home/jordan/backups')