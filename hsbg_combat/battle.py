import random
from dragons import RedWhelp
import copy

def attack_in_start_of_combat(battle, redwhelp, status):
	friendly_minions = battle.attacking_player.warband if status == 1 else battle.attacked_player.warband
	enemy_minions = battle.attacked_player.warband if status == 1 else battle.attacking_player.warband
	damage = redwhelp.add_damage_in_combat(friendly_minions=friendly_minions)
	attacked_minion = random.choice(enemy_minions)
	j = enemy_minions.index(attacked_minion)
	st = 2 if status == 1 else 1
	attacked_minion.take_damage(damage, False, battle, st)

	if attacked_minion.health < 1:
		battle.execute_death_phase(0, 0)
		if isinstance(attacked_minion, RedWhelp):
			return attacked_minion

class Player:
	def __init__(self, name, start_warband, warband,
				attack_index=0, attacked_minion=0,

				dead_minions=[], dead_minions_dict={}, 
				this_turn_dead=[], deathrattles=[], 

				effects_after_friend_is_summoned = {},
				effects_after_friend_is_dead = {},
				effects_after_friend_lost_ds = {},
				
				effects_causing_next_death=[], 

				level=1, life=40):

		self.name = name
		self.start_warband = start_warband 
		self.warband = warband

		self.attack_index = attack_index
		self.attacked_minion = attacked_minion

		self.dead_minions = dead_minions
		self.dead_minions_dict = dead_minions_dict
		self.this_turn_dead = this_turn_dead
		self.deathrattles = deathrattles

		self.effects_after_friend_is_summoned = effects_after_friend_is_summoned
		self.effects_after_friend_is_dead = effects_after_friend_is_dead
		self.effects_after_friend_lost_ds = effects_after_friend_lost_ds

		self.effects_causing_next_death = effects_causing_next_death

		self.level = level
		self.life = life

	def find_minions_with_superpowers(self, warband):
		for minion in warband:
			if minion.has_effect:
				self.add_to_effect_dict(minion, minion.has_effect)

	def add_to_effect_dict(self, minion, minions_effect):
		if minions_effect == "friend_summoned":
			self.effects_after_friend_is_summoned[minion] = minion.effect
		elif minions_effect == "friend_death":
			self.effects_after_friend_is_dead[minion] = minion.effect
		elif minions_effect == "friend_ds_lost":
			self.effects_after_friend_lost_ds[minion] = minion.effect

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

	def execute_deaths(self, player, deaths_number, status):
		if player.this_turn_dead:
			for minion in player.this_turn_dead:
				j = player.warband.index(minion)
				if j <= player.attack_index:
					deaths_number += 1
				if minion.has_deathrattle:
					player.deathrattles.append(minion)
				minion.die(self, status, j=j)
			player.this_turn_dead = []
		return deaths_number

	def execute_deathrattles(self, player, status):

		for minion in player.deathrattles:
			minion.deathrattle(self, status)
		player.deathrattles = []

	def execute_death_phase(self, dead_attacking_minions, dead_attacked_minions):
		while True:

			self.attacking_player.effects_causing_next_death = []
			self.attacked_player.effects_causing_next_death = []

			players = [self.attacking_player, self.attacked_player]
			status_dict = {self.attacking_player:1, self.attacked_player:2}
			deaths_number_dict = {self.attacking_player:dead_attacking_minions, self.attacked_player:dead_attacked_minions}
			# print()
			# print("number of deaths BEFORE:")
			# for k, v in deaths_number_dict.items():
			# 	print(k, v)

			for player in players:
				for minion in player.warband:
					if minion.health < 1:
						player.this_turn_dead.append(minion)
						player.dead_minions_dict[minion] = player.warband.index(minion)
						player.dead_minions.append(minion)

			for player in players:
				if player.this_turn_dead:
					deaths_number_dict[player] = self.execute_deaths(player=player, deaths_number=deaths_number_dict[player], status=status_dict[player])
			
			# print("number of deaths AFTER:")
			# for k, v in deaths_number_dict.items():
			# 	print(k, v)

			for player in players:
				if player.deathrattles:
					self.execute_deathrattles(player=player, status=status_dict[player])

			if not (self.attacking_player.effects_causing_next_death or self.attacked_player.effects_causing_next_death):
				break 
			# elif not self.attacking_player.warband or not self.attacked_player.warband:
			# 	print("two")
			# 	break
		dead_attacking_minions = deaths_number_dict[self.attacking_player]
		dead_attacked_minions = deaths_number_dict[self.attacked_player]
		print(dead_attacking_minions, dead_attacked_minions)
		return dead_attacking_minions, dead_attacked_minions
