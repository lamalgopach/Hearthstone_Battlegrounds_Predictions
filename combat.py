import random
from random import choice
import copy
from minions import Player, minions_lst, Card, SelflessHero, SpawnOfnZoth, InfestedWolf
from minions import GlyphGuardian, RedWhelp

alices_warband = [] 
bobs_warband = []

for minion in minions_lst:

	s = random.choice([1, 2])

	if s == 2:
		alices_warband.append(minion)
	else:
		bobs_warband.append(minion)

# change it:
# create objects immidietely
# choose randomly fromthe list
# make minions dict??? or what?

# for i in range(14):
# 	s = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
# 	p = random.choice([1, 2])

# 	if p == 2:
# 		minion = create_minion(s)
# 		alices_warband.append(minion)
# 	else:
# 		bobs_warband.append(minion)



Player_1 = Player("Alice", alices_warband)
Player_2 = Player("Bob", bobs_warband)


def attack_in_combat(minion1, minion2):
	minion1.take_damage(minion2.attack)
	minion2.take_damage(minion1.attack)

	return minion1, minion2

def count_damage(warband):
	damage = 0

	for minion in warband:
		damage += minion.tier

	return damage


def game_order():

	order = True

	p1 = Player_1.warband
	p2 = Player_2.warband

	Player_1.warband = copy.deepcopy(p1)
	Player_2.warband = copy.deepcopy(p2)

	if len(Player_1.warband) < len(Player_2.warband):
		order = False
	elif len(Player_1.warband) == len(Player_2.warband):
		order = random.choice([True, False])

	if order == True:
		game = [p1, p2]
	else:
		game = [p2, p1]

	return p1, p2, game

def kill_minion(minion, minions):
	if minion.has_deathrattle:
		minion.deathrattle(minions)
	return minions

def redwhelp_attack(redwhelp, game, attackers_minions, opponents_minions, i):
	start_rw_attack = redwhelp.attack

	redwhelp.add_damage(attackers_minions)
	redwhelp.take_no_damage()
	attacked_minion = random.choice(opponents_minions)
	redwhelp, attacked_minion = attack_in_combat(redwhelp, attacked_minion)

	redwhelp.attack = start_rw_attack

	if attacked_minion.health < 1:
		
		# for minion in game[i]:
		# 	print(minion.name)
		# print()
		# print(attacked_minion.name, "goni")
		# print()
		game[i].remove(attacked_minion)
		game[i] = kill_minion(attacked_minion, opponents_minions)
		
		# for minion in game[i]:
		# 	print(minion.name)
		# print()

	return game

def start_of_combat(game):

	i = 1
	for attackers_minions in game:
		opponents_minions = game[i]
		for minion in attackers_minions:
			if isinstance(minion, RedWhelp):
				redwhelp_attack(minion, game, attackers_minions, opponents_minions, i)
		i = 0

	p1 = game[0]
	p2 = game[1]
	return p1, p2, game

def count_taunts(px):
	output = 0
	taunted_minions = []


	for p in px:

		if p.is_taunted == True:
			output += 1
			taunted_minions.append(p)

	return output, taunted_minions


p1, p2, game = game_order()

p1, p2, game = start_of_combat(game)

def combat(p1, p2, game):

	# for p in game:
	# 	for minion in p:
	# 		print(minion.name)
	# 		print(minion.health)
	# 	print()

	# start of combat:





	# for p in game:
	# 	for minion in p:
	# 		print(minion.name, 2)
	# 		print(minion.health, 2)
	# 	print()

	a, b = 0, 1
	first_player_attack_minion = 0
	second_player_attack_minion = 0

	attacking_minion = first_player_attack_minion

	while p1 and p2:

		attacked_minion = None

		if count_taunts(game[a + b])[0] > 0:
			taunts = count_taunts(game[a + b])[1]
			r = random.randint(0, len(taunts) - 1)
			minion = taunts[r]

			for i in range(len(game[a + b])):
				if game[a + b][i].name == minion.name:
					attacked_minion = i
					break

		else:
			attacked_minion = random.randint(0, len(game[a + b]) - 1)

		minion1 = game[a][attacking_minion]

		minion2 = game[a + b][attacked_minion]
		
		# print()
		# print(minion1.name, minion1.attack, minion1.health)
		# print(minion2.name, minion2.attack, minion2.health)

		minion1, minion2 = attack_in_combat(minion1, minion2)

		# print(minion1.name, minion1.attack, minion1.health)
		# print(minion2.name, minion2.attack, minion2.health)
		# print(minion2.health, minion2.name)
		# print(p1)
		# print(p2)


		if minion1.health <= 0:
			# print()
			# print("minion1")
			# for i in game[a]:
			# 	print(i.name)
			# 	print(i.health)
			# 	print(i.attack)
			# print()
			# print("killed:", game[a][attacking_minion].name)
			# print()
			del game[a][attacking_minion]
			
			kill_minion(minion1, game[a])
			# print(not p1, not p2)
			# for i in game[a]:
			# 	print(i.name)
			# 	print(i.health)
			# 	print(i.attack)
			# print()
			attacking_minion -= 1
			# ??

		if minion2.health <= 0:
			# print()
			# print("minion2")
			# for i in game[a + b]:
			# 	print(i.name)
			# 	print(i.health)
			# 	print(i.attack)
			# print()
			# print("killed:", game[a + b][attacked_minion].name)
			# print()
			del game[a + b][attacked_minion]

			kill_minion(minion2, game[a + b])
			# print(not p1, not p2)
			# for i in game[a + b]:
			# 	print(i.name)
			# 	print(i.health)
			# 	print(i.attack)
			# print()

		attacking_minion += 1

		if a == 0:
			a = 1
			b = -1

			first_player_attack_minion = attacking_minion

			if second_player_attack_minion >= len(game[1]):
				second_player_attack_minion = 0

			attacking_minion = second_player_attack_minion

		else:
			a = 0
			b = 1

			second_player_attack_minion = attacking_minion
			
			if first_player_attack_minion >= len(game[0]):
				first_player_attack_minion = 0

			attacking_minion = first_player_attack_minion


	if not p1 and not p2:
		print("NO WINNER")
		damage = 0


	else:
		winner = Player_1.name if p1 else Player_2.name 
		print(f'{winner} WINNER')
		
		damage = count_damage(p1) if p1 else count_damage(p2)
		print(f'DAMAGE: {damage}')

combat(p1, p2, game)
