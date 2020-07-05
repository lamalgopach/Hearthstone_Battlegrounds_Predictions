from card import *

class Alleycat(Card):
	#btlcry
	def __init__(self):
		super().__init__(name="Alleycat", attack_value=1, health=1, tier=1, 
						m_type=MinionType.BEAST)

class CaveHydra(Card):
	def __init__(self):
		super().__init__(name="Cave Hydra", attack_value=2, health=4, tier=4, 
						has_triggered_attack=True, m_type=MinionType.BEAST)

class GentleMegasaur(Card):
	# btlcry
	def __init__(self):
		super().__init__(name="Gentle Megasaur", attack_value=5, health=4, tier=6, 
						m_type=MinionType.BEAST)

class GoldrinnTheGreatWolf(Card):
	def __init__(self):
		super().__init__(name="Goldrinn, the Great Wolf", attack_value=4, health=4, 
						tier=5, m_type=MinionType.BEAST, has_deathrattle=True)
	
	def deathrattle(self, battle, status):
		friendly_minions = battle.attacking_player.warband if status == 1 else battle.attacked_player.warband
		if friendly_minions:
			for minion in friendly_minions:
				if minion.m_type == MinionType.BEAST:
					minion.attack_value += 4
					minion.health += 4

class InfestedWolf(Card):
	def __init__(self):
		super().__init__(name="Infested Wolf", attack_value=3, health=3, tier=3, 
						m_type=MinionType.BEAST, has_deathrattle=True)

	def deathrattle(self, battle, status):
		friendly_minions = battle.attacking_player.warband if status == 1 else battle.attacked_player.warband
		j = battle.attacking_player.dead_minions_dict[self] if status == 1 else battle.attacked_player.dead_minions_dict[self]
		i = 0
		while len(friendly_minions) < 7 and i != 2:
			spider = self.summon_minion(Spider, battle, status)
			friendly_minions.insert(j, spider)
			i += 1

class IronhideDirehorn(Card):
	def __init__(self):
		super().__init__(name="Ironhide Direhorn", attack_value=7, health=7, tier=4, 
						m_type=MinionType.BEAST, has_overkill=True)	

	def overkill(self, battle):
		j = battle.attacking_player.attack_index
		if len(battle.attacking_player.warband) < 7:
			ironhide_runt = self.summon_minion(IronhideRunt, battle, status=1)
			battle.attacking_player.warband.insert(j + 1, ironhide_runt)

class KindlyGrandmother(Card):
	def __init__(self):
		super().__init__(name="Kindly Grandmother", attack_value=1, health=1, tier=2, 
						m_type=MinionType.BEAST, has_deathrattle=True)

	def deathrattle(self, battle, status):
		friendly_minions = battle.attacking_player.warband if status == 1 else battle.attacked_player.warband
		j = battle.attacking_player.dead_minions_dict[self] if status == 1 else battle.attacked_player.dead_minions_dict[self]
		wolf = self.summon_minion(BigBadWolf, battle, status)
		friendly_minions.insert(j, wolf)

class Maexxna(Card):
	def __init__(self):
		super().__init__(name="Maexxna", attack_value=2, health=8, tier=6, 
						m_type=MinionType.BEAST, poisonous=True)

class MamaBear(Card):
	def __init__(self):
		super().__init__(name="Mama Bear", attack_value=5, health=5, tier=6, 
						m_type=MinionType.BEAST, has_effect="friend_summoned",
						effect=MamaBearChangeStats())

	def die(self, battle, status, j):
		super().die(battle, status, j)
		if status == 1:
			battle.attacking_player.effects_after_friend_is_summoned.pop(self)
		else:
			battle.attacked_player.effects_after_friend_is_summoned.pop(self)

class RabidSaurolisk(Card):
	#action on turn
	def __init__(self):
		super().__init__(name="Rabid Saurolisk", attack_value=3, health=1, tier=1, 
						m_type=MinionType.BEAST)

class RatPack(Card):
	def __init__(self):
		super().__init__(name="Rat Pack", attack_value=2, health=2, tier=2, 
						m_type=MinionType.BEAST, has_deathrattle=True)

	def deathrattle(self, battle, status):
		friendly_minions = battle.attacking_player.warband if status == 1 else battle.attacked_player.warband
		j = battle.attacking_player.dead_minions_dict[self] if status == 1 else battle.attacked_player.dead_minions_dict[self]
		# j = battle.attacking_player.warband.index(self) if status == 1 else battle.attacked_player.warband.index(self)

		x = self.attack_value
		i = 0

		while len(friendly_minions) < 7 and i != x:
			rat = self.summon_minion(Rat, battle, status)
			friendly_minions.insert(j + i, rat)
			i += 1

class SavannahHighmane(Card):
	def __init__(self):
		super().__init__(name="Savannah Highmane", attack_value=6, health=5, tier=4, 
						m_type=MinionType.BEAST, has_deathrattle=True)

	def deathrattle(self, battle, status):
		friendly_minions = battle.attacking_player.warband if status == 1 else battle.attacked_player.warband
		j = battle.attacking_player.dead_minions_dict[self] if status == 1 else battle.attacked_player.dead_minions_dict[self]
		i = 0
		while len(friendly_minions) < 7 and i != 2:
			hyena = self.summon_minion(Hyena, battle, status)
			friendly_minions.insert(j, hyena)
			i += 1

class ScavengingHyena(Card):
	def __init__(self):
		super().__init__(name="Scavenging Hyena", attack_value=2, health=2, tier=1, 
						m_type=MinionType.BEAST, 
						has_effect="friend_death",
						effect=ScavengingHyenaEffect())

	def die(self, battle, status, j):
		super().die(battle, status, j)
		if status == 1:
			battle.attacking_player.effects_after_friend_is_dead.pop(self)
		else:
			battle.attacked_player.effects_after_friend_is_dead.pop(self)

class TheBeast(Card):
	def __init__(self):
		super().__init__(name="The Beast", attack_value=9, health=7, tier=3, 
						m_type=MinionType.BEAST, has_deathrattle=True)

	def deathrattle(self, battle, status):
		enemy_minions = battle.attacked_player.warband if status == 1 else battle.attacking_player.warband
		if len(enemy_minions) < 7:
			finkle_einhorn = self.summon_minion(FinkleEinhorn, battle, status)
			last_place = len(enemy_minions)
			enemy_minions.insert(last_place, finkle_einhorn)

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
		super().__init__(name="Ironhide Runt", attack_value=5, health=5, tier=1, 
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

# effects:
class MamaBearChangeStats(Effect):
	def __init__(self):
		super().__init__(class_type=MamaBear)

	def change_stats(self, minion, battle, status):
		if minion.m_type == MinionType.BEAST:
			minion.health += 5
			minion.attack_value += 5
		return minion

# gain sth after death:
class ScavengingHyenaEffect(Effect):
	def __init__(self):
		super().__init__(class_type=ScavengingHyena)

	def change_stats(self, minion, battle, status):
		if minion.m_type == MinionType.BEAST:
			if status == 1:
				dict_ = battle.attacking_player.effects_after_friend_is_dead
			else:
				dict_ = battle.attacked_player.effects_after_friend_is_dead

			obj = list(dict_.keys())[list(dict_.values()).index(self)]
			obj.attack_value += 2
			obj.health += 1