#IMPORTS -BRINGING STUFF IN#
from functions import *
from rooms import *
#THIS VARIABLE CONTROLS THE GAME LOOP - WHILE IT"S TRUE IT KEEPS THE GAME OPEN#
gamerunning= True
inputerror = False
	
#STARTING ROOM#
location = (1, 1) #This is the location where the player starts. (1, 1), for example, is the position of room "centre"

#MAIN GAME LOOP#
while gamerunning == True:
	
	#ROOM ENTRY#
	
	
	
	try:
		#if playerinput
		playerinput = (input('>>> ')).lower()
		
		playerlist = playerinput.split(" ")
		
		if playerlist[0] == "go":
			if playerlist[1] == "n":
				print ("north")
			if playerlist[1] == "e":
				print ("east")
			if playerlist[1] == "s":
				print ("south")
			if playerlist[1] == "w":
				print ("west")
	
	except ValueError:
		pass
	 
   


