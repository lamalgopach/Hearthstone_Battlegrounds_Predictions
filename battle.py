class Player:

	def __init__(self, name, warband, life=40):
		self.name = name
		self.warband = warband
		self.life = life



class Battle():
	#should I use other classes?
	def __init__(self, player1, player2, game_state=[]):
		self.player1 = player1
		self.player2 = player2
		self.game_state = game_state


	def start_of_combat():
		# check if any red whelp
		# check how many
		# randomly choose player
		# count dragons in warband
		# red whelp attack(no damage)
		pass

	def choose_first():
		# randomly choose first player
		pass

	def play():
		# first player attack
		# next player attack
		# 
		pass


	def player_die(self):
		# if self.player.life < 0:

		pass



