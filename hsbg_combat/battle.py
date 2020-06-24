import random
from dragons import RedWhelp


def attack_in_start_of_combat(battle, redwhelp, status):
	friendly_minions = battle.attacking_player.warband if status == 1 else battle.attacked_player.warband
	enemy_minions = battle.attacked_player.warband if status == 1 else battle.attacking_player.warband
	damage = redwhelp.add_damage_in_combat(friendly_minions=friendly_minions)
	attacked_minion = random.choice(enemy_minions)
	j = enemy_minions.index(attacked_minion)
	attacked_minion.take_damage(damage, redwhelp.poisonous)

	if attacked_minion.health < 1:
		battle.execute_death_phase(0, 0)
		if isinstance(attacked_minion, RedWhelp):
			return attacked_minion


class Player:
	def __init__(self, name, start_warband, warband, effects_dict={},
				attack_index=0, 
				attacked_minion=0, dead_minions=[], dead_minions_dict={}, 
				this_turn_dead=[], effects_after_friendly_deaths = {},
				deathrattles=[], effects_causing_next_death=[], 
				level=1, life=40):

		self.name = name
		self.start_warband = start_warband 
		self.warband = warband
		self.effects_dict = effects_dict
		self.attack_index = attack_index
		self.attacked_minion = attacked_minion
		self.dead_minions = dead_minions
		self.dead_minions_dict = dead_minions_dict
		self.this_turn_dead = this_turn_dead
		self.effects_after_friendly_deaths = effects_after_friendly_deaths
		self.deathrattles = deathrattles
		self.effects_causing_next_death = effects_causing_next_death
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
	def __init__(self, players, round):
		self.players = players
		self.round = 0

	@property
	def attacking_player(self):
		return self.players[self.round % len(self.players)]

	@property
	def attacked_player(self):
		return self.players[(self.round + 1) % len(self.players)]


	def print_state(self, statement):
		print(statement)
		print(f'{self.players[0].name}:')
		if self.players[0].warband:
			for minion in self.players[0].warband:
				print(minion.name, minion.attack_value, minion.health, minion.has_ds)
		else:
			print("Warband empty")	
		print()
		print(f'{self.players[1].name}:')
		if self.players[1].warband:
			for minion in self.players[1].warband:
				print(minion.name, minion.attack_value, minion.health, minion.has_ds)
		else:
			print("Warband empty")	
		print()
		print()

	def create_rw_list_and_dict(self, status):
		friendly_minions = self.attacking_player.warband if status == 1 else self.attacked_player.warband
		redwhelp_list = []
		redwhelp_dict = {}
		for minion in friendly_minions:
			if isinstance(minion, RedWhelp):
				redwhelp_list.append(minion)
				redwhelp_dict[minion] = status
		return redwhelp_list, redwhelp_dict

	def start_of_combat(self):
		# create list and dictionary of red whelp 
		# both in attacked and attacking warband
		redwhelp_list, redwhelp_dict = self.create_rw_list_and_dict(status=1)
		redwhelp_list2, redwhelp_dict2 = self.create_rw_list_and_dict(status=2)
		# merge those lists and dicts
		redwhelp_dict.update(redwhelp_dict2)
		redwhelp_list.extend(redwhelp_list2)
		# randomly choose attacking red whelp
		while redwhelp_list:
			random_redwhelp = random.choice(redwhelp_list)
			status = redwhelp_dict[random_redwhelp]
			killed_before_attack = attack_in_start_of_combat(self, random_redwhelp, status)
			if killed_before_attack in redwhelp_list:
				redwhelp_list.remove(killed_before_attack)
			redwhelp_list.remove(random_redwhelp)

	def count_taunts(self):
		taunted_minions_number = 0
		taunted_minions = []
		for minion in self.attacked_player.warband:
			if minion.taunt == True:
				taunted_minions_number += 1
				taunted_minions.append(minion)
		return taunted_minions_number, taunted_minions

	def choose_attacked_minion(self):
		if self.count_taunts()[0] > 0:
			taunts = self.count_taunts()[1]
			random_minion = random.choice(taunts)
			attacked_minion = [i for i in range(len(self.attacked_player.warband)) if self.attacked_player.warband[i] == random_minion][0]
		# otherwise attacked minion is chosen randomly:
		else:
			attacked_minion = random.randint(0, len(self.attacked_player.warband) - 1)
		return attacked_minion	

	def execute_deaths(self, d_ag_ms, d_ad_ms):

		if self.attacking_player.this_turn_dead:
			for minion in self.attacking_player.this_turn_dead:
				j = self.attacking_player.warband.index(minion)
				if j <= self.attacking_player.attack_index:
					d_ag_ms += 1
				if minion.has_deathrattle:
					self.attacking_player.deathrattles.append(minion)
				minion.die(self, status=1, j=j)

			self.attacking_player.this_turn_dead = []

		if self.attacked_player.this_turn_dead:
			for minion in self.attacked_player.this_turn_dead:
				j = self.attacked_player.warband.index(minion)
				if j <= self.attacked_player.attack_index:
					d_ad_ms += 1 
				if minion.has_deathrattle:
					self.attacked_player.deathrattles.append(minion)
				minion.die(self, status=2, j=j)

			self.attacked_player.this_turn_dead = []

		return d_ag_ms, d_ad_ms

	def execute_deathrattles(self):
		
		for minion in self.attacking_player.deathrattles:
			minion.deathrattle(self, status=1)
		self.attacking_player.deathrattles = []

		for minion in self.attacked_player.deathrattles:
			minion.deathrattle(self, status=2)
		self.attacked_player.deathrattles = []

	def execute_death_phase(self, dead_attacking_minions, dead_attacked_minions):
		while True:
			# self.print_state("while True")
			self.attacking_player.effects_causing_next_death = []
			self.attacked_player.effects_causing_next_death = []

			players = [self.attacking_player, self.attacked_player]

			
			for player in players:
				for minion in player.warband:
					if minion.health < 1:
						player.this_turn_dead.append(minion)

			if self.attacking_player.this_turn_dead or self.attacked_player.this_turn_dead:
				dead_attacking_minions, dead_attacked_minions = self.execute_deaths(d_ag_ms=dead_attacking_minions, d_ad_ms=dead_attacked_minions)		


			if self.attacking_player.deathrattles or self.attacked_player.deathrattles:
				self.execute_deathrattles()

			if not (self.attacking_player.effects_causing_next_death or self.attacked_player.effects_causing_next_death):
				break 
			elif not self.attacking_player.warband or not self.attacked_player.warband:
				break

		return dead_attacking_minions, dead_attacked_minions

	# def check_dead_minions(self):

	# 	if self.attacking_player.gain_from_death:
	# 		for dead_minion in self.attacking_player.this_turn_dead:










