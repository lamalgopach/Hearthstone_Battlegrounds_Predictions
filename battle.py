import copy
import random

class Player:

	def __init__(self, name, warband, level=1, life=40):
		self.name = name
		self.warband = warband
		self.level = level
		self.life = life

	# at the end of the battle count damage:
	def count_final_damage(self, alive_minions):
		damage = self.level
		for minion in alive_minions:
			damage += minion.tier
		return damage

	def summon_minion(self, class_type):
		minion = class_type
		return minion


class Battle:

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

		print(self.player1.name)
		for minion in p1:
			print(minion.name, minion.attack_value, minion.health, minion.has_ds)
		print()

		print(self.player2.name)
		for minion in p2:
			print(minion.name, minion.attack_value, minion.health, minion.has_ds)
		print()


class GameState:

	def __init__(self, player1, player2, attacking, attacked, attacking_warband, 
				attacked_warband):
		self.player1 = player1
		self.player2 = player2
		self.attacking = attacking
		self.attacked = attacked
		self.attacking_warband = attacking_warband
		self.attacked_warband = attacked_warband

	def next_turn(self):
		if self.attacking == self.player1:
			self.attacking = self.player2
			self.attacked = self.player1
		else:
			self.attacking = self.player1
			self.attacked = self.player2






















