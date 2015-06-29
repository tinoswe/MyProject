# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 18:01:38 2015

@author: martino.olivo
"""

import pandas as pd
import sqlite3 # replace this with small csv or h5
from pandas.io import sql
import subprocess

# In and output file paths
in_csv = '../data/my_large.csv'
out_sqlite = '../data/my.sqlite'

table_name = 'my_table' # name for the SQLite database table
chunksize = 100000 # number of lines to process at each iteration

# columns that should be read from the CSV file
columns = ['molecule_id','charge','db','drugsnow','hba','hbd','loc','nrb','smiles']

# Get number of lines in the CSV file
nlines = subprocess.check_output('wc -l %s' % in_csv, shell=True)
nlines = int(nlines.split()[0]) 

# connect to database
cnx = sqlite3.connect(out_sqlite)

# Iteratively read CSV and dump lines into the SQLite table
for i in range(0, nlines, chunksize):

    df = pd.read_csv(in_csv,  
            header=None,  # no header, define column header manually later
            nrows=chunksize, # number of rows to read at each iteration
            skiprows=i)   # skip rows that were already read

    # columns to read        
    df.columns = columns

    sql.to_sql(df, 
                name=table_name, 
                con=cnx, 
                index=False, # don't use CSV file index
                index_label='molecule_id', # use a unique column from DataFrame as index
                if_exists='append') 
cnx.close()    