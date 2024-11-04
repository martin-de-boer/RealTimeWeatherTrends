from neca.events import *
from datetime import *
from official_handling import config

def add_hoverable_marker(coords, info_text):
    emit("map", {
        "action": "draw",
        "type": "marker",
        "name": "hover_marker",
        "coordinates": coords,  # Coordinates as [latitude, longitude]
        "options": {
            "title": "Marker",  # Tooltip title on hover
            "popup": info_text  # Popup text to display on hover
        }
    })

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def calculate_avg(data):
        
    #calculate the average of temperatures
    c0 = sum([data[i][0] for i in range(len(data))])/len(data)
    c1 = sum([data[i][1] for i in range(len(data))])/len(data)

    #return a list for the emit
    return [c1, c0]

def handler(data):
    if is_number(data["geo"]["coordinates"][0]):
        add_hoverable_marker(data["geo"]["coordinates"], data["text"])
    elif is_number(data["place"]["bounding_box"]["coordinates"][0][0][0]):
        coords = data["place"]["bounding_box"]["coordinates"][0]
        add_hoverable_marker(calculate_avg(coords), data["text"])
        