import GameBoard

class GameEngine:
	player_list = []
	turn_order = []
	turn_num = 0
	num_players = 0
	num_games = 0
	
	@staticmethod
	def retriveInput(msg='', is_int=False, error_msg=''):
		if is_int:
			while True:
				try:
					data = int(input(msg))
					return data
				except:
					print(error_msg)
		while True:
			try:
				data = input(msg)
				return data
			except:
				print(error_msg)

	@staticmethod
	def verifyGamesCount(num):
		if num % 2 == 0: return False
		return True

	@staticmethod
	def determineTurnOrder():
		'''
		critera: 
		if player has 12|12, add to turn order
		if player has highest double, add to turn order
		Lastly if no double was there, pick 4th domino get the sum of each number then the highest to lowest of sum order becomes the turn order
		'''
		double_c = 12
		for x in range(GameEngine.num_players):
			expr = GameBoard.GameBoard.getDomExpr(double_c, double_c)
			if GameEngine.player_list[x].doesHandHave(expr):
				GameEngine.turn_order.append(GameEngine.player_list[x])
				break
		double_c -= 1
