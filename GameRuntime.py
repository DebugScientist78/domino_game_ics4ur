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
				GameRuntime.simulateGame()
			if val == 3: return

	@staticmethod
	def gameSetup():
		#print(game_board.pile.arrange_dominos_doubles_first_in_2d_list(0,12)) 
		GameEngine.GameEngine.num_players = GameEngine.GameEngine.retriveInput("How many players?: ", True, "Please Enter an int")
		
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


	@staticmethod
	def simulateGame():
		GameEngine.GameEngine.turn_order += 1
		'''
		check if player has a win condition
		1) if a player's hand is empty
		2) if the pile is empty, or no player can play a domino from their hand or (if) existing pile
			the player with the lowest domino sum wins
		'''

		for x in GameEngine.GameEngine.turn_order:
			if x.isEmpty():
				return x
