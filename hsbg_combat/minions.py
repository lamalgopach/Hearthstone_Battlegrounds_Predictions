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


class CaveHydra(Card):
	def __init__(self):
		super().__init__(name="Cave Hydra", attack_value=2, health=4, tier=4, 
						has_triggered_attack=True, m_type=MinionType.BEAST)


class DragonspawnLieutenant(Card):
	def __init__(self):
		super().__init__(name="Dragonspawn Lieutenant", attack_value=2, health=3, 
						tier=1, m_type=MinionType.DRAGON, taunt=True)


class GlyphGuardian(Card):
	def __init__(self):
		super().__init__(name="Glyph Guardian", attack_value=2, health=4, tier=2, 
						m_type=MinionType.DRAGON)

	def attack(self):
		self.attack_value = 2 * self.attack_value


class GoldrinnTheGreatWolf(Card):
	def __init__(self):
		super().__init__(name="Goldrinn The Great Wolf", attack_value=4, health=4, 
						tier=5, m_type=MinionType.BEAST, has_deathrattle=True)
	
	def deathrattle(self, battle, friendly_minions, enemy_minions, j):
		if friendly_minions.warband:
			for minion in friendly_minions.warband:
				if minion.m_type == MinionType.BEAST:
					minion.attack_value += 4
					minion.health += 4



class HeraldOfFlame(Card):
# to be continued
	def __init__(self):
		super().__init__(name="Herald Of Flame", attack_value=5, health=6, tier=4, 
						m_type=MinionType.DRAGON, has_overkill=True)	

	def overkill(self, battle, j, k):

		any_died = False

		for i in range(len(battle.attacked_warband.warband)):
			if i == k:
				continue
			else:
				leftmost_minion = battle.attacked_warband.warband[i]
				leftmost_minion.take_damage(3, self.poisonous)
				
				if leftmost_minion.health > 0:
					break

				elif leftmost_minion.health == 0:
					any_died = True
					break

				elif leftmost_minion.health < 0:
					any_died = True
				
		return any_died

class IronhideDirehorn(Card):
	def __init__(self):
		super().__init__(name="Ironhide Direhorn", attack_value=7, health=7, tier=4, 
						m_type=MinionType.BEAST, has_overkill=True)	

	def overkill(self, battle, j, k):
		if len(battle.attacking_warband.warband) < 7:
			ironhide_runt = self.summon_minion(IronhideRunt)
			battle.attacking_warband.warband.insert(j + 1, ironhide_runt)






class InfestedWolf(Card):
	def __init__(self):
		super().__init__(name="Infested Wolf", attack_value=3, health=3, tier=3, 
						m_type=MinionType.BEAST, has_deathrattle=True)

	def deathrattle(self, battle, friendly_minions, enemy_minions, j):
		i = 0
		while len(friendly_minions.warband) < 7 and i != 2:
			spider = self.summon_minion(Spider)
			friendly_minions.warband.insert(j, spider)
			i += 1





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

class KindlyGrandmother(Card):
	def __init__(self):
		super().__init__(name="Kindly Grandmother", attack_value=1, health=1, tier=2, 
						m_type=MinionType.BEAST, has_deathrattle=True)

	def deathrattle(self, battle, friendly_minions, enemy_minions, j):
		wolf = self.summon_minion(BigBadWolf)
		friendly_minions.warband.insert(j, wolf)


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


# class MurlocWarleader(Card):
# 	def __init__(self):
# 		super().__init__(name="Murloc Warleader", attack_value=3, health=3, tier=2, 
# 			m_type=MinionType.MURLOC)


class Maexxna(Card):
	def __init__(self):
		super().__init__(name="Maexxna", attack_value=2, health=8, tier=6, 
						m_type=MinionType.BEAST, poisonous=True)


