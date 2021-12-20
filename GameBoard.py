import DominosPile
import random
import GameEngine

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
	def grabDom():
		''' 
		Grabs 1 domino from the pile and return them
		'''
		expr = GameBoard.getRanDomExpr()
		while True:
			#prevent dupes
			if GameBoard.pile.dom_dict[expr] == "v":
				expr = GameBoard.getRanDomExpr()
			else:
				break
		GameBoard.pile.dom_dict[expr] = "v"
		return expr

	@staticmethod
	def grabStartHand():
		''' 
		Grab 7 dominos from the pile and return them as a list
		'''
		ls = []
		for x in range(7):
			expr = GameBoard.grabDom()
			ls.append(expr)
		return ls

	@staticmethod
	def getRemainPile():
		ls = []
		for key in GameBoard.pile.dom_dict:
			if GameBoard.pile.dom_dict[key] != 'v':
				ls.append(key)
		if len(ls) == 0: return False
		return ls

	@staticmethod
	def validDominos(hand):
		'''
		given an string array of dominos, check to see if any of them are valid to play
		return False if none, return a list of valid options
		'''
		l = GameBoard.getDomNum(GameBoard.board.getL())[0]
		r = GameBoard.getDomNum(GameBoard.board.getR())[1]
		#print(l, r)

		ls = []
		for x in hand:
			a, b = GameBoard.getDomNum(x)
			if a == l or a == r:
				ls.append(x)
			elif b == l or b == r:
				ls.append(x)

		if len(ls) == 0: return False
		return ls

	@staticmethod
	def putDomino(dom):
		'''
		Determine which side is valid, after a side is chosen, determine if a flip is needed
		'''
		l = GameBoard.getDomNum(GameBoard.board.getL())[0]
		r = GameBoard.getDomNum(GameBoard.board.getR())[1]
		a,b = GameBoard.getDomNum(dom)
		while True:
			val = GameEngine.GameEngine.retriveInput("Pick:\n1) Left\n2) Right\n", True, '')
			if val == 1:
				if l == a or l == b:
					if a == l: GameBoard.board.appendL(GameBoard.getDomExpr(b,a))
					else: GameBoard.board.appendL(dom)
					break
				else: print("You can't play this domino on the left side")
			elif val == 2:
				if r == a or r == b:
					if b == r: GameBoard.board.appendR(GameBoard.getDomExpr(b,a))
					else: GameBoard.board.appendR(dom)
					break
				else: print("You can't play this domino on the right side")
			else:
				print("Please enter 1 or 2")

	@staticmethod
	def displayBoard():
		print("The Board: " + GameBoard.board.deq.__str__())