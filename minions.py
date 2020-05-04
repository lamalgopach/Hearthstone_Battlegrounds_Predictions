import random
import copy
from random import choice
from enum import Enum

class Player:

	def __init__(self, name, warband):
		self.name = name
		self.warband = warband
		# type of warband -> list

class MinionType(Enum):

	PLAIN = 0
	MURLOC = 1
	DRAGON = 2
	BEAST = 3
	MECH = 4
	DEMON = 5

class Card:

	def __init__(self, name, attack, health, tier, m_type, is_taunted, has_ds, 
		has_deathrattle):
		self.name = name
		self.attack = attack
		self.health = health
		self.tier = tier
		self.m_type = m_type
		self.is_taunted = is_taunted
		self.has_ds = has_ds
		self.has_deathrattle = has_deathrattle


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


class SelflessHero(Card):

	def deathrattle(self, friendly_minions, j):
		if not friendly_minions:
			return

		minion = random.choice(friendly_minions)
		minion.has_ds = True
		return minion

class SpawnOfnZoth(Card):

	def deathrattle(self, friendly_minions, j):
		if friendly_minions:
			for minion in friendly_minions:
				minion.attack += 1
				minion.health += 1
		return friendly_minions	

class InfestedWolf(Card):

	def deathrattle(self, friendly_minions, j):
		spider = Card("Spider", 1, 1, 1, 3, False, False, False)
		friendly_minions.insert(j, spider)

		if len(friendly_minions) < 6:
			spider_2 = copy.copy(spider)
			friendly_minions.insert(j + 1, spider)

		return friendly_minions

class GlyphGuardian(Card):

	def add_attack(self):
		self.attack = 2 * self.attack


class RedWhelp(Card):

	def add_damage(self, minions):
		damage = 0

		for minion in minions:
			if minion.m_type == 2:
				damage += 1
		self.attack = damage

	def take_no_damage(self):
		self.has_ds = True


# minions completed:
dragonspawn_lieutenant = Card("Dragonspawn Lieutenant", 2, 3, 1, 2, True, False, False)
righteous_protector = Card("Righteous Protector", 1, 1, 1, 0, True, True, False)
spawn_of_nzoth = SpawnOfnZoth("Spawn Of n'Zoth", 2, 2, 2, 0, False, False, True)
selfless_hero = SelflessHero("Selfless Hero", 2, 1, 1, 0, False, False, True)
glyph_guardian = GlyphGuardian("Glyph Guardian", 2, 4, 2, 2, False, False, False)
infested_wolf = InfestedWolf("Infested Wolf", 3, 3, 3, 3, False, False, True)

# done but need to be finished (random player order)
red_whelp = RedWhelp("Red Whelp", 1, 2, 1, 2, False, False, False)

# to do:
murloc_warleader = Card("Murloc Warleader", 3, 3, 2, 1, False, False, False)

# battlecry:
rockpool_hunter = Card("Rockpool Hunter", 2, 3, 1, 1, False, False, False)

minions_lst = [dragonspawn_lieutenant, righteous_protector, murloc_warleader,
			glyph_guardian, red_whelp, spawn_of_nzoth, infested_wolf, selfless_hero, 
			rockpool_hunter]



# ?
# class Event:
# 	def __init__(self, evnt):
# 		self.evnt = evnt




