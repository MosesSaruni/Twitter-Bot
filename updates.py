import tweepy
import time

consumer_key = 'FR1xqvPDH7zX5pSI9ScEGLbk8'
consumer_secret = 'YuITQpdHlNIkDdFZDfVQ6DLA6leKZhgyh8RWsFHEeyKTfPfJTO'

key = '1480473183388119045-2kx5UfM1ggZvp1sWom0yioy9Yp0Mik'
secret = 'BxGcqdRhoISaCEd0U08v6XBEaKg42XaaxyBUxEqgekQQA'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)


def media_upload():
    status = "I just Uploaded a new image !!"
    filename = "bltz.jpg"
    api.update_with_media(filename, status)

def new_tweet():
    status = "Hello! This is a tweet from the twitter bot I built😁"
    api.update_status(status)

new_tweet()
media_upload()

