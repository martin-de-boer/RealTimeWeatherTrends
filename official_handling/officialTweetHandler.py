from neca.events import *
from datetime import *
from official_handling import config
from official_handling.dailyEmits import *
from official_handling.predictionEmits import *

#next day condition
def next_day(values,new_data):
    return values[0]["weather_data"]["ptime"].day != new_data["weather_data"]["ptime"].day

#next_hour condition
def next_hour(values,new_data):
    return values[0]["weather_data"]["ptime"].hour != new_data["weather_data"]["ptime"].hour


#DAILY VALUES ---------------------------------------------------------------------------------------

def daily_handler(data):
        #if this is the first value, initialize
    if config.hour_values == []:
        daily_reset()
        config.hour_values.append(data)

    #if next_day reset daily charts
    else:
        if next_day(config.hour_values, data):
            daily_reset()

        #in next_hour reset hour_values
        if next_hour(config.hour_values, data):
            config.hour_values = []

        config.hour_values.append(data)
        
    #emit to dily temperature+rain chart
    daily_emit()

#PREDICTION VALUES ---------------------------------------------------------------------------------------

def prediction_handler(data):
    #if this is the first value, initialize
    
    config.prediction_values.append(data)
    
    prediction_reset(data)
    prediction_emit()


#HANDLER ---------------------------------------------------------------------------------------
def handler(data):
    print(data["created_at"])
    daily_handler(data)
    prediction_handler(data)