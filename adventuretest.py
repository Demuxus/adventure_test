#IMPORTS -BRINGING STUFF IN#
from functions import *
#THIS VARIABLE CONTROLS THE GAME LOOP - WHILE IT'S TRUE IT KEEPS THE GAME OPEN#
gamerunning= True
inputerror = False

#LOCATIONS IN THE GAME#
bridge = ('Captains Bridge', 'the bridge of the ship, complete with a captains chair.')
lift = ('Space Lift', 'the lift that can take you various places in the ship.')
engine_room = ('Engine Room', 'the gentle humming of the ion thrusters are quite calming.')
centre = ('Centre Room', 'The hub of the spaceship.')
airlock = ('The Airlock', 'the Airlock. You need a keycard to open the outer airlock door!')


#ROOM TRANSITION CONDITIONS DICTIONARY#
transitions = {
	centre: (lift, engine_room, bridge, airlock),
	bridge: (centre,),
	engine_room: (centre,),
	lift: (centre,),
	airlock: (centre,)
	}

#STARTING ROOM#
location = centre

#MAIN GAME LOOP#
while gamerunning == True:
	
	#ROOM ENTRY#
	
	entryroom(inputerror, location, transitions)

	playerinput = int(input('Choice: '))
	
	if playerinput <= len(transitions[location]) and playerinput >= 1:
		location = transitions[location][playerinput - 1]
		inputerror = False
	else:
		print ('\r')
		print ('That location does not exist, please try again\n') 
		inputerror = True
	
	
	
	 
   


