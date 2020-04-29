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

	def __init__(self, name, attack, life, tier, m_type, is_taunted):
		self.name = name
		self.attack = attack
		self.life = life
		self.tier = tier
		self.m_type = m_type
		self.is_taunted = is_taunted

class Event:
	def __init__(self, evnt):
		self.evnt = evnt

def Taunt(Event):

	def is_attacked_first(self):
		attacked_first = True


#CHECKCHEKCCHECKCHEKCHCKLECHEKCHEKCHEKCHEKCHECK


class AddingAttack(Event):
	# murloc_warleader

	is_alive = True
	is_attack_added = False

	def __init__(self, is_alive, additional_attack, objects_to_whom):
		
		for i in self.objects_to_whom:
			i.attack += additional_attack

		is_attack_added = True

class DoublingAttack(Event):
	# glyph guardian

	is_attacking = True

	def __init__(self, attack):
		self.attack = 2*attack



class StartOfCombat(Event):
	# red whelp
	is_attacking = True

	def __init__(self, warband):
		damage = sum(1 for i in self.warband if i.m_type == 2)




