from neca.events import *
from datetime import *
from official_handling import config

#checks if the hour value of the two inputs is the same
def next_hour(values,new_data):
    return values["text"][0]["ptime"].hour != new_data["ptime"].hour

#calculate avg temperature from config.hour_values
def calculate_avg():
        
    #extract hour value of the first element in config.hour_values
    hour = int(datetime.strftime(config.hour_values[0]["weather_data"]["ptime"], "%H"))

    #calculate the average of temperatures
    data = sum([config.hour_values[i]["weather_data"]["temperature"] for i in range(len(config.hour_values))])/len(config.hour_values)

    #return a list for the emit
    return [hour,data,0]

#calculate sum of rain data from config.hour_values
def calculate_sum():

    #extract hour value of the first element in config.hour_values
    hour = int(datetime.strftime(config.hour_values[0]["weather_data"]["ptime"], "%H"))

    #calculate the sum of rain data
    data = sum([config.hour_values[i]["weather_data"]["rain"] for i in range(len(config.hour_values))])
        
    #return a list for the emit    
    return [hour,data,1]

def daily_emit():
        
    #emit temperature
    data = calculate_avg()
    emit(config.daily_key, {
    "action" : "set",
    "value" : data
    })
    
    #emit rain
    data = calculate_sum()
    emit(config.daily_key, {
    "action" : "set",
    "value" : data
    })

#resets the rain + temp chart values
def daily_reset():
    print("reset")
    emit(config.daily_key, {
    "action" : "reset",
    })
