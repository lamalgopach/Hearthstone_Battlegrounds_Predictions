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

def find_special_minions(warband):

	lst_of_specials = [MamaBear, PackLeader]
	specials_dict = {MamaBear:MamaBearChangeStats(), 
					PackLeader:PackLeaderChangeStats(),
					}
	effects = {}

	for minion in warband:
		if type(minion) in lst_of_specials:
			effects[minion] = specials_dict[type(minion)]
	print(effects)
	return effects


def start_of_game(warband1, warband2):

	w1 = copy.deepcopy(warband1)
	w2 = copy.deepcopy(warband2)
	player1 = Player("Alice", warband1, w1)
	player2 = Player("Bob", warband2, w2)
	player1.dead_minions = []
	player2.dead_minions = []

	player1.effects = find_special_minions(w1)
	player2.effects = find_special_minions(w2)

	# THE ORDER OF ATTACK:
	game = choose_first(player1, player2)

	attacking_player = player1 if game[0] == player1.warband else player2
	attacked_player = player2 if game[1] == player2.warband else player1

	attacking_warband = player1.warband if game[0] == player1.warband else player2.warband
	attacked_warband = player2.warband if game[1] == player2.warband else player1.warband

	battle_state = BattleState([attacking_player, attacked_player], 0)
	battle_state.print_state("START OF THE GAME: ")

	return battle_state, player1, player2


def combat(battle_state, player1, player2):
	winner = None
	battle_state.start_of_combat()
	battle_state.print_state("after start of combat:")

	# attack till at least one player has no minions:
	while battle_state.attacking_player.warband and battle_state.attacked_player.warband:
		# choose attacked minion:
		next_phase = False
		attacked_minion = battle_state.choose_attacked_minion()
		battle_state.attacked_player.attacked_minion = attacked_minion

	 	# create minions in game:
		minion1 = battle_state.attacking_player.warband[battle_state.attacking_player.attack_index]
		minion2 = battle_state.attacked_player.warband[attacked_minion]

		# if minion1.has_ds and DrakonidEnforcer or BolivarFireblood in fw:
		# 	DrakonidEnforcer or BolivarFireblood.change_stats()
		# if minion2.has_ds and DrakonidEnforcer or BolivarFireblood in fw:
		# 	DrakonidEnforcer or BolivarFireblood.change_stats()

		# attack phase:
		minion1.attack()
		minion1.take_damage(minion2.attack_value, minion2.poisonous)
		minion2.take_damage(minion1.attack_value, minion1.poisonous)

		
		# summon after damage:
		if minion1.damage_effect and minion2.attack_value > 0:
			minion1.act_after_damage(battle=battle_state, status=1)

		if minion2.damage_effect and minion1.attack_value > 0:
			minion2.act_after_damage(battle=battle_state, status=2)

		if minion1.has_triggered_attack and len(battle_state.attacked_player.warband) > 1:
			minion1.triggered_attack(battle=battle_state)
			next_phase = True

		print("								Attacking: ", battle_state.attacking_player.name)
		print("								", minion1.name, minion1.attack_value, minion1.health)
		print("								Attacked: ", battle_state.attacked_player.name)
		print("								", minion2.name, minion2.attack_value, minion2.health)
		print()
		# count dead minions:
		dead_attacking_minions = 0
		dead_attacked_minions = 0

		if minion1.health < 1 and minion2.health < 1:
			next_phase, dead_attacking_minions, dead_attacked_minions = battle_state.both_minions_die(next_phase=next_phase, d_ag_ms=dead_attacking_minions, d_ad_ms=dead_attacked_minions)

		elif minion1.health < 1 or minion2.health < 1:
			if minion1.health < 1:
				status = 1
				minion = minion1
				dead_minions = dead_attacking_minions
			elif minion2.health < 1:
				status = 2
				minion = minion2
				dead_minions = dead_attacked_minions
			next_phase, dead_minions = battle_state.one_minion_dies(next_phase=next_phase, minion=minion, status=status, dead_minions=dead_minions)
			if status == 1:
				dead_attacking_minions = dead_minions
			elif status == 2:
				dead_attacking_minions = dead_minions

			#minion1, minion2 
			# if minion2.m_type = MinionType.BEAST and ScavengingHyena in friendly_warband:
			# 	ScavengingHyena.change_stats()

			# elif minion2.m_type = MinionType.MECH and Junkbot in friendly_warband:
			# 	Junkbot.change_stats()

			# elif minion2.m_type = MinionType.DEMON and SoulJuggler in friendly_warband:
			# 	SoulJuggler attacks random minion

			# if minion1.m_type == MinionType.DRAGON and WaxxTogwagler in friendly warband:
			# 	WaxxTogwagler.change_stats()


		# next DEATHRATTLES:
		if next_phase:
			dead_attacking_minions, dead_attacked_minions = battle_state.solve_next_phase(next_phase, dead_attacking_minions, dead_attacked_minions)
		
		if minion1.health > 0 and minion1.has_windfury:
			minion1.has_windfury = False
		else:
			# ATTACKING INDEX:
			battle_state.attacking_player.attack_index += 1 - dead_attacking_minions

			# ATTACKING INDEX -> 0:
			if battle_state.attacking_player.attack_index > len(battle_state.attacking_player.warband) - 1:
				battle_state.attacking_player.attack_index = 0
			elif battle_state.attacking_player.attack_index < 0:
				battle_state.attacking_player.attack_index = 0

			# ATTACKED INDEX:
			if dead_attacked_minions > 0:
				battle_state.attacked_player.attack_index -= dead_attacked_minions

			# ATTACKED INDEX -> 0:
			if battle_state.attacked_player.attack_index > len(battle_state.attacked_player.warband) - 1:
				battle_state.attacked_player.attack_index = 0
			elif battle_state.attacked_player.attack_index < 0:
				battle_state.attacked_player.attack_index = 0

			battle_state.round += 1


