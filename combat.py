import random
from random import choice
import copy
from minions import Card, Player



# classes written:
murloc_warleader = Card("Murloc Warleader", 3, 3, 2, 1, False, False)
glyph_guardian = Card("Glyph Guardian", 2, 4, 2, 2, False, False)
red_whelp = Card("Red Whelp", 1, 2, 1, 2, False, False)


#taunt:
dragonspawn_lieutenant = Card("Dragonspawn Lieutenant", 2, 3, 1, 2, True, False)
# + divine shield
righteous_protector = Card("Righteous Protector", 1, 1, 1, 0, True, True)



#deathrattles:
spawn_of_nzoth = Card("Spawn Of n'Zoth", 2, 2, 2, 0, False, False)
infested_wolf = Card("Infested Wolf", 3, 3, 3, 3, False, False)
selfless_hero = Card("Selfless Hero", 2, 1, 1, 0, False, False)

# battlecry:
rockpool_hunter = Card("Rockpool Hunter", 2, 3, 1, 1, False, False)
red_whelp_a = Card("Red Whelp", 1, 2, 1, 2, False, False)
red_whelp_b = Card("Red Whelp", 1, 2, 1, 2, False, False)
red_whelp_c = Card("Red Whelp", 1, 2, 1, 2, False, False)

alices_warband = [dragonspawn_lieutenant, red_whelp_a, selfless_hero] 
bobs_warband = [righteous_protector, red_whelp_b, spawn_of_nzoth]

Player_1 = Player("Alice", alices_warband)
Player_2 = Player("Bob", bobs_warband)



def attack(minion_1, minion_2):


	minion_1.take_damage(minion_2.attack)
	minion_2.take_damage(minion_1.attack)
	print(minion_1.has_ds, "taak")
	print(minion_2.has_ds, "ahhak")

	return minion_1, minion_2

def count_damage(warband):

	damage = 0

	for minion in warband:
		damage += minion.tier

	return damage


def play_first():

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


p1, p2, game = play_first()

def combat(p1, p2, game):

	#game
	index = 0
	factor = 1

	first_player_idx, second_player_idx = 0, 0

	next_minion = first_player_idx


	while p1 and p2:


		taunts_num, taunts = count_taunts(game[index + factor])
		attacked_minion = None

		if taunts_num > 0:
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



		print()

		print(minion_1.name, minion_1.attack, minion_1.health)
		print(minion_2.name, minion_2.attack, minion_2.health)

		minion_1, minion_2 = attack(minion_1, minion_2)

		print(minion_1.name, minion_1.attack, minion_1.health)
		print(minion_2.name, minion_2.attack, minion_2.health)
		print(minion_2.health, minion_2.name)
		print(p1)
		print(p2)


		if minion_1.health <= 0:
			del game[index][next_minion]
			next_minion -= 1

		if minion_2.health <= 0:
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


		elif not p1 or not p2:
			winner = Player_1.name if p1 else Player_2.name 
			print(f'{winner} WINNER')
			
			damage = count_damage(p1) if p1 else count_damage(p2)
			print(f'DAMAGE: {damage}')


		# elif not p2:
		# 	print(Player_1.name, "WINNER")
		# 	damage = count_damage(p1)

		# elif not p1:
		# 	print(Player_2.name, "WINNER")
		# 	damage = count_damage(p2)

	# print("DAMAGE: ", damage)

combat(p1, p2, game)
