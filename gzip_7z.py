# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 10:23:01 2015

@author: martino.olivo
"""

data_dir = 'C:/Progetti/Algorithms/Kaggle/Avito Context ADs/input/sample_submission/'
fname = 'sampleSubmission.csv.7z'

import gzip
import py7zlib as pz
#f = gzip.open(data_dir + fname, 'rb')
#file_content = f.read()
#f.close()


f = pz.Archive7z(open(data_dir + fname, 'rb'))
#    #f = Archive7z(open('pylzma.7z', 'rb'))
#    f.list()