class NadinaTheRed(Card):
	def __init__(self):
		super().__init__(name="Nadina The Red", attack_value=7, health=4, tier=6, 
						m_type=MinionType.MINION, has_deathrattle=True)
	
	def deathrattle(self, battle, friendly_minions, enemy_minions, j):
		if friendly_minions.warband:
			for minion in friendly_minions.warband:
				if minion.m_type == MinionType.DRAGON:
					minion.has_ds = True


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

	def attack_in_start_of_combat(self, friendly_minions, enemy_minions, dead_warband, battle):
		damage = self.add_damage_in_combat(friendly_minions.warband)
		attacked_minion = random.choice(enemy_minions.warband)
		j = enemy_minions.warband.index(attacked_minion)
		attacked_minion.take_damage(damage, self.poisonous)

		if attacked_minion.health < 1:
			attacked_minion.die(enemy_minions.warband, j, dead_warband)
			if attacked_minion.has_deathrattle:
				attacked_minion.deathrattle(battle, enemy_minions, friendly_minions, j)
				if isinstance(attacked_minion, KaboomBot) or isinstance(attacked_minion, UnstableGhoul):
					return True


class RatPack(Card):
	def __init__(self):
		super().__init__(name="Rat Pack", attack_value=2, health=2, tier=2, 
						m_type=MinionType.BEAST, has_deathrattle=True)

	def deathrattle(self, battle, friendly_minions, enemy_minions, j):
		x = self.attack_value
		i = 0

		while len(friendly_minions.warband) < 7 and i != x:
			rat = self.summon_minion(Rat)
			friendly_minions.warband.insert(j + i, rat)
			i += 1



class RighteousProtector(Card):
	def __init__(self):
		super().__init__(name="Righteous Protector", attack_value=1, health=1, tier=1, 
						m_type=MinionType.MINION, taunt=True, has_ds =True)



class RockpoolHunter(Card):
	def __init__(self):
		super().__init__(name="Rockpool Hunter", attack_value=2, health=3, tier=1, 
						m_type=MinionType.MURLOC)



class SavannahHighmane(Card):
	def __init__(self):
		super().__init__(name="Savannah Highmane", attack_value=6, health=5, tier=4, 
						m_type=MinionType.BEAST, has_deathrattle=True)

	def deathrattle(self, battle, friendly_minions, enemy_minions, j):
		i = 0
		while len(friendly_minions.warband) < 7 and i != 2:
			hyena = self.summon_minion(Hyena)
			friendly_minions.warband.insert(j, hyena)
			i += 1




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



class SpawnOfnZoth(Card):
	def __init__(self):
		super().__init__(name="Spawn Of n'Zoth", attack_value=2, health=2, tier=2, 
						m_type=MinionType.MINION, has_deathrattle=True)
	
	def deathrattle(self, battle, friendly_minions, enemy_minions, j):
		if friendly_minions.warband:
			for minion in friendly_minions.warband:
				minion.attack_value += 1
				minion.health += 1



class TheBeast(Card):
	def __init__(self):
		super().__init__(name="The Beast", attack_value=9, health=7, tier=3, 
						m_type=MinionType.BEAST, has_deathrattle=True)

	def deathrattle(self, battle, friendly_minions, enemy_minions, j):

		if len(enemy_minions.warband) < 7:
			finkle_einhorn = self.summon_minion(FinkleEinhorn)
			last_place = len(enemy_minions.warband)
			enemy_minions.warband.insert(last_place, finkle_einhorn)



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



# class(es) not imported to create minions in warbands:
class BigBadWolf(Card):
	def __init__(self):
		super().__init__(name="Big Bad Wolf", attack_value=3, health=2, tier=1, 
						m_type=MinionType.BEAST)



class FinkleEinhorn(Card):
	def __init__(self):
		super().__init__(name="Finkle Einhorn", attack_value=3, health=3, tier=1, 
						m_type=MinionType.MINION)





class Hyena(Card):
	def __init__(self):
		super().__init__(name="Hyena", attack_value=2, health=2, tier=1, 
						m_type=MinionType.BEAST)




class IronhideRunt(Card):
	def __init__(self):
		super().__init__(name="Ironhide Runt", attack_value=7, health=7, tier=1, 
						m_type=MinionType.BEAST)



class Rat(Card):
	def __init__(self):
		super().__init__(name="Rat", attack_value=1, health=1, tier=1, 
						m_type=MinionType.BEAST)





class Spider(Card):
	def __init__(self):
		super().__init__(name="Spider", attack_value=1, health=1, tier=1, 
						m_type=MinionType.BEAST)



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