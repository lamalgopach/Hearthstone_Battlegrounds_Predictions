import random
from random import choice
import copy
from minions import Player, minions_lst, Card, SelflessHero, SpawnOfnZoth, InfestedWolf
from minions import GlyphGuardian, RedWhelp

alices_warband = [] 
bobs_warband = []

# for minion in minions_lst:

# 	s = random.choice([1, 2])

# 	if s == 2:
# 		alices_warband.append(minion)
# 	else:
# 		bobs_warband.append(minion)


dragonspawn_lieutenant = Card("Dragonspawn Lieutenant", 2, 3, 1, 2, True, False, False)
righteous_protector = Card("Righteous Protector", 1, 1, 1, 0, True, True, False)
spawn_of_nzoth = SpawnOfnZoth("Spawn Of n'Zoth", 2, 2, 2, 0, False, False, True)
infested_wolf = InfestedWolf("Infested Wolf", 3, 3, 3, 3, False, False, True)
selfless_hero = SelflessHero("Selfless Hero", 2, 1, 1, 0, False, False, True)
glyph_guardian = GlyphGuardian("Glyph Guardian", 2, 4, 2, 2, False, False, False)
red_whelp = RedWhelp("Red Whelp", 1, 2, 1, 2, False, False, False)



# classes written:
murloc_warleader = Card("Murloc Warleader", 3, 3, 2, 1, False, False, False)

# battlecry:
rockpool_hunter = Card("Rockpool Hunter", 2, 3, 1, 1, False, False, False)

