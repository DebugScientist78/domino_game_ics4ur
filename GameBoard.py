import DominosPile
import random

class Deque:
	def __init__(self, ls=[]):
		self.deq = ls[:]
	def appendR(self, data):
		self.deq.append(data)
	def appendL(self, data):
		ls = [data]
		self.deq = ls + self.deq
	def popL(self):
		self.deq.pop(0)
	def popR(self):
		self.deq.pop(-1)
	def getL(self):
		return self.deq[0]
	def getR(self):
		return self.deq[-1]


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

	@staticmethod
	def getRemainPile():
		ls = []
		for key in GameBoard.pile.dom_dict:
			if GameBoard.pile.dom_dict[key] != 'v':
				ls.append(key)
		return ls

	@staticmethod
	def validDominos(hand):
		'''
		given an string array of dominos, check to see if any of them are valid to play
		return False if none, return a list of valid options
		'''
		l = GameBoard.getDomNum(GameBoard.board.getL())[0]
		r = GameBoard.getDomNum(GameBoard.board.getR())[1]
		print(l, r)

		ls = []
		for x in hand:
			a, b = GameBoard.getDomNum(x)
			if a == l or a == r:
				ls.append(x)
			elif b == l or b == r:
				ls.append(x)

		if len(ls) == 0: return False
		return ls