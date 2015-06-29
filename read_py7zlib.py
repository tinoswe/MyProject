# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 10:28:58 2015
@author: martino.olivo
"""

import os
import py7zlib as pz
import pandas as pd

data_dir = 'C:/Progetti/Algorithms/Kaggle/Avito Context ADs/input/sample_submission/'#out_csv/'
fname = 'sampleSubmission.csv.7z'
#fname = 'test.csv.7z'
#out_dir = data_dir + 'out_csv/'

#f = pz.Archive7z(open(data_dir + fname, 'rb'))
#f.list()

for dirpath, dirname, filename in os.walk(data_dir):
    
    for myfile in filename:

        if myfile.endswith('n.csv.7z'):

            print data_dir + myfile

            myZip = pz.Archive7z(open(os.path.join(data_dir,myfile), 'rb'))
        
#            csvInZipFile = zip(myZip.filenames,myZip.files)
        
#            for myCsvFileName, myCsvFile in csvInZipFile:
    
#                pass    
    
                #with open(os.path.join(out_dir, myCsvFileName),'wb') as outfile:
                #    outfile.write(myCsvFile.read()) 
                 
                #df = pd.read_csv(myCsvFile.read()) 
                                 #'delimiter=',',
                                 #'encoding='utf-8',
                                 #'skiprows=[-1])
                                 
                #df_test = pd.read_csv(myCsvFile)#.read())
                    
                
#dframe = pd.read_csv(myCsvFileName) 
                    