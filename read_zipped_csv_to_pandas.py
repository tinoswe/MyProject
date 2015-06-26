# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 08:56:59 2015

@author: martino.olivo
"""

import pandas as pd
import zipfile


#zf1 = zipfile.ZipFile('C:/Progetti/Algorithms/Kaggle/Avito Context ADs/input/sample_submission/sampleSubmission.zip')
#df1 = pd.read_csv(zf1.open('sampleSubmission.csv'))


#SearchID - identifier for a visitors's search event.
#AdID - identifier of the ad (see also ad description in AdsInfo.tsv).
#Position - position of the ad in search result page (1 - is first ad on a page starting from the top). Only ads on position 1, 2, 6, 7, and 8 are logged.
#ObjectType - type of the ad shown to user. The options are: 1 - regular free ads added by users; 2 - highlighted regular (owners have to pay fixed price to highlight them and stick to the top for some period of time); 3 - contextual ads (owners have to pay per visitor's click).
#HistCTR - some naive history-based estimation of click-through rate for contextual ads, calculated when the ad is showed. For non-contextual ads this field equals NULL.
#IsClick - 1 if there was a click on this ad. Otherwise 0. For non-contextual ads this field equals NULL. The goal of this competition is to make a click prediction model for contextual ads.

zf_test = zipfile.ZipFile('C:/Progetti/Algorithms/Kaggle/Avito Context ADs/input/test_search_stream/testSearchStream.zip')
df_test = pd.read_csv(zf_test.open('testSearchStream.tsv'), delimiter='\t')

#zf_train = zipfile.ZipFile('C:/Progetti/Algorithms/Kaggle/Avito Context ADs/input/train_search_stream/trainSearchStream.zip')
#df_train = pd.read_csv(zf_train.open('trainSearchStream.tsv'), delimiter='\t')

#from df3 create a smaller csv to test the code
#nlines = len(df_test['ID'])
#chunksize = 100 # number of lines to process at each iteration

df_test[:10].to_csv('C:/Progetti/Algorithms/Kaggle/Avito Context ADs/input/test_search_stream/chunk' + str(1) + '.csv', sep=',') #1kb
df_test[:10].to_pickle('C:/Progetti/Algorithms/Kaggle/Avito Context ADs/input/test_search_stream/chunk' + str(1) + '.pkl') #2kb
df_test[:10].to_hdf('C:/Progetti/Algorithms/Kaggle/Avito Context ADs/input/test_search_stream/chunk' + str(1) + '.hdf5','table',append=True) #83kb

