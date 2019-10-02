
# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import os
# Variables that contains the user credentials to access Twitter API 
access_token = "1128488703255465984-VNEkApDcACGuAPf1P2Vs3v2WqhRiC3"
access_token_secret = "q9Jyj392gIWxOcaN0SQji3FKrvglZMKwli52tzCDRyJfO"
ckey = "KLolDdtqq9nqv2t79M1GjN70v"
consumer_secret = "IHk0p9tr8JmbVXJYSW1oBgajfqR5VDDuyadari7UdeKGJYsrBn"

#grabs the system time
start_time = time.time()

#track list
keyword_list = ['twitter']

#Geo Locations
GEOBOX_WORLD = [-180,-90,180,90]
GEOBOX_GERMANY = [5.0770049095, 47.2982950435, 15.0403900146, 54.9039819757]

#listener that just prints received tweets to stdout.
class Listener(StreamListener):
    def __init__(self, start_time, time_limit=60):
        self.time = start_time
        self.limit = time_limit
        self.tweet_data = []
    def on_data(self, data):
        saveFile = open('twitter_data.json', 'a', encoding='utf-8')
        while (time.time() - self.time) < self.limit:
            
            try:
                self.tweet_data.append(data)
                return True

            except BaseException as e:
                print ('failed ondata,', str(e))
                time.sleep(5)
                pass

        saveFile = open('twitter_data.json', 'w', encoding='utf-8')
        saveFile.write(u'{\n "tweets":[\n')
        saveFile.write(','.join(self.tweet_data))
        saveFile.write(u'\n]\n}')
        saveFile.close()
        exit()

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, consumer_secret) #OAuth object
auth.set_access_token(access_token, access_token_secret)


twitterStream = Stream(auth, Listener(start_time, time_limit=60)) #initialize Stream object with a time out limit
#twitterStream.filter(locations=GEOBOX_GERMANY)  #call the filter method to run the Stream Object
twitterStream.filter(locations=GEOBOX_WORLD, languages=["de"]) # This line filter Twitter Streams to capture data by the keywords

'''

if __name__ == '__main__':

    #This handles Twitter Auth and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    # Online-Tool to create boxes (c+p as raw CSV): http://boundingbox.klokantech.com/
    GEOBOX_WORLD = [-180,-90,180,90]
    GEOBOX_GERMANY = [5.0770049095, 47.2982950435, 15.0403900146, 54.9039819757]
    #Savefile
    saveFile = io.open('raw_tweets.json', 'a', encoding='utf-8')

    # This line filter Twitter Streams to capture data by the keywords
    #stream.filter(track=['ich'])

    #This line filter Twitter Streams to capture data by the location
    stream.filter(locations=GEOBOX_GERMANY)

'''