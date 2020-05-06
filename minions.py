import random
import copy
from random import choice
from enum import Enum

class Player:

	def __init__(self, name, warband):
		self.name = name
		self.warband = warband

class MinionType(Enum):
	PLAIN = 0
	MURLOC = 1
	DRAGON = 2
	BEAST = 3
	MECH = 4
	DEMON = 5

class Card:

	def __init__(self, *, name, attack_value, health, tier, m_type, is_taunted=False, 
		has_ds=False, has_deathrattle=False):
		self.name = name
		self.attack_value = attack_value
		self.health = health
		self.tier = tier
		self.m_type = m_type
		self.is_taunted = is_taunted
		self.has_ds = has_ds
		self.has_deathrattle = has_deathrattle


	# deathrattle = None


	def take_damage(self, damage):
		if damage == 0:
			return

		if self.has_ds:
			self.has_ds = False
		else:
			self.health -= damage

	def remove_ds(self):
		self.has_ds = False

	def die(self, friendly_minions, j):
		del friendly_minions[j]
		if self.has_deathrattle:
			self.deathrattle(friendly_minions, j)
		return friendly_minions


class DragonspawnLieutenant(Card):
	def __init__(self):
		super().__init__(name="Dragonspawn Lieutenant", attack_value=2, health=3, tier=1, m_type=2, 
			is_taunted=True)


class GlyphGuardian(Card):
	def __init__(self):
		super().__init__(name="Glyph Guardian", attack_value=2, health=4, tier=2, m_type=2)
	def add_attack(self):
		#change it
		self.attack_value = 2 * self.attack_value


class InfestedWolf(Card):
	def __init__(self):
		super().__init__(name="Infested Wolf", attack_value=3, health=3, tier=3, m_type=3, 
			has_deathrattle=True)
	def deathrattle(self, friendly_minions, j):
		spider = Spider()
		#are you sure?
		friendly_minions.insert(j, spider)

		if len(friendly_minions) < 6:
			spider_2 = copy.copy(spider)
			friendly_minions.insert(j + 1, spider)

		return friendly_minions

class MurlocWarleader(Card):
	def __init__(self):
		super().__init__(name="Murloc Warleader", attack_value=3, health=3, tier=2, m_type=1)



class RedWhelp(Card):
	def __init__(self):
		super().__init__(name="Red Whelp", attack_value=1, health=2, tier=1, m_type=2)
	def take_no_damage(self):
		self.has_ds = True
	def add_damage(self, minions):
		damage = 0

		for minion in minions:
			if minion.m_type == 2:
				damage += 1
		self.attack_value = damage
		# self.take_no_damage()
		self.has_ds = True



class RighteousProtector(Card):
	def __init__(self):
		super().__init__(name="Righteous Protector", attack_value=1, health=1, tier=1, m_type=0,
			is_taunted=True, has_ds =True)


class RockpoolHunter(Card):
	def __init__(self):
		super().__init__(name="Rockpool Hunter", attack_value=2, health=3, tier=1, m_type=1)


class SelflessHero(Card):
	def __init__(self):
		super().__init__(name="Selfless Hero", attack_value=2, health=1, tier=1, m_type=0, 
			has_deathrattle=True)
	def deathrattle(self, friendly_minions, j):
		if not friendly_minions:
			return

		minion = random.choice(friendly_minions)
		minion.has_ds = True
		return minion

class SpawnOfnZoth(Card):
	def __init__(self):
		super().__init__(name="Spawn Of n'Zoth", attack_value=2, health=2, tier=2, m_type=2, 
			has_deathrattle=True)
	def deathrattle(self, friendly_minions, j):
		if friendly_minions:
			for minion in friendly_minions:
				minion.attack_value += 1
				minion.health += 1
		return friendly_minions	


# class not imported to creating minions in warbands:

class Spider(Card):
	def __init__(self):
		super().__init__(name="Spider", attack_value=1, health=1, tier=1, m_type=3)

# Jakub:
# minion = SpawnOfnZoth()
# if minion.deathrattle is not None:
# # if hasattr(minion, "deathrattle"):
# 	minion.deathrattle(friendly_minions, j)


# Jakub
# class Minion:
# 	def __init__(self, *, attack_value):
# 		self.attack_value = attack_value

# 	def attack(self, game_state, target):
# 		target.health -= self.attack_value
# 		self.health -= target.attack_value
# 		return game_state

# class GlyphGuardian(Minion):
# 	def attack(*args, **kwargs):
# 		self.attack_value *= 2
# 		super().attack(*args, **kwargs)





#todo:
# redwhelp: random player order)
# glyph_guardian: change add attack


# minions_lst = [dragonspawn_lieutenant, righteous_protector, murloc_warleader,
# 			glyph_guardian, red_whelp, spawn_of_nzoth, infested_wolf, selfless_hero, 
# 			rockpool_hunter]



# ?
# class Event:
# 	def __init__(self, evnt):
# 		self.evnt = evnt




