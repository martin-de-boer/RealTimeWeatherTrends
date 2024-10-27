import neca
from neca.events import *

@event("init")
def init(context, data):
	print("init")

@event("connect")
def connect(context, data):
	emit("tempchart_data", {
		"action": "set",
		"value": ["Sunday", 10]
	})

	emit("rainchart_data", {
		"action": "add",
		"value": ["Monday", 20]
	})

	emit("windchart_data", {
		"action": "add",
		"value": ["Monday", 20]
	})


# starts the server and prevents the program from exiting
neca.start()