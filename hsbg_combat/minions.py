import random
import copy
from random import choice
from enum import Enum




class MinionType(Enum):
	MINION = 0
	MURLOC = 1
	DRAGON = 2
	BEAST = 3
	MECH = 4
	DEMON = 5


class Card:
	def __init__(self, *, name, attack_value, health, tier, m_type, taunt=False, 
		has_ds=False, has_deathrattle=False, has_triggered_attack=False, 
		has_overkill=False, poisonous=False, damage_effect=False):

		self.name = name
		self.attack_value = attack_value
		self.health = health
		self.tier = tier
		self.m_type = m_type
		self.taunt = taunt
		self.has_ds = has_ds
		self.has_deathrattle = has_deathrattle
		self.has_triggered_attack = has_triggered_attack
		self.has_overkill = has_overkill
		self.poisonous = poisonous
		self.damage_effect = damage_effect

	def attack(self):
		# used in Glyph Guardian

		return

	def take_poison(self):
		
		if self.has_ds:
			self.has_ds = False

		else:
			self.health = 0

	def take_damage(self, damage, poisonous):
		if damage == 0:
			return

		if self.has_ds:
			self.has_ds = False
		elif poisonous:
			self.health = 0
		else:
			self.health -= damage
		# if self.has_ds:
		# 	self.has_ds = False
		# else:
		# 	self.health -= damage

	def die(self, friendly_minions, j, dead_warband):
		del friendly_minions[j]
		dead_warband.append(self)

	def triggered_attack(self, enemy_minions, j):
		if j != 0 and j + 1 < len(enemy_minions):
			a = j - 1
			b = j + 1	
			enemy_minions[b].take_damage(self.attack_value, self.poisonous)
		elif j == 0 and j + 1 <= len(enemy_minions):
			a = j + 1
		elif j == len(enemy_minions) - 1:
			a = j - 1
		enemy_minions[a].take_damage(self.attack_value, self.poisonous)

	def summon_minion(self, minion_class):
		minion = minion_class()
		return minion


class BrannBronzebeard(Card):
# add effect
	def __init__(self):
		super().__init__(name="Brann Bronzebeard", attack_value=2, health=4, tier=5, 
						m_type=MinionType.MINION)



class CrowdFavorite(Card):
	# add special function later
	def __init__(self):
		super().__init__(name="Crowd Favorite", attack_value=4, health=4, tier=3, 
						m_type=MinionType.MINION)


class Crystalweaver(Card):
	#btlcry
	def __init__(self):
		super().__init__(name="Crystalweaver", attack_value=5, health=4, tier=3, 
						m_type=MinionType.MINION)


class DefenderOfArgus(Card):
	#btlcry
	def __init__(self):
		super().__init__(name="Defender of Argus", attack_value=2, health=3, tier=4, 
						m_type=MinionType.MINION)



class Houndmaster(Card):
	#btlcry
	def __init__(self):
		super().__init__(name="Houndmaster", attack_value=4, health=3, tier=3, 
						m_type=MinionType.MINION)


class KangorsApprentice(Card):
	def __init__(self):
		super().__init__(name="Kangor's Apprentice", attack_value=3, health=6, tier=6, 
						m_type=MinionType.MINION, has_deathrattle=True)

	def deathrattle(self, battle, friendly_minions, enemy_minions, j):
		warband = []

		if friendly_minions == battle.attacking_warband:
			warband = battle.dead_attacking_minions
		else:
			warband = battle.dead_attacked_minions

		mechs_to_summon = []

		for minion in warband:
			if minion.m_type == MinionType.MECH:
				mechs_to_summon.append(minion)
		
		if mechs_to_summon:
			mechs = []
			i = 0
			for mech in mechs_to_summon:
				if len(friendly_minions.warband) < 7 and i < 2:
					summoned_mech = self.summon_minion(type(mech))

					# summoned_mech.attack_value = mech.attack_value
					# summoned_mech.health = mech.health
					# summoned_mech.taunt = mech.taunt
					# summoned_mech.has_ds = mech.has_ds
					# summoned_mech.has_deathrattle = mech.has_deathrattle
					# summoned_mech.has_triggered_attack = mech.has_triggered_attack
					# summoned_mech.damage_effect = mech.damage_effect

					friendly_minions.warband.insert(j + i, summoned_mech)
					i += 1
				else:
					break




