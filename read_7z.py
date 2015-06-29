# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 10:01:35 2015

@author: martino.olivo
"""

#Load files for processing
#credit http://stackoverflow.com/questions/20104460/how-to-read-from-a-text-file-compressed-with-7z-in-python

import pandas as pd
import os
import py7zlib

#data_dir = '../input/'
data_dir = 'C:/Progetti/Algorithms/Kaggle/Avito Context ADs/input/sample_submission/'

class SevenZFileError(py7zlib.ArchiveError):
    pass

class SevenZFile(object):
    @classmethod
    def is_7zfile(cls, filepath):
        """ Determine if filepath points to a valid 7z archive. """
        is7z = False
        fp = None
        try:
            fp = open(filepath, 'rb')
            archive = py7zlib.Archive7z(fp)
            n = len(archive.getnames())
            is7z = True
        finally:
            if fp: fp.close()
        return is7z

    def __init__(self, filepath):
        fp = open(filepath, 'rb')
        self.filepath = filepath
        self.archive = py7zlib.Archive7z(fp)

    def __contains__(self, name):
        return name in self.archive.getnames()

    def bytestream(self, name):
        """ Iterate stream of bytes from an archive member. """
        if name not in self:
            raise SevenZFileError('member %s not found in %s' %
                                  (name, self.filepath))
        else:
            member = self.archive.getmember(name)
            for byte in member.read():
                if not byte: break
                yield byte

    def readlines(self, name):
        """ Iterate lines from an archive member. """
        linesep = os.linesep[-1]
        line = ''
        for ch in self.bytestream(name):
            line += ch
            if ch == linesep:
                yield line
                line = ''
        if line: yield line
		
import csv

if SevenZFile.is_7zfile(data_dir + 'sampleSubmission.csv.7z'):
    sevenZfile = SevenZFile(data_dir + 'sampleSubmission.csv.7z')

    if 'sampleSubmission.csv' not in sevenZfile:
        print 'sampleSubmission.csv is not a member of sampleSubmission.csv.7z'
    else:
        reader = csv.reader(sevenZfile.readlines('sampleSubmission.csv'))
        #for row in reader:
        #    print ', '.join(row)
        #pd.read_csv(sevenZfile.readlines('sampleSubmission.csv'))
        
        