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
		has_ds=False, has_deathrattle=False, has_triggered_attack=False, has_overkill=False):
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

	def die(self, friendly_minions, j, dead_warband):
		del friendly_minions[j]
		dead_warband.append(self)

	def triggered_attack(self, enemy_minions, j):
		if j != 0 and j + 1 < len(enemy_minions):
			a = j - 1
			b = j + 1	
			enemy_minions[b].take_damage(self.attack_value)
		elif j == 0 and j + 1 <= len(enemy_minions):
			a = j + 1
		elif j == len(enemy_minions) - 1:
			a = j - 1
		enemy_minions[a].take_damage(self.attack_value)

	def summon_minions(self, n, minion_class):
		# n - number of summoned minions
		# just one type of minion
		summoned_minions = []
		for i in range(n):
			minion = minion_class()
			summoned_minions.append(minion)
		return summoned_minions


class CaveHydra(Card):
	def __init__(self):
		super().__init__(name="Cave Hydra", attack_value=2, health=4, tier=4, 
						has_triggered_attack=True, m_type=MinionType.BEAST)


class DragonspawnLieutenant(Card):
	def __init__(self):
		super().__init__(name="Dragonspawn Lieutenant", attack_value=2, health=3, 
						tier=1, m_type=MinionType.DRAGON, taunt=True)


class FiendishServant(Card):
	def __init__(self):
		super().__init__(name="Fiendish Servant", attack_value=2, health=1, tier=1, 
						m_type=MinionType.DEMON, has_deathrattle=True)
	
	def deathrattle(self, battle, friendly_minions, enemy_minions, j):
		friendly_random_minion = random.choice(friendly_minions.warband)
		friendly_random_minion.attack_value += self.attack_value


class FoeReaper4000(Card):
	def __init__(self):
		super().__init__(name="Foe Reaper 4000", attack_value=6, health=9, tier=6, 
						has_triggered_attack=True, m_type=MinionType.MECH)


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


class HarvestGolem(Card):
	def __init__(self):
		super().__init__(name="Harvest Golem", attack_value=2, health=3, tier=2, 
			m_type=MinionType.MECH, has_deathrattle=True)

	def deathrattle(self, battle, friendly_minions, enemy_minions, j):
		golem = self.summon_minions(1, DamagedGolem)
		friendly_minions.warband.insert(j, golem[0])

# class HeraldOfFlame(Card):
# 	def __init__(self):
# 		super().__init__(name="Herald Of Flame", attack_value=5, health=6, tier=4, 
# 			m_type=MinionType.DRAGON, has_overkill=True)	

# 	def overkill(self, enemy_minions):

# 		while True:
# 			most_left_minion = enemy_minions[0]
# 			most_left_minion.take_damage(3)

# 			if most_left_minion.health < 1:
# 				most_left_minion.die()

class IronhideDirehorn(Card):
	def __init__(self):
		super().__init__(name="Ironhide Direhorn", attack_value=7, health=7, tier=4, 
			m_type=MinionType.BEAST, has_overkill=True)	

	def overkill(self, battle, j):
		ironhide_runt = self.summon_minions(1, IronhideRunt)
		if len(battle.attacking_warband.warband) < 7:
			battle.attacking_warband.warband.insert(j + 1, ironhide_runt[0])


class Imprisoner(Card):
	def __init__(self):
		super().__init__(name="Imprisoner", attack_value=3, health=3, tier=2, 
			m_type=MinionType.DEMON, has_deathrattle=True)

	def deathrattle(self, battle, friendly_minions, enemy_minions, j):
		imp = self.summon_minions(1, Imp)
		friendly_minions.warband.insert(j, imp[0])


class InfestedWolf(Card):
	def __init__(self):
		super().__init__(name="Infested Wolf", attack_value=3, health=3, tier=3, 
			m_type=MinionType.BEAST, has_deathrattle=True)

	def deathrattle(self, battle, friendly_minions, enemy_minions, j):
		spiders = self.summon_minions(2, Spider)
		i = 0
		while len(friendly_minions.warband) < 7 and i != 2:
			friendly_minions.warband.insert(j, spiders[i])
			i += 1


class KaboomBot(Card):
	def __init__(self):
		super().__init__(name="Kaboom Bot", attack_value=2, health=2, tier=2, 
			m_type=MinionType.MECH, has_deathrattle=True)

	def deathrattle(self, battle, friendly_minions, enemy_minions, j):
		if enemy_minions.warband:
			enemy_random_minion = random.choice(enemy_minions.warband)
			i = enemy_minions.warband.index(enemy_random_minion)
			enemy_random_minion.take_damage(4)


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
				mechs = self.summon_minions(1, type(mech))
				if len(friendly_minions.warband) < 7 and i < 2:
					friendly_minions.warband.insert(j + i, mechs[0])
					i += 1
				else:
					break



