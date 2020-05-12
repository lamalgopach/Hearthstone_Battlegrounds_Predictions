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
	# deathrattle = None

	def attack(self):
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

	# def die(self, friendly_minions, j, player):
	def die(self, friendly_minions, j):
		del friendly_minions[j]
		if self.has_deathrattle:
			# self.deathrattle(friendly_minions, j, player)
			self.deathrattle(friendly_minions, j)
		return friendly_minions



class DragonspawnLieutenant(Card):
	def __init__(self):
		super().__init__(name="Dragonspawn Lieutenant", attack_value=2, health=3, tier=1, 
			m_type=MinionType.DRAGON, taunt=True)


class GlyphGuardian(Card):
	def __init__(self):
		super().__init__(name="Glyph Guardian", attack_value=2, health=4, tier=2, 
			m_type=MinionType.DRAGON)
	def attack(self):
		#change it
		self.attack_value = 2 * self.attack_value



class InfestedWolf(Card):
	def __init__(self):
		super().__init__(name="Infested Wolf", attack_value=3, health=3, tier=3, 
			m_type=MinionType.MINION, has_deathrattle=True)

	# def deathrattle(self, friendly_minions, j, player):
	def deathrattle(self, friendly_minions, j):
		spider = Spider()
		# are you sure?
		# spider.summon_minion(Spider())
		friendly_minions.insert(j, spider)

		if len(friendly_minions) < 7:
			spider_2 = Spider()
			# spider_2.summon(Spider())
			# summon minion method in Player class
			friendly_minions.insert(j + 1, spider_2)


		# next:
		# player.summon_minion(Spider())


		return friendly_minions

class MurlocWarleader(Card):
	def __init__(self):
		super().__init__(name="Murloc Warleader", attack_value=3, health=3, tier=2, 
			m_type=MinionType.MURLOC)



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

	def start_of_combat(self, friendly_minions, game, i):

		damage = self.add_damage_in_combat(friendly_minions)
		attacked_minion = random.choice(game[i])
		attacked_minion.take_damage(damage)
		
		if attacked_minion.health < 1:
			j = game[i].index(attacked_minion)
			attacked_minion.die(game[i], j)
			print(attacked_minion)

		return game


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
	# def deathrattle(self, friendly_minions, j, player):
	def deathrattle(self, friendly_minions, j):		
		if not friendly_minions:
			return

		minion = random.choice(friendly_minions)
		minion.has_ds = True
		return minion

class SpawnOfnZoth(Card):
	def __init__(self):
		super().__init__(name="Spawn Of n'Zoth", attack_value=2, health=2, tier=2, 
						m_type=MinionType.MINION, has_deathrattle=True)
	# def deathrattle(self, friendly_minions, j, player):
	def deathrattle(self, friendly_minions, j):
		if friendly_minions:
			for minion in friendly_minions:
				minion.attack_value += 1
				minion.health += 1
		return friendly_minions	


# class not imported to create minions in warbands:
class Spider(Card):
	def __init__(self):
		super().__init__(name="Spider", attack_value=1, health=1, tier=1, 
			m_type=MinionType.BEAST)

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
# redwhelp: random player order, add pre combat, overcomplicated, 
# think like effects(kabumbot, unstableghoul)
# selfless hero: only minions without DS
