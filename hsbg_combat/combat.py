import copy
from battle import *
from multiple_types_deathrattle_minions import *

def choose_first(player1, player2):
	order = True

	if len(player1.warband) < len(player2.warband):
		order = False
	elif len(player1.warband) == len(player2.warband):
		order = random.choice([True, False])

	if order == True:
		game = [player1.warband, player2.warband]
	else:
		game = [player2.warband, player1.warband]
	return game


def find_minions(warband, dict_, has_effect):

	for minion in warband:
		if minion.has_effect == has_effect:
			print(minion.name)
			print("minion")
			print()
			dict_[minion] = minion.effect

	return dict_


def start_of_game(warband1, warband2):
				
	w1 = copy.deepcopy(warband1)
	w2 = copy.deepcopy(warband2)
	player1 = Player("Alice", warband1, w1, dead_minions=[], this_turn_dead=[], 
						deathrattles=[], effects_causing_next_death=[])
	player2 = Player("Bob", warband2, w2, dead_minions=[], this_turn_dead=[], 
						deathrattles=[], effects_causing_next_death=[])

	player1.effects_after_friend_is_summoned = find_minions(w1, {}, "friend_summoned")
	player2.effects_after_friend_is_summoned = find_minions(w2, {}, "friend_summoned")

	player1.effects_after_friend_is_dead = find_minions(w1, {}, "friend_death")
	player2.effects_after_friend_is_dead = find_minions(w2, {}, "friend_death")

	player1.effects_after_friend_lost_ds = find_minions(w1, {}, "friend_ds_lost")
	player2.effects_after_friend_lost_ds = find_minions(w2, {}, "friend_ds_lost")

	# THE ORDER OF ATTACK:
	game = choose_first(player1, player2)

	attacking_player = player1 if game[0] == player1.warband else player2
	attacked_player = player2 if game[1] == player2.warband else player1

	attacking_warband = player1.warband if game[0] == player1.warband else player2.warband
	attacked_warband = player2.warband if game[1] == player2.warband else player1.warband

	battle = BattleState([attacking_player, attacked_player], 0)
	battle.print_state("START OF THE GAME: ")

	return battle, player1, player2


def combat(battle, player1, player2):
	winner = None
	battle.start_of_combat()
	battle.print_state("after start of combat:")

	# attack till at least one player has no minions:
	while battle.attacking_player.warband and battle.attacked_player.warband:
		# choose attacked minion:

		attacked_minion = battle.choose_attacked_minion()
		battle.attacked_player.attacked_minion = attacked_minion

	 	# create minions in game:
		minion1 = battle.attacking_player.warband[battle.attacking_player.attack_index]
		minion2 = battle.attacked_player.warband[attacked_minion]

		# attack phase:
		minion1.attack()
		minion1.take_damage(minion2.attack_value, minion2.poisonous, battle, status=1)
		if minion1.has_triggered_attack and len(battle.attacked_player.warband) > 1:
			minion1.triggered_attack(battle=battle)
		else:
			minion2.take_damage(minion1.attack_value, minion1.poisonous, battle, status=2)



		print("								Attacking: ", battle.attacking_player.name, battle.attacking_player.attack_index)
		print("								", minion1.name, minion1.attack_value, minion1.health)
		print("								Attacked: ", battle.attacked_player.name)
		print("								", minion2.name, minion2.attack_value, minion2.health)
		print()
		# count dead minions:
		dead_attacking_minions = 0
		dead_attacked_minions = 0

		if minion1.has_overkill and minion2.health < 0:
			minion1.overkill(battle=battle)

		dead_attacking_minions, dead_attacked_minions = battle.execute_death_phase(dead_attacking_minions, dead_attacked_minions)

		if minion1.health > 0 and minion1.has_windfury:
			minion1.has_windfury = False

		else:
			# ATTACKING minion INDEX:
			battle.attacking_player.attack_index += 1 - dead_attacking_minions
			battle.attacked_player.attack_index -= dead_attacked_minions

			# ATTACKING/ATTACKED INDEX -> 0:
			if battle.attacking_player.attack_index < 0 or battle.attacking_player.attack_index > len(battle.attacking_player.warband) - 1:
				battle.attacking_player.attack_index = 0
			if battle.attacked_player.attack_index < 0 or battle.attacked_player.attack_index > len(battle.attacked_player.warband) - 1:
				battle.attacked_player.attack_index = 0

			battle.round += 1

		statement = f'Warbands after {battle.attacking_player.name}\'s attack:'
		battle.print_state(statement)

	if not battle.attacking_player.warband and not battle.attacked_player.warband:
		print("NO WINNER")
		damage = 0

	else:
		# print()
		winner = battle.attacking_player if battle.attacking_player.warband else battle.attacked_player
		loser = battle.attacking_player if not battle.attacking_player.warband else battle.attacked_player

		print(f'{winner.name} WINNER')
		# print(f'{loser.name} LOSER')
		damage = winner.count_final_damage(winner.warband)
		loser.life -= damage
		# print(f'DAMAGE: {damage}')

	# print(player1.life, "player1 life", player1.name)
	# print(player2.life, "player2 life", player2.name)

	# print(len(player1.warband.warband))
	# print(len(player2.warband.warband))

	return winner