alices_warband = [dragonspawn_lieutenant, righteous_protector, murloc_warleader, glyph_guardian, spawn_of_nzoth, rockpool_hunter]
bobs_warband = [red_whelp, infested_wolf, selfless_hero]


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


	print("game:")
	for p in game:
		for minion in p:
			print(minion.name)
			print(minion.health)
		print()

	print("p1:")
	print(Player_1.name)
	for minion in p1:
		print(minion.name)

	print()
	print("p2:")
	print(Player_2.name)
	for minion in p2:
		print(minion.name)

	# start of combat:

	i = 1
	for attackers_minions in game:
		opponents_minions = game[i]
		for minion in attackers_minions:
			if isinstance(minion, RedWhelp):
				redwhelp_attack(minion, game, attackers_minions, opponents_minions, i)
		i = 0



	# for p in game:
	# 	for minion in p:
	# 		print(minion.name, 2)
	# 		print(minion.health, 2)
	# 	print()

	a, b = 0, 1
	first_player_minion_attacker = 0
	# associated with game[0]
	second_player_minion_attacker = 0
	# associated with game[1]

	offensive = first_player_minion_attacker

	# offensive = first_player_minion_attacker
	defensive = second_player_minion_attacker

	while p1 and p2:
		print()
		print(first_player_minion_attacker, offensive)
		print(second_player_minion_attacker, defensive)


		attacked_minion = None
		dead_attacker_minion = 0
		dead_attacked_minion = 0

		if count_taunts(game[b])[0] > 0:
			taunts = count_taunts(game[b])[1]
			r = random.randint(0, len(taunts) - 1)
			minion = taunts[r]

			for i in range(len(game[b])):
				if game[b][i].name == minion.name:
					attacked_minion = i
					break

		else:
			attacked_minion = random.randint(0, len(game[b]) - 1)

		minion1 = game[a][offensive]

		minion2 = game[b][attacked_minion]
		
		print()
		print("attacker", minion1.name, minion1.attack, minion1.health)
		print("attacked", minion2.name, minion2.attack, minion2.health)

		minion1, minion2 = attack_in_combat(minion1, minion2)

		if minion1.health < 1:
			print("dead:", minion1.name)
		if minion2.health < 1:
			print("dead:", minion2.name)
		# print(game[0])
		# print(game[1])
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
			# print("killed:", game[a][offensive].name)
			# print()
			del game[a][offensive]
			
			kill_minion(minion1, game[a])
			# print(not p1, not p2)
			# for i in game[a]:
			# 	print(i.name)
			# 	print(i.health)
			# 	print(i.attack)
			# print()
			dead_attacker_minion = 1
			# ??

		if minion2.health <= 0:
			# print()
			# print("minion2")
			# for i in game[b]:
			# 	print(i.name)
			# 	print(i.health)
			# 	print(i.attack)
			# print()
			# print("killed:", game[b][attacked_minion].name)
			# print()
			del game[b][attacked_minion]

			kill_minion(minion2, game[b])
			# print(not p1, not p2)
			# for i in game[b]:
			# 	print(i.name)
			# 	print(i.health)
			# 	print(i.attack)
			# print()
			dead_attacked_minion += 1


		offensive += 1

		print()
		print(alices_warband)
		print(bobs_warband)
		print()

		offensive = offensive - dead_attacker_minion

		if offensive > len(game[a]) - 1:
			offensive = 0

		if dead_attacked_minion == 1:
			if defensive > attacked_minion:
				defensive -= 1

		if defensive > len(game[b]) - 1:
			defensive = 0

		# end of turn, change the player:
		
		print()
		print("next attacking: ", offensive, "team", a)



		if a == 0:
			a = 1
			b = 0

			# first_player_minion_attacker = offensive
			# second_player_minion_attacker = defensive

			first_player_minion_attacker = offensive
			second_player_minion_attacker = defensive

			offensive = second_player_minion_attacker
			defensive = first_player_minion_attacker



		else:
			a = 0
			b = 1

			first_player_minion_attacker = defensive
			second_player_minion_attacker = offensive

			offensive = first_player_minion_attacker
			defensive = second_player_minion_attacker

			# first_player_minion_attacker = defensive
			# second_player_minion_attacker = offensive


		# if a == 0:
		# 	a = 1
		# 	b = -1

		# 	# first_player_minion_attacker = playing_minion
		# 	# second_player_minion_attacker = non_playing_minion
		# 	# offensive = second_player_minion_attacker

		# 	# old:
		# 	first_player_minion_attacker = offensive - dead_attacker_minion	
		# 	# if dead minion attacker index should decrease	
		# 	if first_player_minion_attacker > len(game[0]) - 1:
		# 		# check if index doesnt exceed the list range
		# 		first_player_minion_attacker = 0
			
			# # attacked minion:
			# if dead_attacked_minion > 0:
			# 	# check if attacked minion is dead
			# 	if second_player_minion_attacker > attacked_minion:
			# 		# check if the dead minion is on the next player index
			# 		# or below
			# 		# if so its needed to be decreased
			# 		second_player_minion_attacker -= dead_attacked_minion

			# if second_player_minion_attacker > len(game[1]) - 1:
			# 	# check if idexes doesnt exceed the range of warband
			# 	second_player_minion_attacker = 0

			# offensive = second_player_minion_attacker
			# # assign index of the second warband to the attacking minion

		# else:
		# 	a = 0
		# 	b = 1
		# 	# second_player_minion_attacker = playing_minion
		# 	# first_player_minion_attacker = non_playing_minion
		# 	# offensive = second_player_minion_attacker

		# 	# old:
		# 	second_player_minion_attacker = offensive - dead_attacker_minion
			
		# 	if second_player_minion_attacker > len(game[1]) - 1:
		# 		second_player_minion_attacker = 0

		# 	if dead_attacked_minion > 0:
		# 		if first_player_minion_attacker > attacked_minion:
		# 			first_player_minion_attacker -= dead_attacked_minion

		# 	if first_player_minion_attacker > len(game[0]) - 1:
		# 		first_player_minion_attacker = 0

		# 	offensive = first_player_minion_attacker



# imo we dont need that:

		# if first_player_minion_attacker > len(game[0]) - 1:
		# 	first_player_minion_attacker = 0

		# if second_player_minion_attacker > len(game[1]) - 1:
		# 	second_player_minion_attacker = 0


	if not p1 and not p2:
		print("NO WINNER")
		damage = 0


	else:
		winner = Player_1.name if p1 else Player_2.name 
		print(f'{winner} WINNER')
		
		damage = count_damage(p1) if p1 else count_damage(p2)
		print(f'DAMAGE: {damage}')

combat(p1, p2, game)