# def play_round(battle_state):
# 	...
# 	battle_state.round += 1

# def combat(battle_state):
# 	while not any(p.dead for p in battle_state.players):
# 		play_round(battle_state)

		statement = f'Warbands after {battle_state.attacking_player.name}\'s attack:'
		battle_state.print_state(statement)


	if not battle_state.attacking_player.warband and not battle_state.attacked_player.warband:
		print("NO WINNER")
		damage = 0

	else:
		# print()
		winner = battle_state.attacking_player if battle_state.attacking_player.warband else battle_state.attacked_player
		loser = battle_state.attacking_player if not battle_state.attacking_player.warband else battle_state.attacked_player

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
# 	GlyphGuardian(),
# 	RedWhelp(),
# 	HeraldOfFlame(),

# 	ImpMama(),
# 	FiendishServant(),

	TheBeast(),
	SavannahHighmane(),


# #2
	Ghastcoiler(),
	InfestedWolf(),
# 	Maexxna(),
	MamaBear(),

# 	SecurityRover(),
# 	KaboomBot(),


#3
	# FoeReaper4000(),
	# HarvestGolem(),
	# Mecharoo(),
	# SneedsOldShredder(),

	# ZappSlywick(),

	# KingBagurgle(),
	PackLeader(),

#######################################
	# StewardOfTime(),
	# HangryDragon(),
	# TwilightEmissary(),
	# CobaltScalebane(),


	# FloatingWatcher(),
	# AnnihilanBattlemaster(),


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
# 	SpawnOfnZoth(),
# 	SelflessHero(),
# 	UnstableGhoul(), 

# 	ImpGangBoss(),
# 	Imprisoner(),  
# 	Voidlord(),


# #2
# 	NadinaTheRed(),
# 	DragonspawnLieutenant(),
# 	RedWhelp(),
# 	HeraldOfFlame(),

	GoldrinnTheGreatWolf(),
	CaveHydra(),


#3	
	KindlyGrandmother(),
	RatPack(),
	IronhideDirehorn(),

	# MechanoEgg(),
	# PilotedShredder(),
	# ReplicatingMenace(),
	# KangorsApprentice(),
	MamaBear(),
	PackLeader(),



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


	# WrathWeaver(),
	# NathrezimOverseer(),
	]

battle_state, player1, player2 = start_of_game(warband1, warband2)
combat(battle_state, player1, player2)