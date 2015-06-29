# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 14:10:01 2015

@author: martino.olivo
"""

import sqlite3
from pandas.io import sql

# Create connection.
cnx = sqlite3.connect('C:/Progetti/Algorithms/Kaggle/Avito Context ADs/test_sqlite/Chinook_Sqlite.sqlite')


# read the result of the SQL query into a DataFrame
#data = sql.read_sql("SELECT * FROM sqlite_master;", cnx)

#data = sql.read_sql("SELECT * FROM Album;", cnx)
#LIMIT [no of rows] OFFSET [row num]

# now you can write it into a HDF5 file
#data.to_hdf('C:/Progetti/Algorithms/Kaggle/Avito Context ADs/test_sqlite/test_store.hdf','test',mode='w')
