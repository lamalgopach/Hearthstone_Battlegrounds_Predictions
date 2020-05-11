import random
from random import choice
import copy
from battle import Player, Battle, GameState
from minions import RedWhelp
from creating_minions_in_warbands import create_warband


alices_warband = create_warband()
bobs_warband = create_warband()

Player1 = Player("Alice", alices_warband)
Player2 = Player("Bob", bobs_warband)

battle = Battle(Player1, Player2)


def attack_in_combat(minion1, minion2):

	minion1.attack()

	minion1.take_damage(minion2.attack_value)
	minion2.take_damage(minion1.attack_value)

	return minion1, minion2


w1, w2, game = battle.choose_first()

battle.print_state("START OF THE GAME: ", w1, w2)

attacking_player = Player1 if game[0] == w1 else Player2
attacked_player = Player2 if game[1] == w2 else Player1

attacking_warband = w1 if game[0] == w1 else w2
attacked_warband = w2 if game[1] == w2 else w1

game_state = GameState(Player1, Player2, w1, w2, attacking_player, attacked_player, 
						attacking_warband, attacked_warband)


def count_taunts(px):
	output = 0
	taunted_minions = []

	for p in px:
		if p.taunt == True:
			output += 1
			taunted_minions.append(p)
	print(output, taunted_minions)
	return output, taunted_minions


def combat(w1, w2, game):
	# start of combat --> red whelp:
	i = 1
	for friendly_minions in game:
		enemy_minions = game[i]
		for minion in friendly_minions:
			if isinstance(minion, RedWhelp):
				minion.start_of_combat(friendly_minions, game, i)
		i = 0

	# battle.print_state("Warbands after start of combat: ", w1, w2)

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



	# class_trial:

	while w1 and w2:
		# assign attacked minion:
		attacked_minion = None
		# count dead minions:
		dead_attacking_minion = 0
		dead_attacked_minion = 0
		

		if count_taunts(game_state.attacked_warband)[0] > 0:
			taunts = count_taunts(game_state.attacked_warband)[1]
			r = random.randint(0, len(taunts) - 1)
			minion = taunts[r]

			for i in range(len(game_state.attacked_warband)):
				if game_state.attacked_warband[i].name == minion.name:
					attacked_minion = i
					break


			print("twoj szczesliwy numerek", attacked_minion)	
		# otherwise attacked minion is chosen randomly:
		else:
			attacked_minion = random.randint(0, len(attacked_warband) - 1)


		# create minions in game:
		minion1 = game_state.attacking_warband[game_state.attack_i]
		minion2 = game_state.attacked_warband[attacked_minion]
			
		print("attacker", minion1.name, minion1.attack_value, minion1.health)
		print("attacked", minion2.name, minion2.attack_value, minion2.health)

		# attack phase:
		minion1, minion2 = attack_in_combat(minion1, minion2)
		# print("after attack:")
		# print("attacker", minion1.name, minion1.attack_value, minion1.health)
		# print("attacked", minion2.name, minion2.attack_value, minion2.health)

		if minion1.health < 1:
			# player = create link to player
			# minion1.die(game[a], offensive, player)
			minion1.die(attacking_warband, game_state.attack_i)
			dead_attacking_minion = 1

		if minion2.health < 1:
			# minion2.die(game[b], attacked_minion, player)
			minion2.die(attacked_warband, attacked_minion)
			dead_attacked_minion += 1


		# next minion:
		# (if attacker is dead we should keep track it)
		game_state.attack_i += 1 - dead_attacking_minion


		# if the last minion in the warband was attacking start once again:
		if game_state.attack_i > len(attacking_warband) - 1:
			game_state.attack_i = 0

		if dead_attacked_minion == 1:
			if game_state.attacked_i > attacked_minion:
				game_state.attacked_i -= 1

		# if attacked player has attacking his last minion in the warband 
		# start again:
		if game_state.attacked_i > len(attacked_warband) - 1:
			game_state.attacked_i = 0

		# print()	
		# print("previous turn indexes:")
		# print(game_state.attack_i)
		# print(game_state.attacked_i)
		# battle.print_state(f'Warbands after {game_state.attacking_player.name}\'s attack: ', w1, w2)

		# end of turn, change the player:

		game_state.next_turn()
		# print("next turn indexes:")
		# print(game_state.attack_i)
		# print(game_state.attacked_i)
		# print()


