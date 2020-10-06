#pip install twitter
#pip install tweepy
#python -m nltk.downloader stopwords

import json
import twitter
import tweepy
import re
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

#Add your Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

def get_all_tweets(screen_name):
    #Twitter only allows access to a users most recent 3240 tweets

    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    #initialize a list to hold all the tweepy Tweets
    alltweets = []
    all_tweets = []

    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    #tweets = [i.AsDict() for i in new_tweets]

    #save most recent tweets
    alltweets.extend(new_tweets)

    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:

        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,include_rts=False,max_id=oldest)

        #save most recent tweets
        alltweets.extend(new_tweets)

        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        for tweet in alltweets:
            time = tweet.created_at
            # retweet = tweet.retweet_count
            # favorites = tweet.favorite_count
            text = tweet.text
            #twitter_data = {'time':time,'retweet':retweet, 'favorites':favorites}
            twitter_data = {'time':time,'text':text}
            all_tweets.append(twitter_data)

    df = pd.DataFrame(all_tweets)
    df['time']=pd.to_datetime(df['time'])
    df = df.set_index('time')

    return(df)

def word_freq(df):
    words = []

    #remove additional words that are not relevent
    df['text'] = df['text'].str.replace('https', '')
    df['text'] = df['text'].str.replace('Citi', '')
    df['text'] = df['text'].str.replace('UBS', '')

    #words = black_rock_tweets['text'].str.findall(r'[A-Za-z]+')
    for text, item in df.iteritems():
      tokens = item.str.findall(r'[A-Za-z]{3,}')
      for tweet in tokens:
        for word in tweet:
          words.append(word.lower())

    sw = nltk.corpus.stopwords.words('english')
    words_ns = []

    for word in words:
        if word not in sw:
          words_ns.append(word)

    sns.set()

    # Create freq dist and plot
    freqdist1 = nltk.FreqDist(words_ns)
    #print(freqdist1)
    freqdist1.plot(50)

#BLACKROCK
# black_rock_tweets = get_all_tweets("blackrock")
# word_freq(black_rock_tweets)

#CITI
# citi_tweets = get_all_tweets("Citi")
# word_freq(citi_tweets)

#UBS
ubs_tweets = get_all_tweets("UBS")
word_freq(ubs_tweets)