class KindlyGrandmother(Card):
	def __init__(self):
		super().__init__(name="Kindly Grandmother", attack_value=1, health=1, tier=2, 
			m_type=MinionType.BEAST, has_deathrattle=True)

	def deathrattle(self, battle, friendly_minions, enemy_minions, j):
		wolf = self.summon_minions(1, BigBadWolf)
		friendly_minions.warband.insert(j, wolf[0])


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


class MechanoEgg(Card):
	def __init__(self):
		super().__init__(name="Mechano-Egg", attack_value=0, health=5, tier=4, 
			m_type=MinionType.MECH, has_deathrattle=True)

	def deathrattle(self, battle, friendly_minions, enemy_minions, j):
		robosaur = self.summon_minions(1, Robosaur)
		friendly_minions.warband.insert(j, robosaur[0])


class Mecharoo(Card):
	def __init__(self):
		super().__init__(name="Mecharoo", attack_value=1, health=1, tier=1, 
			m_type=MinionType.MECH, has_deathrattle=True)

	def deathrattle(self, battle, friendly_minions, enemy_minions, j):
		joebot = self.summon_minions(1, JoEBot)
		friendly_minions.warband.insert(j, joebot[0])


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
		attacked_minion.take_damage(damage)

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
		rats = self.summon_minions(x, Rat)
		i = 0
		while len(friendly_minions.warband) < 7 and i != x:
			rat = rats[i]
			friendly_minions.warband.insert(j, rat)
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
		hyenas = self.summon_minions(2, Hyena)
		i = 0
		while len(friendly_minions.warband) < 7 and i != 2:
			friendly_minions.warband.insert(j, hyenas[i])
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
		finkle_einhorn = self.summon_minions(1, FinkleEinhorn)
		if len(enemy_minions.warband) < 7:
			last_place = len(enemy_minions.warband)
			enemy_minions.warband.insert(last_place, finkle_einhorn[0])

class UnstableGhoul(Card):
	def __init__(self):
		super().__init__(name="Unstable Ghoul", attack_value=1, health=3, tier=2, 
						m_type=MinionType.MINION, has_deathrattle=True)
	
	def deathrattle(self, battle, friendly_minions, enemy_minions, j):
		if friendly_minions.warband:
			for minion in friendly_minions.warband:
				minion.take_damage(1)
		if enemy_minions.warband:
			for minion in enemy_minions.warband:
				minion.take_damage(1)


class Voidlord(Card):
	def __init__(self):
		super().__init__(name="Voidlord", attack_value=3, health=9, tier=5, 
						m_type=MinionType.DEMON, taunt=True, has_deathrattle=True)

	def deathrattle(self, battle, friendly_minions, enemy_minions, j):
		voidwalkers = self.summon_minions(3, Voidwalker)
		i = 0
		while len(friendly_minions.warband) < 7 and i != 3:
			friendly_minions.warband.insert(j, voidwalkers[i])
			i += 1

# class(es) not imported to create minions in warbands:
class BigBadWolf(Card):
	def __init__(self):
		super().__init__(name="Big Bad Wolf", attack_value=3, health=2, tier=1, 
						m_type=MinionType.BEAST)


class DamagedGolem(Card):
	def __init__(self):
		super().__init__(name="Damaged Golem", attack_value=2, health=1, tier=1, 
						m_type=MinionType.MECH)


class FinkleEinhorn(Card):
	def __init__(self):
		super().__init__(name="Finkle Einhorn", attack_value=3, health=3, tier=1, 
						m_type=MinionType.MINION)


class Hyena(Card):
	def __init__(self):
		super().__init__(name="Hyena", attack_value=2, health=2, tier=1, 
						m_type=MinionType.BEAST)


class Imp(Card):
	def __init__(self):
		super().__init__(name="Imp", attack_value=1, health=1, tier=1, 
						m_type=MinionType.DEMON)

class IronhideRunt(Card):
	def __init__(self):
		super().__init__(name="Ironhide Runt", attack_value=7, health=7, tier=1, 
						m_type=MinionType.BEAST)


class JoEBot(Card):
	def __init__(self):
		super().__init__(name="Jo-E Bot", attack_value=1, health=1, tier=1, 
						m_type=MinionType.MECH)

class Rat(Card):
	def __init__(self):
		super().__init__(name="Rat", attack_value=1, health=1, tier=1, 
						m_type=MinionType.BEAST)


class Robosaur(Card):
	def __init__(self):
		super().__init__(name="Robosaur", attack_value=8, health=8, tier=1, 
						m_type=MinionType.MECH)


class Spider(Card):
	def __init__(self):
		super().__init__(name="Spider", attack_value=1, health=1, tier=1, 
						m_type=MinionType.BEAST)


class Voidwalker(Card):
	def __init__(self):
		super().__init__(name="Voidwalker", attack_value=1, health=3, tier=1, 
						m_type=MinionType.DEMON, taunt=True)

		



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