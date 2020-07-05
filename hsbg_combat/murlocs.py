from card import *


class ColdlightSeer(Card):
	#btlcry
	def __init__(self):
		super().__init__(name="Coldlight Seer", attack_value=2, health=3, tier=3, 
						m_type=MinionType.MURLOC)


class FelfinNavigator(Card):
	#btlcry
	def __init__(self):
		super().__init__(name="Felfin Navigator", attack_value=4, health=4, tier=3, 
						m_type=MinionType.MURLOC)


class KingBagurgle(Card):
	# add the battlecry later
	def __init__(self):
		super().__init__(name="King Bagurgle", attack_value=6, health=3, tier=5, 
						m_type=MinionType.MURLOC, has_deathrattle=True)

	def deathrattle(self, battle, status):
		friendly_minions = battle.attacking_player.warband if status == 1 else battle.attacked_player.warband
		if friendly_minions:
			for minion in friendly_minions:
				if minion.m_type == MinionType.MURLOC:
					minion.attack_value += 2
					minion.health += 2


class MurlocTidecaller(Card):
# add attack
	def __init__(self):
		super().__init__(name="Murloc Tidecaller", attack_value=1, health=2, tier=1, 
						m_type=MinionType.MURLOC)


class MurlocTidehunter(Card):
	#btlcry
	def __init__(self):
		super().__init__(name="Murloc Tidehunter", attack_value=2, health=1, tier=1, 
						m_type=MinionType.MURLOC)


# class MurlocWarleader(Card):
# 	def __init__(self):
# 		super().__init__(name="Murloc Warleader", attack_value=3, health=3, tier=2, 
# 			m_type=MinionType.MURLOC)

class OldMurkEye(Card):
	def __init__(self):
		super().__init__(name="Old Murk Eye", attack_value=2, health=4, tier=1, 
						m_type=MinionType.MURLOC)	

	def add_attack(self, friendly_minions, enemy_minions):
		
		for minion in friendly_minions.warband:
			if minion.m_type == MinionType.MURLOC:
				self.attack_value += 1

		for minion in enemy_minions.warband:
			if minion.m_type == MinionType.MURLOC:
				self.attack_value += 1

class PrimalfinLookout(Card):
	#Btlcry
	def __init__(self):
		super().__init__(name="Primalfin Lookout", attack_value=3, health=2, tier=5, 
						m_type=MinionType.MURLOC)	


class RockpoolHunter(Card):
	# btlcry
	def __init__(self):
		super().__init__(name="Rockpool Hunter", attack_value=2, health=3, tier=1, 
						m_type=MinionType.MURLOC)


class Toxfin(Card):
	# btlcry
	def __init__(self):
		super().__init__(name="Toxfin", attack_value=1, health=2, tier=4, 
						m_type=MinionType.MURLOC)


# summoned:
class MurlocScout(Card):
	def __init__(self):
		super().__init__(name="Murloc Scout", attack_value=1, health=1, tier=1, 
						m_type=MinionType.MURLOC)

