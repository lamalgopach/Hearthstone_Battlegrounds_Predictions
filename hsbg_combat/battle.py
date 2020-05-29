import random
from minions import *

class Warband:
	def __init__(self, player, warband=[]):
		self.player = player
		self.warband = warband

	def create_minion(self):
		# add the rest of classes 
		available_classes = [
			DragonspawnLieutenant, 
			GlyphGuardian, 
			InfestedWolf,
			KaboomBot, 
			RatPack,
			RedWhelp, 
			RighteousProtector, 
			RockpoolHunter, 
			SpawnOfnZoth, 
			SelflessHero,
			]
		return random.choice(available_classes)()

	# def create_warband(self):
	# random created warband
	# 	warband = []
	# 	while len(warband) != 7:
	# 		minion = self.create_minion()
	# 		warband.append(minion)
	# 		self.warband = warband

	def create_warband(self, warband_x):
		# Create given warband
		self.warband = warband_x

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

	def player_die(self):
		# if self.life < 0:
		pass


class BattleState:
	def __init__ (self, attacking_player, attacked_player, attacking_warband, 
		attacked_warband, attack_i=0, attacked_i=0, dead_attacking_minions=[],
		dead_attacked_minions=[]):
		self.attacking_player = attacking_player
		self.attacked_player = attacked_player
		self.attacking_warband = attacking_warband
		self.attacked_warband = attacked_warband
		self.attack_i = attack_i
		self.attacked_i = attacked_i
		self.dead_attacking_minions = dead_attacking_minions
		self.dead_attacked_minions = dead_attacked_minions


	def count_taunts(self):
		output = 0
		taunted_minions = []
		for minion in self.attacked_warband.warband:
			if minion.taunt == True:
				output += 1
				taunted_minions.append(minion)
		return output, taunted_minions

	def choose_attacked_minion(self):
		if self.count_taunts()[0] > 0:
			taunts = self.count_taunts()[1]
			r = random.randint(0, len(taunts) - 1)
			minion = taunts[r]
			for i in range(len(self.attacked_warband.warband)):
				if self.attacked_warband.warband[i].name == minion.name:
					attacked_minion = i
					break
		# otherwise attacked minion is chosen randomly:
		else:
			attacked_minion = random.randint(0, len(self.attacked_warband.warband) - 1)
		return attacked_minion	

	def play_next(self):
		print(self.attack_i)
		print(self.attacked_i)
		temp_player = self.attacking_player
		self.attacking_player = self.attacked_player
		self.attacked_player = temp_player

		temp_warband = self.attacking_warband
		self.attacking_warband = self.attacked_warband
		self.attacked_warband = temp_warband

		temp_i = self.attack_i
		self.attack_i = self.attacked_i
		self.attacked_i = temp_i

		temp_dead = self.dead_attacking_minions
		self.dead_attacking_minions = self.dead_attacked_minions
		self.dead_attacked_minions = temp_dead
		print(self.attack_i)
		print(self.attacked_i)

	def play(self):
		# first player attack
		# next player attack
		# 
		pass

	def print_state(self, statement):
		print(statement)
		print(f'{self.attacking_player.name}:')
		if self.attacking_warband.warband:
			for minion in self.attacking_warband.warband:
				print(minion.name, minion.attack_value, minion.health, minion.has_ds)
		else:
			print("Warband empty")	
		print()
		print(f'{self.attacked_player.name}:')
		if self.attacked_warband.warband:
			for minion in self.attacked_warband.warband:
				print(minion.name, minion.attack_value, minion.health, minion.has_ds)
		else:
			print("Warband empty")	
		print()
		print()

	def start_of_combat(self):
		# create list and dictionary of red whelp 
		# both in attacked and attacking warband
		red_whelp_list, red_whelp_dict = self.create_rw_list_and_dict(self.attacking_warband, self.attacked_warband)
		red_whelp_list2, red_whelp_dict2 = self.create_rw_list_and_dict(self.attacked_warband, self.attacking_warband)
		# merge those lists and dicts
		red_whelp_dict.update(red_whelp_dict2)
		red_whelp_list.extend(red_whelp_list2)
		# randomly choose attacking red whelp
		while red_whelp_list:
			random_rw = random.choice(red_whelp_list)
			friendly_warband = red_whelp_dict[random_rw][0]
			enemy_warband = red_whelp_dict[random_rw][1]
			# if Unstable Ghoul or Kaboombot dead:
			if enemy_warband == self.attacking_warband:
				dead_warband = self.dead_attacking_minions
			else:
				dead_warband = self.dead_attacked_minions
			if random_rw.attack_in_start_of_combat(friendly_warband, enemy_warband, dead_warband, self):
				self.solve_next_phase(True, 0, 0)
			red_whelp_list.remove(random_rw)

	def create_rw_list_and_dict(self, friendly_warband, enemy_warband):
		red_whelp_list = []
		red_whelp_dict = {}
		for minion in friendly_warband.warband:
			if isinstance(minion, RedWhelp):
				red_whelp_list.append(minion)
				red_whelp_dict[minion] = (friendly_warband, enemy_warband)
		return red_whelp_list, red_whelp_dict


	def one_minion_dies(self, minion, dead_minion, next_phase, friendly_minions, enemy_minions, j, dead_minions):

		minion.die(friendly_minions.warband, j, dead_minions)
		dead_minion += 1

		if dead_minion == 1 and minion.has_deathrattle:
			minion.deathrattle(self, friendly_minions, enemy_minions, j)			
			if isinstance(minion, KaboomBot) or isinstance(minion, UnstableGhoul):
				next_phase = True

		return dead_minion, next_phase


	def both_minions_die(self, minion1, minion2, dead_attacking_minion, dead_attacked_minion, next_phase, i):

		if minion1.health < 1:
			minion1.die(self.attacking_warband.warband, self.attack_i, self.dead_attacking_minions)
			dead_attacking_minion += 1

		if minion2.health < 1:
			minion2.die(self.attacked_warband.warband, i, self.dead_attacking_minions)
			dead_attacked_minion += 1

		if dead_attacking_minion == 1 and minion1.has_deathrattle:
			minion1.deathrattle(self, self.attacking_warband, self.attacked_warband, self.attack_i)
			if isinstance(minion1, KaboomBot) or isinstance(minion1, UnstableGhoul):
				next_phase = True

		if dead_attacked_minion == 1 and minion2.has_deathrattle:
			minion2.deathrattle(self, self.attacked_warband, self.attacking_warband, i)
			if isinstance(minion2, KaboomBot) or isinstance(minion2, UnstableGhoul):
				next_phase = True
		return dead_attacking_minion, dead_attacked_minion, next_phase

	def solve_next_phase(self, next_phase, dead_attacking_minion, dead_attacked_minion):

		while next_phase:
			# slighten
			dthr1 = False
			dthr2 = False
			minion1t = None
			minion2t = None
			j1 = 0
			j2 = 0
			next_phase = False

			for minion in self.attacking_warband.warband:
				if minion.health < 1:
					j1 = self.attacking_warband.warband.index(minion)
					minion.die(self.attacking_warband.warband, j1, self.dead_attacking_minions)
					next_phase = True
					if minion.has_deathrattle:
						dthr1 = True
						minion1t = minion
					if j1 < self.attack_i:
						dead_attacking_minion += 1
					break

			for minion in self.attacked_warband.warband:
				if minion.health < 1:
					j2 = self.attacked_warband.warband.index(minion)
					minion.die(self.attacked_warband.warband, j2, self.dead_attacked_minions)
					next_phase = True
					if minion.has_deathrattle:
						dthr2 = True
						minion2t = minion

					if j2 < self.attacked_i:
						dead_attacked_minion += 1
					break

			if dthr1:
				minion1t.deathrattle(self, self.attacking_warband, self.attacked_warband, j1)
				next_phase = True

			if dthr2:
				minion2t.deathrattle(self, self.attacked_warband, self.attacking_warband, j2)
				next_phase = True

		return dead_attacking_minion, dead_attacked_minion