import pandas as pd
import tweepy

#keys, tokens and secrets
CONSUMER_KEY = "5uZBofueiS8jKVhKXnpfr2MTN"
CONSUMER_SECRET = "gTI1aFRaSFEvCYwgxyJp6BNZywsavklgipwWzswo7wyl48SzGq"
ACCESS_TOKEN = "1049322266583031808-Of422oa5DYZwYKlDbBxg7zYVeXjrj1"
ACCESS_SECRET = "i2KsOw73ECIRqEx53QNfqv6KKNh5eSwyPcayN5xJhhHxQ"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)

api = tweepy.API(auth)

#number of tweets to find
no_tweets = 1000

#Key words and remove retweets
new_search = "oil, price, WTI" + " -filter:retweets"


def twitterAPI(api,no_tweets,new_search):
    #collect tweets
    tweets = tweepy.Cursor(api.search,q=new_search,lang="en").items(no_tweets)

    #collect data from tweets
    user_locs = [[tweet.text,tweet.user.screen_name,tweet.user.location,tweet.favorite_count,tweet.retweet_count] for tweet in tweets]
    df = pd.DataFrame(data=user_locs,columns=["text","user","location","like count","retweet count"])
    return df


