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
	board = Deque()
	pile = DominosPile.DominosPile()
	
	@staticmethod
	def getDomExpr(a, b):
		'''
		Assume a > b, put the two integers into a string domino form
		'''
		return str(a)+'|'+str(b)

	@staticmethod
	def getRanDomExpr():
		a = random.randint(0,12)
		b = random.randint(0,12)
		#order the ints such that the larger is in front
		if b > a:
			return GameBoard.getDomExpr(b,a)
		return GameBoard.getDomExpr(a,b)

	@staticmethod
	def getDomNum(expr):
		#returns the ints from a domino string
		a,b = expr.split("|")
		a = int(a)
		b = int(b)
		return a,b


	@staticmethod
	def grabStartHand():
		''' 
		Grab 7 dominos from the pile and return them as a list
		'''
		ls = []
		for x in range(7):
			expr = GameBoard.getRanDomExpr()
			while True:
				#prevent dupes
				if GameBoard.pile.dom_dict[expr] == "v":
					expr = GameBoard.getRanDomExpr()
				else:
					break
			GameBoard.pile.dom_dict[expr] = "v"
			ls.append(expr)
		return ls
