# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 16:25:25 2019

@author: Kamakshi
"""

import pandas
import tweepy
from textblob import TextBlob

consumer_key = "W8olFrRLK7Lt7BUh6YAbdSG4h"
consumer_secret = "izRdiwC73rntSdMdAQm2gL8zFNAHVLa99A8dI99w0Lz16jvNrx"

access_token = "620364433-Kj5up6bB6KLfl5wfmxxcAnWthse5o38P2MKABM00"
access_token_secret = "Faxxv0hb54KF7MmakQ8WZmvaCC5YIprcWhiOuEyQY2iLt"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret,)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
colnames=['date', 'text', 'followers']

df = pandas.read_csv('Square_tweets.csv',encoding='latin-1', names=colnames, header=None)
df['polarity'] = 0.0000
df['sentiment_confidence'] = 0.0000

for index,row in df.iterrows():
    analysis = TextBlob(df['text'][index])
    #print(analysis)
    sentiment, confidence  = analysis.sentiment
    df.at[index,'polarity'] = sentiment
    df.at[index,'sentiment_confidence'] = confidence

df.to_csv('sentimentdata/Square_sentiment.csv')