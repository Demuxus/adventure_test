#IMPORTS -BRINGING STUFF IN#
from functions import *
#THIS VARIABLE CONTROLS THE GAME LOOP - WHILE IT'S TRUE IT KEEPS THE GAME OPEN#
gamerunning= True
inputerror = False

#LOCATIONS IN THE GAME#
bridge = ('Captains Bridge', 'the bridge of the ship, complete with a captains chair.')
lift = ('Space Lift', 'the lift that can take you various places in the ship.')
engine_room = ('Engine Room', 'the gentle humming of the ion thrusters are quite calming.')
centre = ('Centre Room', 'the hub of the spaceship.')
airlock = ('The Airlock', 'the Airlock. You need a keycard to open the outer airlock door!')
observation = ('The Observation Platform', 'the Observation Platform, a large glass window enbales a view into the void of space.')
communications = ('The Communications Tower', 'the Communications Tower is your only means of contact with all external to the space station, without it fully functioning, nobody knows you exsist.')
subdecka = ('Sub Deck Alpha', 'a lower deck where crew members sleep and reside off watch.')
subdeckb = ('Sub Deck Beta', 'a lower deck which also houses the main life support systems for the ship.')
subdeckc = ('Sub Deck Charlie', 'a lower deck mainly used for container storage.')

#ROOM TRANSITION CONDITIONS DICTIONARY#
transitions = {
	centre: (lift, engine_room, bridge, airlock),
	bridge: (centre,),
	engine_room: (centre,),
	lift: (centre, observation, communications, subdecka, subdeckb, subdeckc),
	airlock: (centre,),
	observation: (lift,),
	communications: (lift,),
	subdecka: (lift,),
	subdeckb: (lift,),
	subdeckc: (lift,),
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
	
	
	
	 
   


