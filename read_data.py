# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 16:21:52 2015
@author: tinoswe
"""
#https://plot.ly/ipython-notebooks/big-data-analytics-with-pandas-and-sqlite/
#http://stackoverflow.com/questions/14262433/large-data-work-flows-using-pandas
#http://sebastianraschka.com/Articles/sqlite3_database.html
#http://johnbeieler.org/blog/2013/06/06/using-sql/

#import sqlite3
# Create a database in RAM
#db = sqlite3.connect(':memory:')
# Creates or opens a file called mydb with a SQLite3 DB
#db = sqlite3.connect('C:/Progetti/Algorithms/Kaggle/Avito Context ADs/test_sqlite/Chinook_Sqlite.sqlite')


import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('sqlite:///../input/database.sqlite') # ---------> HOW BIG? about 40 Gb

def get_count(name):
    count=pd.read_sql('select count(*) from '+name, engine)
    return count.iloc[0,0]
def get_sample(name):
    sample=pd.read_sql('select * from ' + name + ' limit 10', engine)
    return sample 
tabs=["AdsInfo","Category","Location","PhoneRequestsStream","SearchInfo","UserInfo","VisitsStream","testSearchStream","trainSearchStream"]
counts=[get_count(tab) for tab in tabs]

tab_count_df=pd.DataFrame({'name': tabs, 'row_count':counts})
tab_count_df

samples=[get_sample(tab) for tab in tabs]
sample_df=pd.DataFrame({'name': tabs, 'sample':samples})
sample_df.iloc[0,1] #AdsInfo