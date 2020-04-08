import pandas as pd
import numpy as np
import re
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import tweepy
from tweepyTest import twitterAPI

# keys, tokens and secrets
CONSUMER_KEY = "5uZBofueiS8jKVhKXnpfr2MTN"
CONSUMER_SECRET = "gTI1aFRaSFEvCYwgxyJp6BNZywsavklgipwWzswo7wyl48SzGq"
ACCESS_TOKEN = "1049322266583031808-Of422oa5DYZwYKlDbBxg7zYVeXjrj1"
ACCESS_SECRET = "i2KsOw73ECIRqEx53QNfqv6KKNh5eSwyPcayN5xJhhHxQ"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

# number of tweets to find
no_tweets = 1000

# Key words and remove retweets
new_search = "oil, price, WTI" + " -filter:retweets"



def run():
    #Call the twitter method and store all tweets in a list
    StringArray = twitterAPI(api, no_tweets, new_search)['text'].values.tolist()

    #Remove punctuation
    for eachString in twitterAPI(api, no_tweets, new_search)['text']:
        result = re.sub(r'[^a-zA-Z]', " ", eachString)
        StringArray.remove(eachString)
        StringArray.append(result)

    #print (StringArray)
    sid = SentimentIntensityAnalyzer()
    overallScore = 0
    for eachString in StringArray:
        ss = sid.polarity_scores(eachString)
        #Remove the comment below to find what the text in the articles consists of
        #print (eachString, " has a score of ", ss['compound'])
        overallScore += ss['compound']

    print ("Overall score: ", overallScore / len(StringArray))
    return overallScore

run()
