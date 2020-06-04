from random import choice

from beasts import *
from demons import *
from dragons import *
from minions import *
from mechs import *
from murlocs import *



class Ghastcoiler(Card):
	#unhash
	def __init__(self):
		super().__init__(name="Ghastcoiler", attack_value=7, health=7, 
						tier=6, m_type=MinionType.BEAST, has_deathrattle=True)
	
	def deathrattle(self, battle, friendly_minions, enemy_minions, j):
		deathrattle_minions = [
			SelflessHero, 
			Mecharoo,
			FiendishServant,
			SpawnOfnZoth,
			KindlyGrandmother,
			RatPack,
			# HarvestGolem,
			# KaboomBot,
			Imprisoner,
			UnstableGhoul,
			InfestedWolf,
			TheBeast,
			# PilotedShredder,
			# ReplicatingMenace,
			# MechanoEgg,
			GoldrinnTheGreatWolf,
			SavannahHighmane,
			Voidlord,
			KingBagurgle,
			# SneedsOldShredder,
			KangorsApprentice,
			NadinaTheRed,
			]

		i = 0
		while len(friendly_minions.warband) < 7 and i != 2:
			random_deathrattle_minion_type = random.choice(deathrattle_minions)
			random_deathrattle_minion = self.summon_minion(random_deathrattle_minion_type)
			friendly_minions.warband.insert(j, random_deathrattle_minion)
			i += 1


class PilotedShredder(Card):
	#unhash summoned minions
	def __init__(self):
		super().__init__(name="Piloted Shredder", attack_value=4, health=3, tier=3, 
						m_type=MinionType.MECH, has_deathrattle=True)

	def deathrattle(self, battle, friendly_minions, enemy_minions, j):
		two_cost_minions = [
			VulgarHomunculus,
			MicroMachine,
			MurlocTidehunter,
			RockpoolHunter,
			DragonspawnLieutenant,
			KindlyGrandmother,
			# ScavengingHyena,
			UnstableGhoul,
			# Khadgar,	
			]

		random_2cost_minion_type = random.choice(two_cost_minions)
		random_2cost_minion = self.summon_minion(random_2cost_minion_type)
		friendly_minions.warband.insert(j, random_2cost_minion)	


class SneedsOldShredder(Card):
	def __init__(self):
		super().__init__(name="Sneed's Old Shredder", attack_value=5, health=7, tier=5, 
						m_type=MinionType.MECH, has_deathrattle=True)

	def deathrattle(self, battle, friendly_minions, enemy_minions, j):
		legendary_minions = [
			# OldMurkEye,
			# Khadgar,
			ShifterZerus,
			# BolvarFireblood,
			# BaronRivendare,
			BrannBronzebeard,
			# Malganis,
			Maexxna,
			GoldrinnTheGreatWolf,
			TheBeast,
			KingBagurgle,
			FoeReaper4000,
			]

		random_legendary_minion_type = random.choice(legendary_minions)
		random_legendary_minion = self.summon_minion(random_legendary_minion_type)
		friendly_minions.warband.insert(j, random_legendary_minion)