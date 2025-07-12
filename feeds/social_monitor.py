Below is a Python script that monitors social media platforms for changes in sentiment and influencer-driven trends. This script uses Tweepy to access the Twitter API for real-time tweets and VADER from the NLTK library for sentiment analysis. It tracks specified keywords and evaluates the sentiment of tweets to detect shifts in public opinion. Make sure to install the necessary libraries and obtain Twitter API credentials before running the script.

```python
import tweepy
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import json

# Twitter API credentials
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Sentiment Analysis Setup
sid = SentimentIntensityAnalyzer()

# Define the keywords to track
keywords = ['keyword1', 'keyword2', 'influencer']

# Define a class inheriting from StreamListener to process the incoming tweets
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        # Extract text from the tweet
        tweet_text = status.text
        
        # Perform sentiment analysis on the tweet
        sentiment_score = sid.polarity_scores(tweet_text)
        
        # Print the tweet and its sentiment score
        print(f"Tweet: {tweet_text}")
        print(f"Sentiment Score: {sentiment_score}")
        
        # Check for significant sentiment shift or influencer mention
        if sentiment_score['compound'] > 0.5 or any(influencer in tweet_text.lower() for influencer in keywords):
            print("Significant positive sentiment or influencer mention detected!")
        elif sentiment_score['compound'] < -0.5:
            print("Significant negative sentiment detected!")

    def on_error(self, status_code):
        if status_code == 420:
            # Returning False disconnects the stream
            return False

# Initialize the stream
my_stream_listener = MyStreamListener()
my_stream = tweepy.Stream(auth=api.auth, listener=my_stream_listener)

# Start streaming tweets that contain the specified keywords
my_stream.filter(track=keywords)
```

### Instructions:
1. Replace `'YOUR_CONSUMER_KEY'`, `'YOUR_CONSUMER_SECRET'`, `'YOUR_ACCESS_TOKEN'`, and `'YOUR_ACCESS_TOKEN_SECRET'` with your actual Twitter API credentials.
2. Modify the `keywords` list to include the specific keywords or influencer names you want to monitor.
3. Install the required libraries if you haven't already:
   - Install Tweepy: `pip install tweepy`
   - Install NLTK and download VADER lexicon:
     ```python
     import nltk
     nltk.download('vader_lexicon')
     ```
4. Run the script to start monitoring tweets. Adjust the sentiment thresholds as needed based on your specific requirements for detecting sentiment shifts.