from minions import *


class Alleycat(Card):
	#btlcry
	def __init__(self):
		super().__init__(name="Alleycat", attack_value=1, health=1, tier=1, 
						m_type=MinionType.BEAST)


class CaveHydra(Card):
	def __init__(self):
		super().__init__(name="Cave Hydra", attack_value=2, health=4, tier=4, 
						has_triggered_attack=True, m_type=MinionType.BEAST)


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

class IronhideDirehorn(Card):
	def __init__(self):
		super().__init__(name="Ironhide Direhorn", attack_value=7, health=7, tier=4, 
						m_type=MinionType.BEAST, has_overkill=True)	

	def overkill(self, battle, j, k):
		if len(battle.attacking_warband.warband) < 7:
			ironhide_runt = self.summon_minion(IronhideRunt)
			battle.attacking_warband.warband.insert(j + 1, ironhide_runt)

class KindlyGrandmother(Card):
	def __init__(self):
		super().__init__(name="Kindly Grandmother", attack_value=1, health=1, tier=2, 
						m_type=MinionType.BEAST, has_deathrattle=True)

	def deathrattle(self, battle, friendly_minions, enemy_minions, j):
		wolf = self.summon_minion(BigBadWolf)
		friendly_minions.warband.insert(j, wolf)


class Maexxna(Card):
	def __init__(self):
		super().__init__(name="Maexxna", attack_value=2, health=8, tier=6, 
						m_type=MinionType.BEAST, poisonous=True)



class RabidSaurolisk(Card):
	#action on turn
	def __init__(self):
		super().__init__(name="Rabid Saurolisk", attack_value=3, health=1, tier=1, 
						m_type=MinionType.BEAST)



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


class TheBeast(Card):
	def __init__(self):
		super().__init__(name="The Beast", attack_value=9, health=7, tier=3, 
						m_type=MinionType.BEAST, has_deathrattle=True)

	def deathrattle(self, battle, friendly_minions, enemy_minions, j):

		if len(enemy_minions.warband) < 7:
			finkle_einhorn = self.summon_minion(FinkleEinhorn)
			last_place = len(enemy_minions.warband)
			enemy_minions.warband.insert(last_place, finkle_einhorn)



# summoned:
class BigBadWolf(Card):
	def __init__(self):
		super().__init__(name="Big Bad Wolf", attack_value=3, health=2, tier=1, 
						m_type=MinionType.BEAST)

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

class Tabbycat(Card):
	def __init__(self):
		super().__init__(name="Tabbycat", attack_value=1, health=1, tier=1, 
						m_type=MinionType.BEAST)

