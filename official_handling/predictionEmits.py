from neca.events import *
from datetime import *
from official_handling import config

def prediction_reset(data):
    i = 0
    while i < len(config.prediction_values):
        if (config.prediction_values[i]["weather_data"]["ptime"] - data["created_at"]).total_seconds() < 600:
            config.prediction_values.pop(i)
        i = i+1
    
    emit(config.prediction_key, {
    "action" : "reset",
    "series" : "temperature",
    })
    
    emit(config.prediction_key, {
    "action" : "reset",
    "series" : "rain",
    })    

            
def prediction_emit():
    
    ptime = [(i["weather_data"]["ptime"] - config.start_time).total_seconds() / 60 for i in config.prediction_values]
    
    
    #emit temperature
    data = [i["weather_data"]["temperature"] for i in config.prediction_values]
    
    vals = [list(i) for i in zip(ptime, data)]

    emit(config.prediction_key, {
    "action" : "set",
    "series" : "temperature",
    "value" : vals
    })
    
    
    #emit rain
    data = [i["weather_data"]["rain"] for i in config.prediction_values]
    
    vals = [list(i) for i in zip(ptime, data)]
    
    emit(config.prediction_key, {
    "action" : "set",
    "series" : "rain",
    "value" : vals
    })