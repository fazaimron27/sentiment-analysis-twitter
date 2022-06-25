import os
import json
import tweepy
from datetime import date
from textblob import TextBlob 
from dotenv import load_dotenv

# load environment variables
load_dotenv()

# tweepy authentication
auth = tweepy.OAuthHandler(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET'))
auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_TOKEN_SECRET'))
api = tweepy.API(auth)

# query = 'Bitcoin'
# public_tweets = api.search_tweets(q=[query], count=200, lang='en')

all_polarity = 0

# for tweet in public_tweets:
# 	print('tweet: ', tweet.text)

# 	analysis = TextBlob(tweet.text)
# 	print(analysis.sentiment)
# 	all_polarity += analysis.polarity 

# 	print('')

# if all_polarity/100 > 0:
# 	print(all_polarity/100)
# 	print('Positive')	
# else:
# 	print(all_polarity/100)
# 	print('Negative')

# load dataset
with open('data/tweets.json', 'r') as dataset:
    tweets = json.load(dataset)
    for tweet in tweets:
        today = date.today()
        user_created_at = tweet['user_created_at'].split(' ')[5]
        user_followers = tweet['user_followers']
        gap = today.year - int(user_created_at)
        if gap >= 3 and user_followers > 1000:
            print('user:', tweet['user'])
            print('username:', '@'+ tweet['username'])
            print('tweet:', tweet['text'])
            print('user_created_at:', tweet['user_created_at'])
            print('user_followers:', tweet['user_followers'])

            analysis = TextBlob(tweet['text'])
            print(analysis.sentiment)
            all_polarity += analysis.polarity 

            print('')
    
if all_polarity/100 > 0:
    print(all_polarity/100)
    print('Positive')
else:
    print(all_polarity/100)
    print('Negative')