####################################################################
	# while w1 and w2:
	# 	# assign attacked minion:
	# 	attacked_minion = None
	# 	# count dead minions:
	# 	dead_attacking_minion = 0
	# 	dead_attacked_minion = 0

	# 	#check if there are taunts:
	# 	if count_taunts(game[b])[0] > 0:
	# 		taunts = count_taunts(game[b])[1]
	# 		r = random.randint(0, len(taunts) - 1)
	# 		minion = taunts[r]

	# 		for i in range(len(game[b])):
	# 			if game[b][i].name == minion.name:
	# 				attacked_minion = i
	# 				break
	# 	# otherwise attacked minion is chosen randomly:
	# 	else:
	# 		attacked_minion = random.randint(0, len(game[b]) - 1)

	# 	# create minions in game:
	# 	minion1 = game[a][offensive]
	# 	minion2 = game[b][attacked_minion]
			
	# 	# print("attacker", minion1.name, minion1.attack_value, minion1.health)
	# 	# print("attacked", minion2.name, minion2.attack_value, minion2.health)

	# 	# attack phase:
	# 	minion1, minion2 = attack_in_combat(minion1, minion2)

	# 	# if minion1.health < 1:
	# 	# 	print("dead:", minion1.name)
	# 	# if minion2.health < 1:
	# 	# 	print("dead:", minion2.name)

	# 	# if minion1 or minion2 has < 0 health -> minion dies:
	# 	if minion1.health < 1:
	# 		# player = create link to player
	# 		# minion1.die(game[a], offensive, player)
	# 		minion1.die(game[a], offensive)
	# 		dead_attacking_minion = 1

	# 	if minion2.health < 1:
	# 		# minion2.die(game[b], attacked_minion, player)
	# 		minion2.die(game[b], attacked_minion)
	# 		dead_attacked_minion += 1


	# 	# next minion:
	# 	offensive += 1
	# 	# if attacker is dead we shoul keep track it:
	# 	offensive = offensive - dead_attacking_minion

	# 	# if offensive was the last minion in the warband start once again:
	# 	if offensive > len(game[a]) - 1:
	# 		offensive = 0

	# 	if dead_attacked_minion == 1:
	# 		if defensive > attacked_minion:
	# 			defensive -= 1

	# 	# if attacked player has attacking his last minion in the warband 
	# 	# start again:
	# 	if defensive > len(game[b]) - 1:
	# 		defensive = 0

	# 	p = Player1.name if game[a] == w1 else Player2.name
	# 	# battle.print_state(f'Warbands after {p}\'s attack: ', w1, w2)

	# 	# end of turn, change the player:
	# 	if a == 0:
	# 		a = 1
	# 		b = 0

	# 		first_player_minion_attacker = offensive
	# 		second_player_minion_attacker = defensive

	# 		offensive = second_player_minion_attacker
	# 		defensive = first_player_minion_attacker

	# 	else:
	# 		a = 0
	# 		b = 1

	# 		first_player_minion_attacker = defensive
	# 		second_player_minion_attacker = offensive

	# 		offensive = first_player_minion_attacker
	# 		defensive = second_player_minion_attacker

	if not w1 and not w2:
		print("NO WINNER")
		damage = 0

	else:
		print()
		winner = Player1.name if w1 else Player2.name 
		loser = Player2 if w1 else Player1
		print(f'{winner} WINNER')
		print(f'{loser.name} LOSER')

		damage = Player1.count_final_damage(w1) if w1 else Player2.count_final_damage(w2)

		loser.life -= damage
		print(f'DAMAGE: {damage}')
		print(Player1.life, "w1 life", Player1.name)
		print(Player2.life, "w2 life", Player2.name)


combat(w1, w2, game)