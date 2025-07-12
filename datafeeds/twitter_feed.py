import tweepy
import os

API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET = os.getenv("TWITTER_API_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")

def fetch_tweets(keywords=["inflation", "fed", "oil", "AI"], count=10):
    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    
    tweets = []
    for keyword in keywords:
        for tweet in api.search_tweets(q=keyword, count=count, lang="en", tweet_mode="extended"):
            tweets.append({
                "user": tweet.user.screen_name,
                "text": tweet.full_text,
                "keyword": keyword,
                "time": tweet.created_at
            })
    return tweets