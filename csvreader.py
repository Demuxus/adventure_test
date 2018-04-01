#csv is a python lib that allows read/write csv files.
import csv

	#DECLARING VARIABLES#
xpos = 0
xcounter = 0
ycounter = 0
gamemap = []
gamemap = []

#CSV TABLE TO LIST ARRAY CONVERTER#
	
#CODE FOR OPENING A CSV FILE, CAN BE USED ANYWHERE A CSV TABLE IS STORED - EVEN REMOTELY IF THE PATH IS SPECIFIED#
#r = READABLE#
with open("map.csv", "r") as csvfile:
	reader = csv.reader(csvfile, delimiter=",")
	for row in reader:
		#xpos USED TO FIND OUT FINAL POSITION OF CURRENT ROW#
		xpos = len(row)
		
		#MAKES A 2D ARRAY (not AR-RAY)CONTAINING THE X AND Y AND ROOM NAME DATA FOR EACH LIST CHUNK#
		while xcounter < xpos:
			if row[xcounter] != "":
				gamemap.append([xcounter, ycounter, row[xcounter]])
			xcounter = xcounter + 1

		#ITERATES AND RESETS THE XCOUNTER AND YCOUNTER VALUES TO PROPERLY FORMAT THE gamemap#
		xcounter = 0
		ycounter = ycounter +1
