from datetime import *
from official_handling.formatAux import *

def official(tweet_data):
    
    #actual date of the tweet
    date_ = datetime.strptime(tweet_data["created_at"], '%a %b %d %H:%M:%S %z %Y')
    
    #text of the tweet
    text = tweet_data["text"]
    
    #hour minute and second of the prediction time
    phour = int(text.split('-')[0].split(':')[0])
    pminute = int(text.split('-')[0].split(':')[1])
    psecond = int(text.split('-')[0].split(':')[2])
    
    #creating a whole datetime structure for prediction time
    #by taking the next datetime after the tweet_datetime
    ptime = next_datetime(date_,hour = phour, minute = pminute, second = psecond)
    
    #extract strings for all values
    
    parts = text.split('|')
    
    temp = parts[0].split('T.')[1].strip().split('\u00ba')[0].replace(',', '.')
    hum = parts[1].split('Hum ')[1].split('%')[0].strip()
    
    wind_speed = parts[1].split('wind ')[1].split(' m')[0].replace(',', '.').strip()
    wind_force = parts[1].split('F')[1].split('bft')[0].strip()
    wind_direction = parts[1].split(').')[1].strip()
    
    pressure = parts[2].split('hPa.')[0].strip().replace(',', '.')
    pressure_change = parts[2].split('hPa.')[1].strip()
    
    rain = parts[3].split('rain ')[1].split(' mm')[0].strip().replace(',', '.')
    uv = parts[4].split('Uv ')[1].strip().replace(',', '.')
    
    location = parts[5].split(' #')[1]
    
    #this dict will be in tweet_data["weather_data"]
    weather_data = {
        "ptime": ptime, #usually ~ date + 1/2 hour
        "temperature": float(temp), #centigrades
        "humidity": float(hum)/100, #%
        "wind_speed": float(wind_speed), #m/s
        "wind_force": float(wind_force), #on Beaufort Wind Scale: 1 to 12
        "wind_direction": wind_direction, #3 characters, or "---" usually if wind_speed == 0
        "pressure": float(pressure), #hPa
        "pressure_change": pressure_change, #Rising/Steady/Falling
        "rain": float(rain), #mm
        "uv": float(uv),
        "location": location #Buren
    }
    
    tweet_data["weather_data"] = weather_data
    
    return tweet_data