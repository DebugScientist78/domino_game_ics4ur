class Player:
	def __init__(self):
		self.hand = []
		self.name = ""

	def __str__(self):
		return "NAME: " + self.name + " | HAND: " + self.hand.__str__()

	def __repr__(self):
		return "NAME: " + self.name + " | HAND: " + self.hand.__str__()