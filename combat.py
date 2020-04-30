import random
from random import choice
import copy
from minions import Card, Player, minions

alices_warband = [] 
bobs_warband = []

for minion in minions:

	s = random.choice([1, 2])

	if s == 2:
		alices_warband.append(minion)
	else:
		bobs_warband.append(minion)


Player_1 = Player("Alice", alices_warband)
Player_2 = Player("Bob", bobs_warband)


def attack(minion1, minion2):
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

def count_taunts(px):

	output = 0
	taunted_minions = []


	for p in px:

		if p.is_taunted == True:
			output += 1
			taunted_minions.append(p)

	return output, taunted_minions


p1, p2, game = game_order()

def combat(p1, p2, game):
	index, factor = 0, 1
	first_player_idx, second_player_idx = 0, 0

	next_minion = first_player_idx

	while p1 and p2:


		# taunts_num, taunts = count_taunts(game[index + factor])
		attacked_minion = None

		if count_taunts(game[index + factor])[0] > 0:
			taunts = count_taunts(game[index + factor])[1]
			r = random.randint(0, len(taunts) - 1)
			minion = taunts[r]

			for i in range(len(game[index + factor])):
				if game[index + factor][i].name == minion.name:
					attacked_minion = i
					break

		else:
			attacked_minion = random.randint(0, len(game[index + factor]) - 1)

		minion_1 = game[index][next_minion]
		minion_2 = game[index + factor][attacked_minion]
		
		# print()
		# print(minion_1.name, minion_1.attack, minion_1.health)
		# print(minion_2.name, minion_2.attack, minion_2.health)

		minion_1, minion_2 = attack(minion_1, minion_2)

		# print(minion_1.name, minion_1.attack, minion_1.health)
		# print(minion_2.name, minion_2.attack, minion_2.health)
		# print(minion_2.health, minion_2.name)
		# print(p1)
		# print(p2)


		if minion_1.health <= 0:
			if minion_1.has_deathrattle:
				random_m = random.choice(game[index])
				minion_1.deathrattle(random_m)
			del game[index][next_minion]
			next_minion -= 1

		if minion_2.health <= 0:
			if minion_2.has_deathrattle:
				random_m = random.choice(game[index + factor])
				minion_2.deathrattle(random_m)
			del game[index + factor][attacked_minion]


		next_minion += 1

		if index == 0:
			index += 1
			factor -= 2

			first_player_idx = next_minion

			if second_player_idx >= len(game[1]):
				second_player_idx = 0

			next_minion = second_player_idx

		else:
			index -= 1
			factor += 2
			second_player_idx = next_minion
			
			if first_player_idx >= len(game[0]):
				first_player_idx = 0

			next_minion = first_player_idx

	if not p1 and not p2:
		print("NO WINNER")
		damage = 0


	else:
		winner = Player_1.name if p1 else Player_2.name 
		print(f'{winner} WINNER')
		
		damage = count_damage(p1) if p1 else count_damage(p2)
		print(f'DAMAGE: {damage}')

combat(p1, p2, game)
