# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:06:46 2019

@author: Kamakshi
"""

import tweepy
import csv

consumer_key = "W8olFrRLK7Lt7BUh6YAbdSG4h"
consumer_secret = "izRdiwC73rntSdMdAQm2gL8zFNAHVLa99A8dI99w0Lz16jvNrx"

access_token = "620364433-Kj5up6bB6KLfl5wfmxxcAnWthse5o38P2MKABM00"
access_token_secret = "Faxxv0hb54KF7MmakQ8WZmvaCC5YIprcWhiOuEyQY2iLt"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Open/Create a file to append data
csvFile = open('Square_tweets.csv', 'a')
#Use csv Writer
fields = ('date','text', 'followers')
csvWriter = csv.writer(csvFile, lineterminator= '\n')

for tweet in tweepy.Cursor(api.search, q="SQ", lang="en", since_id='2019-27-22').items(100):
    #print(tweet.created_at, tweet.text)
    follower_count = tweet.user.followers_count
    #if tweet.created_at >= datetime.datetime(2019,2,24):
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),follower_count])
    

