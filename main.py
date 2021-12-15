import GameBoard
import GameEngine
import Player

if __name__ == "__main__":
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
