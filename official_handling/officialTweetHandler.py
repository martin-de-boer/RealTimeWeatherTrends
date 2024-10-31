from neca.events import *
from datetime import *
from official_handling import config
from official_handling.dailyEmits import *

#next day condition
def next_day(values,new_data):
    return values[0]["weather_data"]["ptime"].day != new_data["weather_data"]["ptime"].day

#next_hour condition
def next_hour(values,new_data):
    return values[0]["weather_data"]["ptime"].hour != new_data["weather_data"]["ptime"].hour


def handler(data, daily_key):
    #if this is the first value, initialize
    if config.hour_values == []:
        daily_reset(daily_key)
        config.hour_values.append(data)

    #if next_day reset daily charts
    else:
        if next_day(config.hour_values, data):
            daily_reset(daily_key)

            #in next_hour reset hour_values
        if next_hour(config.hour_values, data):
            config.hour_values = []

        config.hour_values.append(data)
        
    #for logging time of tweet
    tweet_datetime = datetime.strftime(config.hour_values[-1]["weather_data"]["ptime"],"%Y/%m/%d, %H:%M:%S")
    emit("log", tweet_datetime)
    print(tweet_datetime)
    
    #emit to dily temperature+rain chart
    daily_emit(daily_key)