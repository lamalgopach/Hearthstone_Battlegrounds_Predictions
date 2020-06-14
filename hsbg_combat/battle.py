import random
from minions import UnstableGhoul
from dragons import RedWhelp
from mechs import KaboomBot


def attack_in_start_of_combat(battle, redwhelp, status):
	friendly_minions = battle.attacking_player.warband if status == 1 else battle.attacked_player.warband
	enemy_minions = battle.attacked_player.warband if status == 1 else battle.attacking_player.warband
	damage = redwhelp.add_damage_in_combat(friendly_minions=friendly_minions)
	attacked_minion = random.choice(enemy_minions)

	j = enemy_minions.index(attacked_minion)

	attacked_minion.take_damage(damage, redwhelp.poisonous)


	if attacked_minion.health < 1:

		status = 2 if status == 1 else 1
		attacked_minion.die(battle=battle, status=status, j=j)

		if attacked_minion.has_deathrattle:
			attacked_minion.deathrattle(battle=battle, status=status)
			if isinstance(attacked_minion, KaboomBot):
				return True
			elif isinstance(attacked_minion, UnstableGhoul):
				return True
		elif isinstance(attacked_minion, RedWhelp):
			return attacked_minion


class Player:
	def __init__(self, name, start_warband, warband, attack_index=0, attacked_minion=0,
				dead_minions=[], dead_minions_dict={}, level=1, life=40):
		self.name = name
		self.start_warband = start_warband 
		self.warband = warband
		self.attack_index = attack_index
		self.attacked_minion = attacked_minion
		self.dead_minions = dead_minions
		self.dead_minions_dict = dead_minions_dict
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
			print(redwhelp_list)
			random_redwhelp = random.choice(redwhelp_list)
			status = redwhelp_dict[random_redwhelp]
			output = attack_in_start_of_combat(self, random_redwhelp, status)
			if isinstance(output, RedWhelp) and output in redwhelp_list:
				redwhelp_list.remove(output)
			elif output == True:
				self.solve_next_phase(True, 0, 0)

			redwhelp_list.remove(random_redwhelp)

	def solve_next_phase(self, next_phase, dead_attacking_minions, dead_attacked_minions):
		while next_phase:
			# slighten
			dthr1 = False
			dthr2 = False
			minion1t = None
			minion2t = None
			j1 = 0
			j2 = 0
			next_phase = False

			for minion in self.attacking_player.warband:
				status = 1
				if minion.health < 1:
					j1 = self.attacking_player.warband.index(minion)
					minion.die(self, status=status, j=j1)
					next_phase = True
					if minion.has_deathrattle:
						dthr1 = True
						minion1t = minion
					if j1 < self.attacking_player.attack_index:
						dead_attacking_minions += 1
					break

			for minion in self.attacked_player.warband:
				status = 2
				if minion.health < 1:
					j2 = self.attacked_player.warband.index(minion)
		
					minion.die(self, status=status, j=j2)
					next_phase = True
					if minion.has_deathrattle:
						dthr2 = True
						minion2t = minion
					if j2 < self.attacked_player.attack_index:
						dead_attacked_minions += 1
					break

			if dthr1:
				status = 1
				minion1t.deathrattle(self, status=status)
				next_phase = True

			if dthr2:
				status = 2
				minion2t.deathrattle(self, status=status)
				next_phase = True

		return dead_attacking_minions, dead_attacked_minions

	def count_taunts(self):
		output = 0
		taunted_minions = []
		for minion in self.attacked_player.warband:
			if minion.taunt == True:
				output += 1
				taunted_minions.append(minion)
		return output, taunted_minions

	def choose_attacked_minion(self):
		if self.count_taunts()[0] > 0:
			taunts = self.count_taunts()[1]
			random_minion = random.choice(taunts)
			attacked_minion = [i for i in range(len(self.attacked_player.warband)) if self.attacked_player.warband[i] == random_minion][0]
		# otherwise attacked minion is chosen randomly:
		else:
			attacked_minion = random.randint(0, len(self.attacked_player.warband) - 1)
		return attacked_minion	

	def both_minions_die(self, next_phase):
		minion1 = self.attacking_player.warband[self.attacking_player.attack_index]
		minion2 = self.attacked_player.warband[self.attacked_player.attacked_minion]

		if minion1.health < 1:
			status = 1
			j = self.attacking_player.attack_index 
			minion1.die(self, status=status, j=j)
		if minion2.health < 1:
			j = self.attacked_player.attacked_minion
			status = 2
			minion2.die(self, status=status, j=j)

		if minion1.has_deathrattle:
			status = 1
			minion1.deathrattle(self, status=status)
			if isinstance(minion1, KaboomBot) or isinstance(minion1, UnstableGhoul):
				next_phase = True

		if minion2.has_deathrattle:
			status = 2
			minion2.deathrattle(self, status=status)
			if isinstance(minion2, KaboomBot) or isinstance(minion2, UnstableGhoul):
				next_phase = True

		return next_phase

	def one_minion_dies(self, minion, status, next_phase):

		j = self.attacking_player.attack_index if status == 1 else self.attacked_player.attacked_minion

		minion.die(self, status=status, j=j)
		
		if minion.has_deathrattle:
			minion.deathrattle(self, status=status)			
			if isinstance(minion, KaboomBot) or isinstance(minion, UnstableGhoul):
				next_phase = True

		return next_phase