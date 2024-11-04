import neca
from neca.events import *
from neca.generators import generate_data
from datetime import *
from official_handling import formatTweet
from official_handling import config
from official_handling import officialTweetHandler
from official_handling import discussionTweetHandler

#decide if official or discussion
@event("tweet")
def tweet_handler(context, data):
    
    if config.start_time == 0:
        config.start_time = datetime.strptime(data["created_at"], '%a %b %d %H:%M:%S %z %Y')
    
        
    if data["user"]["id"] == config.official_id:
        
        #if official, call handler with formatted data
        officialTweetHandler.handler(formatTweet.official(data))
            
    else:
        discussionTweetHandler.handler(formatTweet.discussion(data))


def generate_tweets():
    generate_data(
        data_file = "data/weer.json", # file location
        time_scale = 1000, # time speedup factor
        event_name = 'tweet', # to which event is the data sent
    )

@event("init")
def init(context,data):
    generate_tweets()

@event("connect")
def connect(context,data):
    print("connected")

neca.start()