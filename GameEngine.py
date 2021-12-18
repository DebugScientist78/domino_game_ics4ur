import GameBoard

class GameEngine:
	player_list = []
	turn_order = []
	turn_num = 0
	num_players = 0
	num_games = 0
	turn_index = 0
	
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
		if player has 12|12, add to turn order first
		if player has highest double, add to turn order
		Lastly if no double was there, pick 4th domino get the sum of each number then the highest to lowest of sum order becomes the turn order
		'''
		player_in_list = [False] * GameEngine.num_players
		#print(player_in_list)
		for x in range(12, -1, -1):
			for plr in range(GameEngine.num_players):
				expr = GameBoard.GameBoard.getDomExpr(x, x)
				if GameEngine.player_list[plr].doesHandHave(expr) and player_in_list[plr] == False:
					GameEngine.turn_order.append(GameEngine.player_list[plr])
					player_in_list[plr] = True

		#print(GameEngine.turn_order)
		remaining_players = []
		for x in range(GameEngine.num_players):
			if player_in_list[x] == False:
				a, b = GameBoard.GameBoard.getDomNum(GameEngine.player_list[x].hand[3])
				pair = (int(a+b), GameEngine.player_list[x])
				remaining_players.append(pair)
		remaining_players.sort(reverse=True)
		#print(remaining_players)
		for x in remaining_players:
			GameEngine.turn_order.append(x[1])

		print("The Turn order is: ", end='')
		for x in range(len(GameEngine.turn_order)):
			if x == len(GameEngine.turn_order)-1: print(GameEngine.turn_order[x].name, end='')
			else: print(GameEngine.turn_order[x].name, end=' -> ')
		print("")
	