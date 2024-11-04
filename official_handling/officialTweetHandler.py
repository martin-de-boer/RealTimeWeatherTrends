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

def daily_handler(data):
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

def prediction_handler(data):
    
    config.prediction_values.append(data)
    prediction_reset(data)
    prediction_emit()

#PREDICTION VALUES ---------------------------------------------------------------------------------------

def general_info(data):
    emit ("log_loc_key", {
        "message": str(data["place"]["full_name"])
    })
    
    emit("log_temp_key",{
        "message": str(data["weather_data"]["temperature"])
    })
    
    emit("log_rain_key",{
        "message": str(data["weather_data"]["rain"])
    })
    
    emit("log_uv_key",{
        "message": str(data["weather_data"]["uv"])
    })
    
    emit("log_wd_key",{
        "message": str(data["weather_data"]["wind_direction"])
    })
    
    emit("log_wf_key",{
        "message": str(data["weather_data"]["wind_force"])
    })
    
    emit("log_ws_key",{
        "message": str(data["weather_data"]["wind_speed"])
    })
    
    emit("log_hum_key",{
        "message": str(data["weather_data"]["humidity"])
    })
    
    emit("log_ps_key",{
        "message": str(data["weather_data"]["pressure"])
    })
    
    emit("log_ps_change_key",{
        "message": str(data["weather_data"]["pressure_change"])
    })

#HANDLER ---------------------------------------------------------------------------------------
def handler(data):
    print(data["created_at"])
    daily_handler(data)
    prediction_handler(data)
    general_info(data)
    