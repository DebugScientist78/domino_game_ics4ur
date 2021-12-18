import GameBoard
import GameEngine
import Player

class GameRuntime:

	@staticmethod
	def startMenu():
		print("Welcome to Dominos!\nWould you like to?")
		while True:
			val = GameEngine.GameEngine.retriveInput("1) Play\n2) Read the Rules\n3) Exit Program \n", True, "Please Enter an from 1-3")
			if val == 1:
				GameRuntime.gameSetup()
				GameBoard.GameBoard.board.appendL('12|5')
				GameBoard.GameBoard.board.appendL('7|12')
				print(GameBoard.GameBoard.validDominos(GameEngine.GameEngine.turn_order[0].hand))
				#GameRuntime.simulateGame()
			if val == 3: return

	@staticmethod
	def gameSetup():
		while True:
			GameEngine.GameEngine.num_players = GameEngine.GameEngine.retriveInput("How many players?: ", True, "Please Enter an int")
			if GameEngine.GameEngine.num_players <= 4:
				break
			else:
				print("Maximum Lobby Size is 4 Players!")

		for x in range(GameEngine.GameEngine.num_players):
			temp =  Player.Player()
			temp.name = GameEngine.GameEngine.retriveInput("Enter your name: ", False, "")
			temp.hand = GameBoard.GameBoard.grabStartHand()
			GameEngine.GameEngine.player_list.append(temp)
		print(GameEngine.GameEngine.player_list)

		while True:
			GameEngine.GameEngine.num_games = GameEngine.GameEngine.retriveInput("How many rounds?: ", True, "Please enter an odd int")
			if GameEngine.GameEngine.verifyGamesCount(GameEngine.GameEngine.num_games):
				break
			else:
				print("Please enter an odd integer")

		#print(GameBoard.GameBoard.grabStartHand())
		#print(GameBoard.GameBoard.pile.dom_dict)
		print(GameEngine.GameEngine.num_games)
		GameEngine.GameEngine.determineTurnOrder()

	@staticmethod
	def playTurn(player):
		'''
		User should be able to only see valid dominos to play and the option to draw a domino from the pile
		'''
		ls = GameBoard.GameBoard.validDominos(player.hand)
		if ls == False: return

		num = 0
		print("0) draw a domino from pile")
		for op in ls:
			print(str(num) + ") Play: "  + op)
			num += 1

		while True:
			val = GameEngine.GameEngine.retriveInput('', True, 'Please enter an integer only')
			if val == 0:
				#pull from pile
			elif val >= 1 and val < len(ls):
				#play a domino

	@staticmethod
	def simulateGame():
		GameEngine.GameEngine.turn_num += 1
		'''
		check if player has a win condition
		1) if a player's hand is empty
		2) if the pile is empty, or no player can play a domino from their hand or (if) existing pile
			the player with the lowest domino sum wins
		'''
		if len(GameBoard.GameBoard.board) >= 13:
			for player in GameEngine.GameEngine.turn_order:
				if player.isEmpty():
					return player
			if len(GameBoard.GameBoard.getRemainPile()) == 0:
				flag = True
				for player in GameEngine.GameEngine.turn_order:
					if GameBoard.GameBoard.validDominos(player.hand) != False:
						flag = False
						break
				if flag:
					ls = []
					for player in GameEngine.GameEngine.turn_order:
						s = 0
						for dom in player.hand:
							a,b = GameBoard.GameBoard.getDomNum(dom)
							s += (a+b)
						pair = (s, player)
						ls.append(pair)
					ls.sort()
					return ls[0][1]
		else:
			GameRuntime.playTurn(GameEngine.GameEngine.turn_order[GameEngine.GameEngine.turn_index])
		GameEngine.GameEngine.turn_index += 1
		if GameEngine.GameEngine.turn_index == len(GameEngine.GameEngine.turn_order):
			GameEngine.GameEngine.turn_index = 0
