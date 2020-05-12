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
		print(statement)
		print()

		print(f'{self.player1.name}:')
		if p1:
			for minion in p1:
				print(minion.name, minion.attack_value, minion.health, minion.has_ds)
		else:
			print("Warband empty")	
		print()

		print(f'{self.player2.name}:')
		if p2:
			for minion in p2:
				print(minion.name, minion.attack_value, minion.health, minion.has_ds)
		else:
			print("Warband empty")	
		print()
		print()
		print()


class GameState:

	def __init__(self, player1, player2, warband1, warband2, attacking_player, 
		attacked_player, attacking_warband, attacked_warband, attack1=0, attack2=0, 
		attack_i=0, attacked_i=0):
		self.player1 = player1
		self.player2 = player2
		self.warband1 = warband1
		self.warband2 = warband2
		self.attacking_player = attacking_player
		self.attacked_player = attacked_player
		self.attacking_warband = attacking_warband
		self.attacked_warband = attacked_warband
		self.attack1 = attack1
		self.attack2 = attack2
		self.attack_i = attack_i
		self.attacked_i = attacked_i

	def next_turn(self):
		if self.attacking_player == self.player1:
			self.attacking_player = self.player2
			self.attacked_player = self.player1
			self.attacking_warband = self.warband2
			self.attacked_warband = self.warband1

			self.attack1 = self.attack_i
			self.attack2 = self.attacked_i

			self.attack_i = self.attack2
			self.attacked_i = self.attack1

		else:
			self.attacking_player = self.player1
			self.attacked_player = self.player2
			self.attacking_warband = self.warband1
			self.attacked_warband = self.warband2

			self.attack2 = self.attack_i
			self.attack1 = self.attacked_i

			self.attack_i = self.attack1
			self.attacked_i = self.attack2






















