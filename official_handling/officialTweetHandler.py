from neca.events import *
from datetime import *
from official_handling import config
from official_handling.dailyEmits import *
from official_handling.predictionEmits import *

#next day condition
def next_day(values,new_data):
    return values[0]["weather_data"]["ptime"].day != new_data.day

#next_hour condition
def next_hour(values,new_data):
    return values[0]["weather_data"]["ptime"].hour != new_data.hour


#DAILY VALUES ---------------------------------------------------------------------------------------

def daily_handler(data, isTweet):
    #if not tweet just do resets if needed
    if not isTweet:
        if next_day(config.hour_values, data["created_at"]):
            daily_reset()
        if next_hour(config.hour_values, data["created_at"]):
            config.hour_values = []
            
    else:
        #if this is the first value, initialize
        if config.hour_values == []:
            daily_reset()
            config.hour_values.append(data)

        #if next_day reset daily charts
        else:
            if next_day(config.hour_values, data["weather_data"]["ptime"]):
                daily_reset()

            #in next_hour reset hour_values
            if next_hour(config.hour_values, data["weather_data"]["ptime"]):
                config.hour_values = []

            config.hour_values.append(data)
            
        #emit to daily temperature+rain chart
        daily_emit()

#PREDICTION VALUES ---------------------------------------------------------------------------------------

def prediction_handler(data, isTweet): # is not a tweet
    if not isTweet:
        prediction_reset(data)
    
    else: # is a tweet
        config.prediction_values.append(data)
        prediction_reset(data)
        prediction_emit()


#HANDLER ---------------------------------------------------------------------------------------
def handler(data, isTweet):
    print(data["created_at"])
    daily_handler(data, isTweet)
    prediction_handler(data, isTweet)