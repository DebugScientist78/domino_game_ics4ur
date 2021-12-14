import DominosPile
import random

class Deque:
	def __init__(self, ls=[]):
		self.deq = ls[:]
	def appendL(self, data):
		self.deq.append(data)
	def appendR(self, data):
		ls = [data]
		self.deq = self.deq + ls
	def popL(self):
		self.deq.pop(0)
	def popR(self):
		self.deq.pop(-1)


class GameBoard:
	def __init__(self):
		self.board = Deque()
		self.pile = DominosPile.DominosPile()
	def get_dom_expr(self):
		a = random.randint(0,12)
		b = random.randint(0,12)
		#order the ints such that the larger is in front
		expr = str(a)+'|'+str(b)
		if b > a:
			expr = str(b)+'|'+str(a)
		return expr

	def grabStartHand(self):
		''' 
		Grab 7 dominos from the pile and return them as a list
		'''
		ls = []
		for x in range(7):
			expr = self.get_dom_expr()
			while True:
				#prevent dupes
				if self.pile.dom_dict[expr] == "v":
					expr = self.get_dom_expr()
				else:
					break
			self.pile.dom_dict[expr] = "v"
			ls.append(expr)
		return ls
