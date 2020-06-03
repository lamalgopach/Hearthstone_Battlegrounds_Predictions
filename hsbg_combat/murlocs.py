from minions import *


class ColdlightSeer(Card):
	#btlcry
	def __init__(self):
		super().__init__(name="Coldlight Seer", attack_value=2, health=3, tier=3, 
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


# summoned:
class MurlocScout(Card):
	def __init__(self):
		super().__init__(name="Murloc Scout", attack_value=1, health=1, tier=1, 
						m_type=MinionType.MURLOC)
