# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 11:48:00 2018

@author: Chintan Maniyar
"""

from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime
from dateutil import parser
import webbrowser, csv

access_token = "3318179888-ZvXO61fVSV61UND0QOvMHs9QwQJhAHrwEAJB7EK"
access_token_secret = "0czdPJSxvJiDBUmt7HOFCFnjejgW8R2GHinI7r1mTZFr4"
consumer_key = "cc9yjThuWxyJXF3mIEsv3rBik"
consumer_secret = "ieTAoNPxWeJqu14IuBuJRgcRZrXeMLPbGsgcAQsrk0W53Fdqfu"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

tweets_data = {'id':[], 'text':[], 'place':[], 'time':[]}
url = 'twitter.com/statuses/'

def fetchTweets(info=False):
    for tweet in Cursor(api.search_tweets, 
                         q = 'BlueGreenAlgae OR CyanoBacteria OR cyanotracker OR anabaena OR microcystis OR cyanotoxins OR toxic algae OR algae bloom OR algal bloom OR #CyanoBacteria OR #AlgaeBloom OR #CitSci OR #CyanoBacteriaBlooms',
                         count = 20,
                         result_type = 'recent',
                         include_entities = True,
                         monitor_rate_limit = True,
                         wait_on_rate_limit = True,
                         lang="en").items():
        try:
            if ((datetime.now() - parser.parse(str(tweet.created_at))).days < 1) and (not tweet.retweeted) and ('RT @' not in tweet.text):
                webbrowser.open_new_tab(url+str(tweet.id))
                tweets_data['id'].append(str(tweet.id))
                tweets_data['text'].append(str(tweet.text))
                if(tweet.user.location is None):
                    tweets_data['place'].append("00")
                tweets_data['place'].append(str(tweet.user.location))
                tweets_data['time'].append(str(tweet.created_at))
        except:
            continue
    
    try:
        with open('prod.csv', 'w', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(tweets_data.keys())
            writer.writerows(zip(*tweets_data.values()))
    except IOError as e:
        print(e)
        
    if info:
        for i in range(len(tweets_data['text'])):
            print("\nTweet no %d" %i)
            print("Time of origin: " + tweets_data['time'][i])
            print("Text : " + tweets_data['text'][i])
            print("Place: ", end="")
            if(tweets_data['place'][i]!=None):
                print(tweets_data['place'][i])
            else:
                print("Not available for this tweet")

if __name__ == "__main__":
    
    #fetch tweets and validate them, info prints the tweet information on the console
    fetchTweets(info=True)