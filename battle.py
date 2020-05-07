class Player:

	def __init__(self, name, warband, life=40):
		self.name = name
		self.warband = warband
		self.life = life


	# at the end of the battle count damage:
	def count_final_damage(self, warband):
		damage = 0

		for minion in warband:
			damage += minion.tier

		return damage


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

	def print_state(self):
		print(self.player1.name)
		for minion in self.player1.warband:
			print(minion.name, minion.attack_value, minion.health, minion.has_ds)
		print()
		print(self.player2.name)
		for minion in self.player2.warband:
			print(minion.name, minion.attack_value, minion.health, minion.has_ds)


