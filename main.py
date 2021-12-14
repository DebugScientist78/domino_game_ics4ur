import GameBoard
import GameEngine
import Player

if __name__ == "__main__":
	game_board = GameBoard.GameBoard()
	#print(game_board.pile.arrange_dominos_doubles_first_in_2d_list(0,12))
	print(game_board.grabStartHand())
