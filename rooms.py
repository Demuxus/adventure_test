class Character():
	def __init__(self, coords, name, inventory):
		pass
class Room():
	def __init__(self, coords, name, desc, contents, locks):
		self.coords = coords
		self.name = name
		self.desc = desc
		self.contents = contents
		self.locks = locks
	def lockdirection(self, locks, keyuse):
		pass

