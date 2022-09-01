import tweepy
import time

consumer_key = 'FR1xqvPDH7zX5pSI9ScEGLbk8'
consumer_secret = 'YuITQpdHlNIkDdFZDfVQ6DLA6leKZhgyh8RWsFHEeyKTfPfJTO'

key = '1480473183388119045-2kx5UfM1ggZvp1sWom0yioy9Yp0Mik'
secret = 'BxGcqdRhoISaCEd0U08v6XBEaKg42XaaxyBUxEqgekQQA'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

hashtag = "#Euphoria"
tweetnumber = 10

tweets = tweepy.Cursor(api.search, hashtag).items(tweetnumber)

def searchBot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet done")
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)

searchBot()