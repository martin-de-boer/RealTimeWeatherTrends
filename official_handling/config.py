daily_key = "daily_chart_key"
prediction_key = ""

def init():
    #contains all data of official tweets for the hour
    global hour_values
    hour_values = []
    
    #contains predicton data
    global prediction_values
    prediction_values = []