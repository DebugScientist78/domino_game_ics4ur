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

	#@staticmethod
	#def determineTurnOrder():
