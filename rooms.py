#IMPORTING THE ARRAY MAP FROM CSVREADER#
from csvreader import gamemap
from functions import *

#CREATING ROOMDICT#
roomdict = {}

#CREATING ROOM CLASS THAT CAN BE USED TO MAKE A ROOM INSTANCE#
class Room:
	
	roomtotal = 0
	
	def __init__(self, iname, name, desc, contents, locks):
		
		self.iname = iname
		self.name = name
		self.desc = desc
		self.contents = contents
		self.locks = locks
		
		Room.roomtotal += 1
		
		for i in gamemap:
			if i[2] == self.iname:
				self.x = int(i[0])
				self.y = int(i[1])
				self.coordinates = (self.x, self.y)
				roomdict.update({(self.coordinates):self.contents})


# ROOM INSTANCES: #
bridge = Room("bridge", "Bridge", "the bridge of the ship, complete with a captains chair.", ["Captain\'s chair", "Scrap of Paper"], "")
lift = Room("lift", "Lift", "the lift that can take you various places in the ship.", ["Buttons"], "")
engine = Room("engine", "Engine Room", "the engine room. The gentle humming of the ion thrusters are quite calming.", ["Wrench"], "")
centre = Room("centre", "Central Hub", "the central hub room of the spacecraft.", [], "")
airlock = Room("airlock", "Airlock", "the Airlock. You need a keycard to open the outer airlock door!", [], "")
observ = Room("observ", "Observatory Tower", "the Observation Tower, a large glass window enbales a view into the fathomless void of space.", [], "")
comms = Room("comms", "Communications Tower", "the Communications Tower is your only means of contact with all external to the space station. Without it fully functioning, nobody knows you exsist.", [], "")
subdecka = Room("subdecka", "Subdeck Alpha", "a lower deck where crew members sleep and reside off watch.", [], "")
subdeckb = Room("subdeckb", "Subdeck Bravo", "a lower deck which also houses the main life support systems for the ship.", [], "")
subdeckc = Room("subdeckc", "Subdeck Charlie", "a lower deck mainly used for container storage.", [], "")

print("Room Dictionary: ", roomdict)
print ("\n{}\n\n".format("-"*15))
print ("Total Room Count: ", Room.roomtotal)
