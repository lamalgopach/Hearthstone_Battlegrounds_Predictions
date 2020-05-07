import copy
import random

class Player:

	def __init__(self, name, warband, tier=1, life=40):
		self.name = name
		self.warband = warband
		self.tier = tier
		self.life = life

	# at the end of the battle count damage:
	def count_final_damage(self, alive_minions):
		damage = self.tier
		for minion in alive_minions:
			damage += minion.tier
		return damage


class Battle():

	def __init__(self, player1, player2):
		self.player1 = player1
		self.player2 = player2


	def start_of_combat():
		# check if any red whelp
		# check how many
		# randomly choose player
		# count dragons in warband
		# red whelp attack(no damage)
		pass

	def choose_first(self):

		order = True

		# p1 = self.player1.warband
		# p2 = self.player2.warband

		# self.player1.warband = copy.deepcopy(p1)
		# self.player2.warband = copy.deepcopy(p2)

		p1 = copy.deepcopy(self.player1.warband)
		p2 = copy.deepcopy(self.player2.warband)		

		if len(self.player1.warband) < len(self.player2.warband):
			order = False
		elif len(self.player1.warband) == len(self.player2.warband):
			order = random.choice([True, False])

		if order == True:
			game = [p1, p2]
		else:
			game = [p2, p1]

		return p1, p2, game

	def play():
		# first player attack
		# next player attack
		# 
		pass


	def player_die(self):
		# if self.player.life < 0:

		pass

	def print_state(self, statement, p1, p2):
		print()
		print()
		print(statement)
		print()

		for minion in p1:
			print(minion.name, minion.attack_value, minion.health, minion.has_ds)
		print()

		for minion in p2:
			print(minion.name, minion.attack_value, minion.health, minion.has_ds)
		print()


