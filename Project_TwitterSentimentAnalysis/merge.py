# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 12:07:00 2019

@author: Kamakshi
"""

import pandas as pd
import glob

#allFiles = glob.glob("finaldata/*.csv")
allFiles = glob.glob("finaldata/*.csv")
frame = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=0,encoding='latin-1')
    df = df.drop('text', 1)
    df = df.drop('date', 1)
    list_.append(df)
frame = pd.concat(list_)

frame.to_csv('final.csv')