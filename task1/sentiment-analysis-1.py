import tweepy
from textblob import TextBlob

import credentials


auth = tweepy.OAuthHandler(credentials.api_key,credentials.api_secret)
auth.set_access_token(credentials.access_token,credentials.access_secret)

hashtag_query=['bill gates','steve jobs']

api = tweepy.API(auth)
public_tweets=api.search(hashtag_query)

for tweets in public_tweets:
    analysis=TextBlob(tweets.text)
    #print(tweets.text)
    print(analysis.sentiment.polarity)