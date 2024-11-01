from neca.events import *
from datetime import *
from official_handling import config

def prediction_reset(data):
    for i in range(len(config.prediction_values)):
        if (config.prediction_values[i]["weather_data"]["ptime"] - data["created_at"]).total_seconds() < 600:
            config.prediction_values.pop(i)
            
    #need scrolling or smth if time passes but no new tweets arrive
            
def prediction_emit():
    
    #needs working on format for label
    
    data = [config.prediction_values[-1]["weather_data"]["ptime"],config.prediction_values[-1]["weather_data"]["temperature"]]
    #emit temperature
    emit(config.prediction_key, {
    "action" : "set",
    "value" : data
    })
    
    data = [config.prediction_values[-1]["weather_data"]["ptime"],config.prediction_values[-1]["weather_data"]["rain"]]
    #emit rain
    emit(config.prediction_key, {
    "action" : "set",
    "value" : data
    })