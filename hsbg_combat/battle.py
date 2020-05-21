import random
from .minions import DragonspawnLieutenant, GlyphGuardian, InfestedWolf 
# from minions import KaboomBot, MurlocWarleader
from .minions import RedWhelp, RighteousProtector, RockpoolHunter
from .minions import SpawnOfnZoth, SelflessHero


class Warband:
	def __init__(self, player, warband=[]):
		self.player = player
		self.warband = warband

	def create_minion(self):
		available_classes = [DragonspawnLieutenant, GlyphGuardian, InfestedWolf,
					RedWhelp, RighteousProtector, RockpoolHunter, 
					SpawnOfnZoth, SelflessHero]
		return random.choice(available_classes)()

	# def create_warband(self):
	# 	warband = []
	# 	while len(warband) != 7:
	# 		minion = self.create_minion()
	# 		warband.append(minion)
	# 		self.warband = warband

	def create_warband(self, warband_x):
		self.warband = warband_x
		# if self.player == "Alice":
		# 	self.warband = [RockpoolHunter(), InfestedWolf(), RedWhelp(), 
		# 					GlyphGuardian(), SpawnOfnZoth(), RighteousProtector(), 
		# 					SelflessHero()]

		# else:
		# 	self.warband = [RockpoolHunter(), DragonspawnLieutenant(), SelflessHero(), 
		# 					GlyphGuardian(), RedWhelp(), SpawnOfnZoth(), 
		# 					InfestedWolf()]


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
	def __init__ (self, attacking_player, attacked_player, attacking_warband, attacked_warband, attack_i=0, attacked_i=0):
		self.attacking_player = attacking_player
		self.attacked_player = attacked_player
		self.attacking_warband = attacking_warband
		self.attacked_warband = attacked_warband
		self.attack_i = attack_i
		self.attacked_i = attacked_i


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
		temp_player = self.attacking_player
		self.attacking_player = self.attacked_player
		self.attacked_player = temp_player

		temp_warband = self.attacking_warband
		self.attacking_warband = self.attacked_warband
		self.attacked_warband = temp_warband

		temp_i = self.attack_i
		self.attack_i = self.attacked_i
		self.attacked_i = temp_i

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
		red_whelp_list, red_whelp_dict = self.create_rw_list_and_dict(self.attacking_warband, self.attacked_warband)
		red_whelp_list2, red_whelp_dict2 = self.create_rw_list_and_dict(self.attacked_warband, self.attacking_warband)
		red_whelp_dict.update(red_whelp_dict2)
		red_whelp_list.extend(red_whelp_list2)
		# randomly choose attacking red whelp
		while red_whelp_list:
			random_rw = random.choice(red_whelp_list)
			friendly_warband = red_whelp_dict[random_rw][0]
			enemy_warband = red_whelp_dict[random_rw][1]
			random_rw.attack_in_start_of_combat(friendly_warband, enemy_warband)
			red_whelp_list.remove(random_rw)

	def create_rw_list_and_dict(self, friendly_warband, enemy_warband):
		red_whelp_list = []
		red_whelp_dict = {}
		for minion in friendly_warband.warband:
			if isinstance(minion, RedWhelp):
				red_whelp_list.append(minion)
				red_whelp_dict[minion] = (friendly_warband, enemy_warband)
		return red_whelp_list, red_whelp_dict

# May 14th: 159 lines of code