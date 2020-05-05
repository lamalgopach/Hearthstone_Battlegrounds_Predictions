import random
from random import choice
import copy
from minions import Player, RedWhelp
from creating_minions_in_warbands import create_warband

# to be removed later:
from minions import Card, SpawnOfnZoth, SelflessHero, GlyphGuardian, InfestedWolf


alices_warband = create_warband()
bobs_warband = create_warband()



# to be removed later:
# minions completed:
# dragonspawn_lieutenant = Card("Dragonspawn Lieutenant", 2, 3, 1, 2, True, False, False)
# righteous_protector = Card("Righteous Protector", 1, 1, 1, 0, True, True, False)
# spawn_of_nzoth = SpawnOfnZoth("Spawn Of n'Zoth", 2, 2, 2, 0, False, False, True)
# spawn_of_nzoth_2 = SpawnOfnZoth("Spawn Of n'Zoth", 2, 2, 2, 0, False, False, True)
# selfless_hero = SelflessHero("Selfless Hero", 2, 1, 1, 0, False, False, True)
# selfless_hero_2 = SelflessHero("Selfless Hero", 2, 1, 1, 0, False, False, True)
# glyph_guardian = GlyphGuardian("Glyph Guardian", 2, 4, 2, 2, False, False, False)
# infested_wolf = InfestedWolf("Infested Wolf", 3, 3, 3, 3, False, False, True)
# infested_wolf_2 = InfestedWolf("Infested Wolf", 3, 3, 3, 3, False, False, True)
# infested_wolf_3 = InfestedWolf("Infested Wolf", 3, 3, 3, 3, False, False, True)

# # done but need to be finished (random player order)
# red_whelp = RedWhelp("Red Whelp", 1, 2, 1, 2, False, False, False)
# red_whelp_2 = RedWhelp("Red Whelp", 1, 2, 1, 2, False, False, False)

# # to do:
# murloc_warleader = Card("Murloc Warleader", 3, 3, 2, 1, False, False, False)

# # battlecry:
# rockpool_hunter = Card("Rockpool Hunter", 2, 3, 1, 1, False, False, False)
# rockpool_hunter_2 = Card("Rockpool Hunter", 2, 3, 1, 1, False, False, False)

# alices_warband = [infested_wolf, infested_wolf_2, red_whelp, glyph_guardian, murloc_warleader, 
# 				rockpool_hunter, infested_wolf_3]

# bobs_warband = [dragonspawn_lieutenant, spawn_of_nzoth, red_whelp_2, rockpool_hunter_2, 
# 				selfless_hero, selfless_hero_2, spawn_of_nzoth_2]


Player_1 = Player("Alice", alices_warband)
Player_2 = Player("Bob", bobs_warband)

print("START OF THE GAME: ")
print("Alices:")
for minion in alices_warband:
	print(minion.name)
print()

print("Bobs:")
for minion in bobs_warband:
	print(minion.name)
print()


def attack_in_combat(minion1, minion2):
	if minion1.name == "GlyphGuardian":
		minion1.add_attack()
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

# def kill_minion(minion, minions, j):
# 	if minion.has_deathrattle:
# 		minion.deathrattle(minions, j)
# 	return minions

def redwhelp_attack(redwhelp, game, attackers_minions, opponents_minions, i):

	start_rw_attack = redwhelp.attack

	redwhelp.add_damage(attackers_minions)
	# redwhelp.take_no_damage()
	attacked_minion = random.choice(opponents_minions)
	redwhelp, attacked_minion = attack_in_combat(redwhelp, attacked_minion)
	print("red_whelp's attack: ", redwhelp.attack)

	redwhelp.attack = start_rw_attack

	if attacked_minion.health < 1:
		j = game[i].index(attacked_minion)
		attacked_minion.die(game[i], j)

	print("attacked minion:", attacked_minion.name)
	print("WARBANDS AFTER THIS COMBAT: ")

	for p in game:
		for minion in p:
			print(minion.attack, minion.health, minion.name)
		print()
	print()


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

	# start of combat:
	i = 1
	for attackers_minions in game:
		opponents_minions = game[i]
		for minion in attackers_minions:
			if isinstance(minion, RedWhelp):
				redwhelp_attack(minion, game, attackers_minions, opponents_minions, i)
		i = 0

	print()
	print("Minions after start of combat:")
	print(Player_1.name)
	for minion in p1:
		print(minion.name, minion.health, minion.attack)
	print()
	print(Player_2.name)
	for minion in p2:
		print(minion.name, minion.health, minion.attack, minion.has_ds)
	print()

	# game indexes, change each turn:
	# a - attacking
	# b - attacked
	a, b = 0, 1

	# associated with game[0], index of attacking minion while 1st player turn:
	first_player_minion_attacker = 0
	
	# associated with game[1], index of attacking minion while 2nd player turn:
	second_player_minion_attacker = 0

	# first player is attacking:
	offensive = first_player_minion_attacker

	# track the second player index of attacker:
	defensive = second_player_minion_attacker

	while p1 and p2:
		# assign attacked minion:
		attacked_minion = None
		# count dead minions:
		dead_attacker_minion = 0
		dead_attacked_minion = 0

		#check if there are taunts:
		if count_taunts(game[b])[0] > 0:
			taunts = count_taunts(game[b])[1]
			r = random.randint(0, len(taunts) - 1)
			minion = taunts[r]

			for i in range(len(game[b])):
				if game[b][i].name == minion.name:
					attacked_minion = i
					break
		# otherwise attaked minion is chosen randomly:
		else:
			attacked_minion = random.randint(0, len(game[b]) - 1)

		# create minions in game:
		minion1 = game[a][offensive]
		minion2 = game[b][attacked_minion]
			
		print("attacker", minion1.name, minion1.attack, minion1.health)
		print("attacked", minion2.name, minion2.attack, minion2.health)


		# attack phase:
		minion1, minion2 = attack_in_combat(minion1, minion2)

		# if minion1.health < 1:
		# 	print("dead:", minion1.name)
		# if minion2.health < 1:
		# 	print("dead:", minion2.name)

		# if minion1 or minion2 has < 0 health -> minion dies:
		if minion1.health < 1:
			minion1.die(game[a], offensive)
			dead_attacker_minion = 1

		if minion2.health < 1:
			minion2.die(game[b], attacked_minion)
			dead_attacked_minion += 1


		# next minion:
		offensive += 1
		# if attacker is dead we shoul keep track it:
		offensive = offensive - dead_attacker_minion

		# if offensive was the last minion in the warband start once again:
		if offensive > len(game[a]) - 1:
			offensive = 0

		if dead_attacked_minion == 1:
			if defensive > attacked_minion:
				defensive -= 1

		# if attacked player has attacking his last minion in the warband 
		# start again:
		if defensive > len(game[b]) - 1:
			defensive = 0

		print(Player_1.name, " warband after combat:")
		print(p1)
		print(Player_2.name, " warband after combat:")
		print(p2)
		print()

		# end of turn, change the player:
		if a == 0:
			a = 1
			b = 0

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

	if not p1 and not p2:
		print("NO WINNER")
		damage = 0


	else:
		winner = Player_1.name if p1 else Player_2.name 
		print(f'{winner} WINNER')
		
		damage = count_damage(p1) if p1 else count_damage(p2)
		print(f'DAMAGE: {damage}')

combat(p1, p2, game)