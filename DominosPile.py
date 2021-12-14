class DominosPile:
	counter = 0
	first_dice = 12
	ls_2d = []
	dom_dict = {}
	def arrange_dominos_double_first(self):
		self.counter = 0
		for i in range(self.first_dice,-1,-1):
			second_dice = first_dice - counter
			for j in range(self.counter+1):
				print(str(second_dice) + '|' + str(i))
				second_dice += 1
			self.counter += 1
			print(" ")

	def arrange_dominos_double_last(self):
		self.counter = 0
		for i in range(self.first_dice,-1,-1):
			second_dice = i + self.counter
			for j in range(self.counter+1):
				print(str(second_dice) + '|' + str(i))
				second_dice -= 1
			self.counter += 1
			print(" ")

	def arrange_dominos_doubles_first_in_2d_list(self, counter,first_dice):
	    self.counter = 0
	    self.first_dice = 12
	    ls = []
	    for i in range(self.first_dice,-1,-1):
	        temp = []
	        second_dice = self.first_dice - self.counter
	        for j in range(self.counter+1):
	            temp.append(str(second_dice) + '|' + str(i))
	            second_dice += 1
	        self.counter += 1
	        ls.append(temp)
	    self.ls_2d = ls
	    return ls

	def find_domino(self, num):
		cn = 0
		val = ''
		for x in self.ls_2d:
			for y in x:
				val = y
				cn += 1
				if cn == num: return val

	def get_domino_91_dict(self, ls_2d):
		cn = 1
		val = ''
		dictc = {}
		for x in ls_2d:
			for y in x:
				dictc[y] = cn
				cn += 1
		self.dom_dict = dictc
		return dictc

	def visited(self, dom):
		self.dom_dict[dom] = "v"

	def get_dict(self):
		return self.dom_dict

	def __init__(self):
		ls = self.arrange_dominos_doubles_first_in_2d_list(self.counter, self.first_dice)
		self.get_domino_91_dict(ls)