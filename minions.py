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

	def __init__(self, name, attack, health, tier, m_type, is_taunted, has_ds, has_deathrattle):
		self.name = name
		self.attack = attack
		self.health = health
		self.tier = tier
		self.m_type = m_type
		self.is_taunted = is_taunted
		self.has_ds = has_ds
		self.has_deathrattle = has_deathrattle


	def take_damage(self, damage):
		if damage == 0:
			return

		if self.has_ds:
			self.has_ds = False
		else:
			self.health -= damage

	def remove_ds(self):
		self.has_ds = False


class SelflessHero(Card):

	def deathrattle(self, minion):
		minion.has_ds = True



# types of cards:
# minions completed:

dragonspawn_lieutenant = Card("Dragonspawn Lieutenant", 2, 3, 1, 2, True, False, False)
righteous_protector = Card("Righteous Protector", 1, 1, 1, 0, True, True, False)


# classes written:
murloc_warleader = Card("Murloc Warleader", 3, 3, 2, 1, False, False, False)
glyph_guardian = Card("Glyph Guardian", 2, 4, 2, 2, False, False, False)
red_whelp = Card("Red Whelp", 1, 2, 1, 2, False, False, False)

#deathrattles:
spawn_of_nzoth = Card("Spawn Of n'Zoth", 2, 2, 2, 0, False, False, False)
infested_wolf = Card("Infested Wolf", 3, 3, 3, 3, False, False, False)
selfless_hero = SelflessHero("Selfless Hero", 2, 1, 1, 0, False, False, True)

# battlecry:
rockpool_hunter = Card("Rockpool Hunter", 2, 3, 1, 1, False, False, False)

minions = [dragonspawn_lieutenant, righteous_protector, murloc_warleader,
			glyph_guardian, red_whelp, spawn_of_nzoth, infested_wolf, selfless_hero, 
			rockpool_hunter]











# class Event:
# 	def __init__(self, evnt):
# 		self.evnt = evnt



#CHECKCHEKCCHECKCHEKCHCKLECHEKCHEKCHEKCHEKCHECK


# class AddingAttack(Event):
# 	# murloc_warleader

# 	is_alive = True
# 	is_attack_added = False

# 	def __init__(self, is_alive, additional_attack, objects_to_whom):
		
# 		for i in self.objects_to_whom:
# 			i.attack += additional_attack

# 		is_attack_added = True

# class DoublingAttack(Event):
# 	# glyph guardian

# 	is_attacking = True

# 	def __init__(self, attack):
# 		self.attack = 2*attack



# class StartOfCombat(Event):
# 	# red whelp
# 	is_attacking = True

# 	def __init__(self, warband):
# 		damage = sum(1 for i in self.warband if i.m_type == 2)




