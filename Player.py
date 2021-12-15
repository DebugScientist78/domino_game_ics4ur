class Player:
	def __init__(self):
		self.hand = []
		self.name = ""

	def __str__(self):
		return "NAME: " + self.name + " | HAND: " + self.hand.__str__()

	def __repr__(self):
		return "NAME: " + self.name + " | HAND: " + self.hand.__str__()

	def removeDom(self, index):
		self.hand.pop(index)

	def doesHandHave(self, expr):
		for x in self.hand:
			if x == expr:
				return True
		return False