warband1 = [ 
# #1
	# HeraldOfFlame(),
	# GlyphGuardian(),
	# RedWhelp(),
	DeflectoBot(),
	# ImpMama(),
	# FiendishServant(),
	# Imprisoner(), 
	# KaboomBot(),

	# RedWhelp(),
	SecurityRover(),
	DeflectoBot(),
	# SecurityRover(),
	# DeflectoBot(),
	# SavannahHighmane(),

# #2

	# RatPack(),
	# Ghastcoiler(),
	# Maexxna(),



	# RedWhelp(),
	# FloatingWatcher(),
	# AnnihilanBattlemaster(),
	# SoulJuggler(),
	# SoulJuggler(),
#3
	# FoeReaper4000(),
	# HarvestGolem(),
	# Mecharoo(),
	DrakonidEnforcer(),
	DrakonidEnforcer(),
	# SneedsOldShredder(),
	Junkbot(),

	# ZappSlywick(),

	# KingBagurgle(),

#######################################
	# StewardOfTime(),
	# HangryDragon(),
	# TwilightEmissary(),
	# CobaltScalebane(),



	# GentleMegasaur(),

	# MetaltoothLeaper(),
	# Zoobot(),
	# ScrewjankClunker(),


	# CrowdFavorite(),
	# ShifterZerus(),
	# DefenderOfArgus(),
	# VirmenSensei(),
	# LightfangEnforcer(),
	# Crystalweaver(),
	# Houndmaster(),
	# MenagerieMagician(),
	# BrannBronzebeard(),
	# StrongshellScavenger(),

	# FelfinNavigator(),
	# Toxfin(),
	]

warband2 = [
# #1
# 	RighteousProtector(), 
	CaveHydra(),
	# HeraldOfFlame(),

	# SelflessHero(),
 	# UnstableGhoul(),
 
	# KaboomBot(),	
	# KaboomBot(),
	# KaboomBot(),
	# ImpGangBoss(),
	# Imprisoner(),  
	# Voidlord(),

# #2
# 	NadinaTheRed(),
	# RedWhelp(),

	# GoldrinnTheGreatWolf(),

	# IronhideDirehorn(),

#3	
	KindlyGrandmother(),
	RatPack(),
	# IronhideDirehorn(),
	# ScavengingHyena(),


	# MechanoEgg(),
	# PilotedShredder(),
	# ReplicatingMenace(),

	# KangorsApprentice(),

	ScavengingHyena(),
	PackLeader(),	
	MamaBear(),

############################################
	# Murozond(),
	# RazorgoreTheUntamed(),
	# KalecgosArcaneAspect(),


	# MurlocTidecaller(),
	# ColdlightSeer(),
	# RockpoolHunter(),
	# PrimalfinLookout(),


	# Alleycat(),
	# RabidSaurolisk(),


	# MicroMachine(),
	# PogoHopper(),
	# IronSensei(),
	# Junkbot(),
# 

	# WrathWeaver(),
	# NathrezimOverseer(),
	# NathrezimOverseer(),
	# SoulJuggler(),
	# SoulJuggler(),
	]

battle, player1, player2 = start_of_game(warband1, warband2)
combat(battle, player1, player2)