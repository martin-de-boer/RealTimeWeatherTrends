from neca.events import *
from datetime import *
from official_handling import config

def add_hoverable_marker(coords, info_text):
    emit("map_key", {
        "action": "draw",
        "type": "marker",
        "name": coords,
        "coordinates": coords,  # Coordinates as [latitude, longitude]
        "options": {
            "title": info_text
        }
    })

def is_exist(s):
    return s != None

def calculate_avg(data):
        
    #calculate the average of temperatures
    c0 = sum([data[i][0] for i in range(len(data))])/len(data)
    c1 = sum([data[i][1] for i in range(len(data))])/len(data)

    #return a list for the emit
    return [c1, c0]

def handler(data):
    emit("x", data)
    
    if is_exist(data["geo"]):
        add_hoverable_marker(data["geo"]["coordinates"], data["text"])
        
    elif is_exist(data["place"]["bounding_box"]):
        coords = data["place"]["bounding_box"]["coordinates"][0]
        add_hoverable_marker(calculate_avg(coords), data["text"])