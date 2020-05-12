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

		# otherwise attacked minion is chosen randomly:
		else:
			attacked_minion = random.randint(0, len(game_state.attacked_warband) - 1)


		# create minions in game:
		minion1 = game_state.attacking_warband[game_state.attack_i]
		minion2 = game_state.attacked_warband[attacked_minion]
			
		print("attacker", minion1.name, minion1.attack_value, minion1.health)
		print("attacked", minion2.name, minion2.attack_value, minion2.health)
		print()
		# attack phase:
		minion1, minion2 = attack_in_combat(minion1, minion2)

		print("after attack:")
		print("attacker", minion1.name, minion1.attack_value, minion1.health)
		print("attacked", minion2.name, minion2.attack_value, minion2.health)
		print()

		if minion1.health < 1:
			minion1.die(game_state.attacking_warband, game_state.attack_i)
			dead_attacking_minion = 1

		if minion2.health < 1:
			minion2.die(game_state.attacked_warband, attacked_minion)
			dead_attacked_minion += 1


		# next minion:
		# (if attacker is dead we should keep track it)
		game_state.attack_i += 1 - dead_attacking_minion

		# if the last minion in the warband was attacking start once again:
		if game_state.attack_i > len(game_state.attacking_warband) - 1:
			game_state.attack_i = 0

		if dead_attacked_minion == 1:
			if game_state.attacked_i > attacked_minion:
				game_state.attacked_i -= 1

		# if attacked player has attacking his last minion in the warband 
		# start again:
		if game_state.attacked_i > len(game_state.attacked_warband) - 1:
			game_state.attacked_i = 0


		battle.print_state(f'Warbands after {game_state.attacking_player.name}\'s attack: ', w1, w2)

		# end of turn, change the player:
		game_state.next_turn()


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