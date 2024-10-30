import neca
from neca.events import *

@event("init")
def init(context, data):
	print("init")

@event("connect")
def connect(context, data):
	print("connection")
	emit("dailyTempChart", {
		"action": "data",
		"value": {
			'datasets': [{
				'label': 'Temperature',
				'data': [10,0,10,10,9]
			}],
			'labels': [0,1,2,3,4,5],
		}
	})
	

neca.start()
