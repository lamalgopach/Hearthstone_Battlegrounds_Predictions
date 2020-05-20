import random
from random import choice
import copy
from battle import Player, Warband, BattleState
# from minions import KaboomBot, MurlocWarleader

print("100 simulations for those warbands:")
print()
print("Player1: Alice")	
print("Minion's name, attack, health, Divine Shield:")	
print("Rockpool Hunter 2 3 False")
print("Infested Wolf 3 3 False")
print("Red Whelp 1 2 False")
print("Glyph Guardian 2 4 False")
print("Spawn Of n'Zoth 2 2 False")
print("Righteous Protector 1 1 True")
print("Selfless Hero 2 1 False")
print()

print("Player2: Bob")
print("Minion's name, attack, health, Divine Shield:")	
print("Rockpool Hunter 2 3 False")
print("Dragonspawn Lieutenant 2 3 False")
print("Selfless Hero 2 1 False")
print("Glyph Guardian 2 4 False")
print("Red Whelp 1 2 False")
print("Spawn Of n'Zoth 2 2 False")
print("Infested Wolf 3 3 False")
print()

def choose_first(player1, player2):
	order = True

	w1 = copy.deepcopy(player1.warband)
	w2 = copy.deepcopy(player2.warband)

	if len(w1.warband) < len(w2.warband):
		order = False
	elif len(w1.warband) == len(w2.warband):
		order = random.choice([True, False])

	if order == True:
		game = [w1, w2]
	else:
		game = [w2, w1]

	return w1, w2, game

def start_of_game():
	# create Alices Warband as object of Warband class:
	alices_warband = Warband("Alice")
	bobs_warband = Warband("Bob")
	# use warband method to create warband with minions:
	alices_warband.create_warband()
	bobs_warband.create_warband()
	# create object of Player class and link this warband to this Player:
	Player1 = Player("Alice", alices_warband)
	Player2 = Player("Bob", bobs_warband)

	#what are players names? into console

	# CREATE THE ORDER OF ATTACK:
	w1, w2, game = choose_first(Player1, Player2)

	attacking_player = Player1 if game[0] == w1 else Player2
	attacked_player = Player2 if game[1] == w2 else Player1

	attacking_warband = w1 if game[0] == w1 else w2
	attacked_warband = w2 if game[1] == w2 else w1

	battle_state = BattleState(attacking_player, attacked_player, attacking_warband, attacked_warband)
	# battle_state.print_state("START OF THE GAME: ")

	return w1, w2, battle_state, Player1, Player2

def combat(w1, w2):
	winner = None

	battle_state.start_of_combat()
	# battle_state.print_state("after start of combat:")

	# attack till at least one player has no minions:
	while battle_state.attacking_warband.warband and battle_state.attacked_warband.warband:

		# assign attacked minion:
		attacked_minion = battle_state.choose_attacked_minion()

		# create minions in game:
		minion1 = battle_state.attacking_warband.warband[battle_state.attack_i]
		minion2 = battle_state.attacked_warband.warband[attacked_minion]

		# attack phase:
		minion1.attack()
		minion1.take_damage(minion2.attack_value)
		minion2.take_damage(minion1.attack_value)
		# print("Attacking: ", battle_state.attacking_player.name)
		# print(minion1.name, minion1.attack_value, minion1.health)
		# print("Attacked: ", battle_state.attacked_player.name)
		# print(minion2.name, minion2.attack_value, minion2.health)
		# print()
		# count dead minions:
		dead_attacking_minion = 0
		dead_attacked_minion = 0

		# while ?
		# iterating in minions list?

		if minion1.health < 1 or minion2.health < 1:
			if minion1.health < 1:
				minion1.die(battle_state.attacking_warband.warband, battle_state.attack_i)
				dead_attacking_minion = 1

			if minion2.health < 1:
				minion2.die(battle_state.attacked_warband.warband, attacked_minion)
				dead_attacked_minion = 1

			if dead_attacking_minion == 1:
				if minion1.has_deathrattle:
					minion1.deathrattle(battle_state.attacking_warband.warband, battle_state.attacked_warband.warband, battle_state.attack_i)
			
			if dead_attacked_minion == 1:
				if minion2.has_deathrattle:
					minion2.deathrattle(battle_state.attacked_warband.warband, battle_state.attacking_warband.warband, attacked_minion)

			# attacking_warband_deathrattle = False
			# attacked_warband_deathrattle = False

			# for minion in battle_state.attacking_warband.warband:
			# 	if minion.health < 1:
			# 		i = battle_state.attacking_warband.warband.index(minion)
			# 		minion.die(battle_state.attacking_warband.warband, i)
			# 		dead_attacking_minion += 1
			# 		if minion.has_deathrattle:
			# 			attacking_warband_deathrattle = True


			# for minion in battle_state.attacked_warband.warband:
			# 	if minion.health < 1:
			# 		i = battle_state.attacked_warband.warband.index(minion)
			# 		minion.die(battle_state.attacked_warband.warband, i)
			# 		dead_attacked_minion += 1	
			# 		if minion.has_deathrattle:
			# 			attacked_warband_deathrattle = True	

			# if attacking_warband_deathrattle:
			# 	pass

		# next minion:
		# (if attacker is dead we should keep track it)
		battle_state.attack_i += 1 - dead_attacking_minion

		# if the last minion in the warband was attacking start once again:
		if battle_state.attack_i > len(battle_state.attacking_warband.warband) - 1:
			battle_state.attack_i = 0

		if dead_attacked_minion == 1:
			if battle_state.attacked_i > attacked_minion:
				battle_state.attacked_i -= 1

		# if attacked player has attacking his last minion in the warband 
		# start again:
		if battle_state.attacked_i > len(battle_state.attacked_warband.warband) - 1:
			battle_state.attacked_i = 0

		# statement = f'Warbands after {battle_state.attacking_player.name}\'s attack:'
		# battle_state.print_state(statement)
		# end of turn, change the player:
		battle_state.play_next()


	if not w1.warband and not w2.warband:
		# print("NO WINNER")
		damage = 0

	else:
		# print()
		winner = Player1 if w1.warband else Player2
		loser = Player2 if w1.warband else Player1
		# print(f'{winner.name} WINNER')
		# print(f'{loser.name} LOSER')
		damage = Player1.count_final_damage(w1.warband) if w1.warband else Player2.count_final_damage(w2.warband)
		loser.life -= damage
		# print(f'DAMAGE: {damage}')

	# print(Player1.life, "Player1 life", Player1.name)
	# print(Player2.life, "Player2 life", Player2.name)

	# print(len(Player1.warband.warband))
	# print(len(Player2.warband.warband))

	return winner



i = 100
z = 0
alice_winner = 0
bob_winner = 0
no_winner = 0
while i > 0:
	w1, w2, battle_state, Player1, Player2 = start_of_game()
	winner = combat(w1, w2)
	if winner:
		alice_winner += 1 if winner.name == "Alice" else 0
		bob_winner += 1 if winner.name == "Bob" else 0
	else:
		no_winner += 1

	i -= 1
print(alice_winner, "Alice's winnings")
print(alice_winner / 100, "Alice's probability of winw")
print(bob_winner, "Bob's winnings")
print(bob_winner / 100, "Bob's probability of win")
print(no_winner / 100, "Probability of no-win")
print(alice_winner + bob_winner + no_winner, "checkpoint")
