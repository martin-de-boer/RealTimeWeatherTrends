import neca
from neca.events import *
from neca.generators import generate_data
from datetime import *
from official_handling import formatTweet
from official_handling import config
from official_handling import officialTweetHandler


#decide if official or discussion
@event("tweet")
def tweet_handler(context, data):
    if data["user"]["id"] == 197131172:
        #if official call handler with formatted data
        officialTweetHandler.handler(formatTweet.official(data), config.daily_key)
    else:
        #just emit the tweet to the feed
        emit("x", data)
        #call discussion_handler here for map etc..


def generate_tweets():
    generate_data(
        data_file = "data/weer.json", # file location
        time_scale = 40000, # time speedup factor
        event_name = 'tweet', # to which event is the data sent
    )

@event("init")
def init(context,data):
    generate_tweets()
    

@event("connect")
def connect(context,data):
    print("connected")  

config.init()

neca.start()