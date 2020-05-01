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
		has_deathrattle, start_of_combat):
		self.name = name
		self.attack = attack
		self.health = health
		self.tier = tier
		self.m_type = m_type
		self.is_taunted = is_taunted
		self.has_ds = has_ds
		self.has_deathrattle = has_deathrattle
		self.start_of_combat = start_of_combat


	def take_damage(self, damage):
		if damage == 0:
			return

		if self.has_ds:
			self.has_ds = False
		else:
			self.health -= damage

	def remove_ds(self):
		self.has_ds = False


class SelflessHero(Card):

	def deathrattle(self, friendly_minions):
		if not friendly_minions:
			return

		minion = random.choice(friendly_minions)
		minion.has_ds = True
		return minion

class SpawnOfnZoth(Card):

	def deathrattle(self, friendly_minions):
		if friendly_minions:
			for minion in friendly_minions:
				minion.attack += 1
				minion.health += 1
		return friendly_minions	

class InfestedWolf(Card):

	def deathrattle(self, friendly_minions):
		spider = Card("Spider", 1, 1, 1, 3, False, False, False, False)
		friendly_minions.append(spider)

		if len(friendly_minions) < 6:
			spider_2 = copy.copy(spider)
			friendly_minions.append(spider_2)

		return friendly_minions

class GlyphGuardian(Card):

	def add_attack(self):
		self.attack = 2 * self.attack


class RedWhelp(Card):

	def add_damage(self, minions):
		damage = 1

		for minion in minions:
			if minion.m_type == 2:
				damage += 1
		self.attack += damage


	def take_no_damage(self):
		self.has_ds = True

	# def reduce_attack(self, start_attack):

	# 	self.attack = start_attack



			



# minions completed:

dragonspawn_lieutenant = Card("Dragonspawn Lieutenant", 2, 3, 1, 2, True, False, False, False)
righteous_protector = Card("Righteous Protector", 1, 1, 1, 0, True, True, False, False)
spawn_of_nzoth = SpawnOfnZoth("Spawn Of n'Zoth", 2, 2, 2, 0, False, False, True, False)
infested_wolf = InfestedWolf("Infested Wolf", 3, 3, 3, 3, False, False, True, False)
selfless_hero = SelflessHero("Selfless Hero", 2, 1, 1, 0, False, False, True, False)
glyph_guardian = GlyphGuardian("Glyph Guardian", 2, 4, 2, 2, False, False, False, True)

# classes written:
murloc_warleader = Card("Murloc Warleader", 3, 3, 2, 1, False, False, False, False)
red_whelp = RedWhelp("Red Whelp", 1, 2, 1, 2, False, False, False, False)


# battlecry:
rockpool_hunter = Card("Rockpool Hunter", 2, 3, 1, 1, False, False, False, False)

minions_lst = [dragonspawn_lieutenant, righteous_protector, murloc_warleader,
			glyph_guardian, red_whelp, spawn_of_nzoth, infested_wolf, selfless_hero, 
			rockpool_hunter]











# class Event:
# 	def __init__(self, evnt):
# 		self.evnt = evnt



#CHECKCHEKCCHECKCHEKCHCKLECHEKCHEKCHEKCHEKCHECK


# class AddingAttack(Event):
# 	# murloc_warleader

# 	is_alive = True
# 	is_attack_added = False

# 	def __init__(self, is_alive, additional_attack, objects_to_whom):
		
# 		for i in self.objects_to_whom:
# 			i.attack += additional_attack

# 		is_attack_added = True

# class DoublingAttack(Event):
# 	# glyph guardian

# 	is_attacking = True

# 	def __init__(self, attack):
# 		self.attack = 2*attack



# class StartOfCombat(Event):
# 	# red whelp
# 	is_attacking = True

# 	def __init__(self, warband):
# 		damage = sum(1 for i in self.warband if i.m_type == 2)




