#csv is a python lib that allows read/write csv files.
import csv

	#DECLARING VARIABLES#
xpos = 0
xcounter = 0
ycounter = 0
csvmap = []
gamemap = []

	#CSV TABLE TO LIST ARRAY CONVERTER#
#This is a standard code for reading a csv file, this could be remote on a server non native
with open('map.csv', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		#xpos AND ypos FIND OUT TOTAL TABLE SIZE#
		xpos = len(row)
		
		#MAKES A 2D ARRAY (not AR-RAY)CONTAINING THE X AND Y AND ROOM NAME DATA FOR EACH LIST CHUNK#
		while xcounter < xpos:
			csvmap.append([[xcounter, ycounter],[row[xcounter]]])
			xcounter = xcounter + 1
			
			print (xcounter, ycounter)

		#ITERATES AND RESETS THE XCOUNTER AND YCOUNTER VALUES TO PROPERLY FORMAT THE csvmap#
		xcounter = 0
		ycounter = ycounter +1

#---------------------#

#PROOF OF CONCEPT - SEARCHES csvmap FOR EACH ITEM WHERE THE NAME ISN'T EMPTY#
for i in csvmap:
	for data in i[1]:
		if data != "":
			#PRINTS THE COORDINATES AND THE NAME OF THE ITEM#
			gamemap.append([[i[0]], [i[1]]])
print (gamemap)
