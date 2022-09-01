import tweepy
import time

consumer_key = 'FR1xqvPDH7zX5pSI9ScEGLbk8'
consumer_secret = 'YuITQpdHlNIkDdFZDfVQ6DLA6leKZhgyh8RWsFHEeyKTfPfJTO'

key = '1480473183388119045-2kx5UfM1ggZvp1sWom0yioy9Yp0Mik'
secret = 'BxGcqdRhoISaCEd0U08v6XBEaKg42XaaxyBUxEqgekQQA'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)



FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id =  int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode = 'extended')
    for tweet in reversed(tweets):
        if '#bltzbot' in tweet.full_text.lower():
            print(str(tweet.id) + ' - ' + tweet.full_text)
            api.update_status("@" + tweet.user.screen_name + " Auto reply, like and retweet works!!", tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME, tweet.id)

while True:
    reply()
    time.sleep(15)

