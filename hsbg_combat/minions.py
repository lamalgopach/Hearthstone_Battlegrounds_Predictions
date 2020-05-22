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
		has_ds=False, has_deathrattle=False):
		self.name = name
		self.attack_value = attack_value
		self.health = health
		self.tier = tier
		self.m_type = m_type
		self.taunt = taunt
		self.has_ds = has_ds
		self.has_deathrattle = has_deathrattle

	def attack(self):
		# used in Glyph Guardian
		return

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


	def summon_minions(self, n, minion_class):
		# n - number of summoned minions
		# just one type of minion
		summoned_minions = []
		for i in range(n):
			minion = minion_class()
			summoned_minions.append(minion)
		return summoned_minions


class DragonspawnLieutenant(Card):
	def __init__(self):
		super().__init__(name="Dragonspawn Lieutenant", attack_value=2, health=3, tier=1, 
			m_type=MinionType.DRAGON, taunt=True)


class GlyphGuardian(Card):
	def __init__(self):
		super().__init__(name="Glyph Guardian", attack_value=2, health=4, tier=2, 
			m_type=MinionType.DRAGON)

	def attack(self):
		self.attack_value = 2 * self.attack_value


class InfestedWolf(Card):
	def __init__(self):
		super().__init__(name="Infested Wolf", attack_value=3, health=3, tier=3, 
			m_type=MinionType.BEAST, has_deathrattle=True)

	def deathrattle(self, friendly_minions, enemy_minions, j):
		spiders_lst = self.summon_minions(2, Spider)
		i = 0
		while len(friendly_minions) < 7 and i != 2:
			spider = spiders_lst[i]
			friendly_minions.insert(j, spider)
			i += 1

class KaboomBot(Card):
	def __init__(self):
		super().__init__(name="Kaboom Bot", attack_value=2, health=2, tier=2, 
			m_type=MinionType.MECH, has_deathrattle=True)

	def deathrattle(self, friendly_minions, enemy_minions, j):
		if enemy_minions:
			enemy_random_minion = random.choice(enemy_minions)
			i = enemy_minions.index(enemy_random_minion)
			enemy_random_minion.take_damage(4)

# class MurlocWarleader(Card):
# 	def __init__(self):
# 		super().__init__(name="Murloc Warleader", attack_value=3, health=3, tier=2, 
# 			m_type=MinionType.MURLOC)


class Mecharoo(Card):
	def __init__(self):
		super().__init__(name="Mecharoo", attack_value=1, health=1, tier=1, 
			m_type=MinionType.MECH, has_deathrattle=True)

	def deathrattle(self, friendly_minions, enemy_minions, j):
		joebot = self.summon_minions(1, JoEBot)
		friendly_minions.insert(j, joebot[0])



class RedWhelp(Card):
	def __init__(self):
		super().__init__(name="Red Whelp", attack_value=1, health=2, tier=1, 
			m_type=MinionType.DRAGON)

	def add_damage_in_combat(self, minions):
		damage = 0
		for minion in minions:
			if minion.m_type == MinionType.DRAGON:
				damage += 1
		return damage

	def attack_in_start_of_combat(self, friendly_minions, enemy_minions):
		damage = self.add_damage_in_combat(friendly_minions.warband)
		attacked_minion = random.choice(enemy_minions.warband)
		j = enemy_minions.warband.index(attacked_minion)
		attacked_minion.take_damage(damage)
		if attacked_minion.health < 1:
			attacked_minion.die(enemy_minions.warband, j)
			if attacked_minion.has_deathrattle:
				attacked_minion.deathrattle(enemy_minions.warband, friendly_minions.warband, j)


class RatPack(Card):
	def __init__(self):
		super().__init__(name="Rat Pack", attack_value=2, health=2, tier=2, 
						m_type=MinionType.BEAST, has_deathrattle=True)

	def deathrattle(self, friendly_minions, enemy_minions, j):
		x = self.attack_value
		rats = self.summon_minions(x, Rat)
		i = 0
		while len(friendly_minions) < 7 and i != x:
			rat = rats[i]
			friendly_minions.insert(j, rat)
			i += 1


class RighteousProtector(Card):
	def __init__(self):
		super().__init__(name="Righteous Protector", attack_value=1, health=1, tier=1, 
						m_type=MinionType.MINION, taunt=True, has_ds =True)


class RockpoolHunter(Card):
	def __init__(self):
		super().__init__(name="Rockpool Hunter", attack_value=2, health=3, tier=1, 
						m_type=MinionType.MURLOC)


class SelflessHero(Card):
	def __init__(self):
		super().__init__(name="Selfless Hero", attack_value=2, health=1, tier=1, 
						m_type=MinionType.MINION, has_deathrattle=True)

	def deathrattle(self, friendly_minions, enemy_minions, j):	
		if not friendly_minions:
			return

		minions_no_ds = [minion for minion in friendly_minions if not minion.has_ds]
		
		if not minions_no_ds:
			return

		minion = random.choice(minions_no_ds)
		minion.has_ds = True


class SpawnOfnZoth(Card):
	def __init__(self):
		super().__init__(name="Spawn Of n'Zoth", attack_value=2, health=2, tier=2, 
						m_type=MinionType.MINION, has_deathrattle=True)
	
	def deathrattle(self, friendly_minions, enemy_minions, j):
		if friendly_minions:
			for minion in friendly_minions:
				minion.attack_value += 1
				minion.health += 1


# class(es) not imported to create minions in warbands:
class Spider(Card):
	def __init__(self):
		super().__init__(name="Spider", attack_value=1, health=1, tier=1, 
			m_type=MinionType.BEAST)

class Rat(Card):
	def __init__(self):
		super().__init__(name="Rat", attack_value=1, health=1, tier=1, 
			m_type=MinionType.BEAST)

class JoEBot(Card):
	def __init__(self):
		super().__init__(name="Jo-E Bot", attack_value=1, health=1, tier=1, 
			m_type=MinionType.MECH)


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
# think like effects(unstableghoul)
# classes to do first: waxoggler