from minions import *

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

