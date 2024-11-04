from neca.events import *
from datetime import *
from official_handling import config
import numpy as np

def prediction_reset(data):
    
    emit(config.prediction_key, {
    "action": "remove",
    })
    
    i = 0
    while i < len(config.prediction_values):
        if (config.prediction_values[i]["weather_data"]["ptime"] - data["created_at"]).total_seconds() < 600:
            config.prediction_values.pop(i)
        i = i+1


            
def prediction_emit():
    
    # Original ptime values in minutes
    ptime_raw = [int(np.floor((i["weather_data"]["ptime"] - config.start_time).total_seconds() / 60)) for i in config.prediction_values]

    ptime = [t - ptime_raw[0] for t in ptime_raw]
    
    #emit temperature
    data = [i["weather_data"]["temperature"] for i in config.prediction_values]
    
    vals = [list(i) for i in zip(ptime, data)]
    for i in range(len(vals)):
        vals[i].append(0)
    
    for i in vals:
        emit(config.prediction_key, {
        "action" : "set",
        "value" : i
        })
    
    
    #emit rain
    data = [i["weather_data"]["rain"] for i in config.prediction_values]
    
    vals = [list(i) for i in zip(ptime, data)]
    for i in range(len(vals)):
        vals[i].append(1)
    
    for i in vals:
        emit(config.prediction_key, {
        "action" : "set",
        "value" : i
        })