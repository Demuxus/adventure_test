from csvreader import gamemap
#CREATING ROOM CLASS THAT CAN BE USED TO MAKE A ROOM INSTANCE#
class Room:
	def __init__(self, name, desc, contents, locks):
		self.name = name
		self.desc = desc
		self.contents = contents
		self.locks = locks
		
	def mappos(self):
		for i in gamemap:
			for data in i[1]:
				if data == self.name:
					print (i[0])

			
centre = Room('centre', 'empty', '', '',)

print (centre.mappos())