class KingBagurgle(Card):
	# add the battlecry later
	def __init__(self):
		super().__init__(name="King Bagurgle", attack_value=6, health=3, tier=5, 
						m_type=MinionType.MURLOC, has_deathrattle=True)
	
	def deathrattle(self, battle, friendly_minions, enemy_minions, j):
		if friendly_minions.warband:
			for minion in friendly_minions.warband:
				if minion.m_type == MinionType.MURLOC:
					minion.attack_value += 2
					minion.health += 2

class LightfangEnforcer(Card):
	# effect
	def __init__(self):
		super().__init__(name="Lightfang Enforcer", attack_value=2, health=2, tier=5, 
						m_type=MinionType.MINION)

class MenagerieMagician(Card):
	#btlcry
	def __init__(self):
		super().__init__(name="Menagerie Magician", attack_value=4, health=4, tier=4, 
						m_type=MinionType.MINION)


class NadinaTheRed(Card):
	def __init__(self):
		super().__init__(name="Nadina The Red", attack_value=7, health=4, tier=6, 
						m_type=MinionType.MINION, has_deathrattle=True)
	
	def deathrattle(self, battle, friendly_minions, enemy_minions, j):
		if friendly_minions.warband:
			for minion in friendly_minions.warband:
				if minion.m_type == MinionType.DRAGON:
					minion.has_ds = True


class RighteousProtector(Card):
	def __init__(self):
		super().__init__(name="Righteous Protector", attack_value=1, health=1, tier=1, 
						m_type=MinionType.MINION, taunt=True, has_ds =True)


class SelflessHero(Card):
	def __init__(self):
		super().__init__(name="Selfless Hero", attack_value=2, health=1, tier=1, 
						m_type=MinionType.MINION, has_deathrattle=True)

	def deathrattle(self, battle, friendly_minions, enemy_minions, j):	
		if not friendly_minions.warband:
			return

		minions_no_ds = [minion for minion in friendly_minions.warband if not minion.has_ds]
		
		if not minions_no_ds:
			return

		minion = random.choice(minions_no_ds)
		minion.has_ds = True


class ShifterZerus(Card):
	# add effect
	def __init__(self):
		super().__init__(name="Shifter Zerus", attack_value=1, health=1, tier=3, 
						m_type=MinionType.MINION)


class SpawnOfnZoth(Card):
	def __init__(self):
		super().__init__(name="Spawn Of n'Zoth", attack_value=2, health=2, tier=2, 
						m_type=MinionType.MINION, has_deathrattle=True)
	
	def deathrattle(self, battle, friendly_minions, enemy_minions, j):
		if friendly_minions.warband:
			for minion in friendly_minions.warband:
				minion.attack_value += 1
				minion.health += 1


class StrongshellScavenger(Card):
	# btlcry
	def __init__(self):
		super().__init__(name="Strongshell Scavenger", attack_value=2, health=3, tier=5,
						m_type=MinionType.MINION)


class UnstableGhoul(Card):
	def __init__(self):
		super().__init__(name="Unstable Ghoul", attack_value=1, health=3, tier=2, 
						m_type=MinionType.MINION, has_deathrattle=True)
	
	def deathrattle(self, battle, friendly_minions, enemy_minions, j):
		if friendly_minions.warband:
			for minion in friendly_minions.warband:
				minion.take_damage(1, self.poisonous)

		if enemy_minions.warband:
			for minion in enemy_minions.warband:
				minion.take_damage(1, self.poisonous)


class VirmenSensei(Card):
	#btlcry
	def __init__(self):
		super().__init__(name="Virmen Sensei", attack_value=4, health=5, tier=4, 
						m_type=MinionType.MINION)

class WrathWeaver(Card):
	#btlcry damage
	def __init__(self):
		super().__init__(name="Wrath Weaver", attack_value=1, health=1, tier=1, 
						m_type=MinionType.MINION)

# class(es) not imported to create minions in warbands
class FinkleEinhorn(Card):
	def __init__(self):
		super().__init__(name="Finkle Einhorn", attack_value=3, health=3, tier=1, 
						m_type=MinionType.MINION)


# Jakub:
# minion = SpawnOfnZoth()
# if minion.deathrattle is not None:
# # if hasattr(minion, "deathrattle"):
# 	minion.deathrattle(friendly_minions, j)

# 	def attack(self, game_state, target):
# 		target.health -= self.attack_value
# 		self.health -= target.attack_value
# 		return game_state

# class GlyphGuardian(Minion):
# 	def attack(*args, **kwargs):
# 		self.attack_value *= 2
# 		super().attack(*args, **kwargs)


#todo:
# classes to do: waxtoggler