#IMPORTS -BRINGING STUFF IN#
from functions import *
from rooms import *
#THIS VARIABLE CONTROLS THE GAME LOOP - WHILE IT"S TRUE IT KEEPS THE GAME OPEN#
gamerunning= True
inputerror = False
	
#STARTING ROOM#
location = centre

#MAIN GAME LOOP#
while gamerunning == True:
	
	#ROOM ENTRY#
	
	entryroom(inputerror, location, transitions)

	playerinput = input('Choice: ')
	try:
		playerinput = int(playerinput)
		if int(playerinput) <= len(transitions[location]) and int(playerinput) >= 1:
			location = transitions[location][int(playerinput) - 1]
			inputerror = False
	
		else:
			print ('\r')
			print ('That location does not exist, please try again\n') 
			inputerror = True
	except ValueError:
	
		print ("\n***That's not right!***")

		print ("\n")
	
	 
   


