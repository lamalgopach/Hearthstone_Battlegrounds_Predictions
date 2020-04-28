from enum import Enum
import random
from random import choice
import copy

#do not create class of minions

class MinionType(Enum):

	PLAIN = 0
	MURLOC = 1
	DRAGON = 2
	BEAST = 3
	MECH = 4
	DEMON = 5


class Card:
	name = None
	life = None
	attack = None
	tier = None

	def __init__(self, name, attack, life, tier, m_type):
		self.name = name
		self.attack = attack
		self.life = life
		self.tier = tier
		self.m_type = m_type




class Event:
	def __init__(self, evnt):
		self.evnt = evnt

#CHECKCHEKCCHECKCHEKCHCKLECHEKCHEKCHEKCHEKCHECK


class AddingAttack(Event):
	# murloc_warleader

	is_alive = True
	is_attack_added = False

	def __init__(self, is_alive, additional_attack, objects_to_whom):
		
		for i in self.objects_to_whom:
			i.attack += additional_attack

		is_added = True

class DoublingAttack(Event):
	# glyph guardian

	# is_attacking = True

	def __init__(self, attack):
		self.attack = 2*attack

# class Taunt(Event):
# 	is_attacked_first = True



class StartOfCombat(Event):
	# red whelp
	is_attacking = True

	def __init__(self, warband):
		damage = sum(1 for i in self.warband if i.m_type == 2)





class Player:

	def __init__(self, name, warband):
		self.name = name
		self.warband = warband
		# type of warband -> list

# classes written:
murloc_warleader = Card("Murloc Warleader", 3, 3, 2, 1)
glyph_guardian = Card("Glyph Guardian", 2, 4, 2, 2)
red_whelp = Card("Red Whelp", 1, 2, 1, 2)


#taunt:
dragonspawn_lieutenant = Card("Dragonspawn Lieutenant", 2, 3, 1, 2)
# + divine shield
righteous_protector = Card("Righteous Protector", 1, 1, 1, 0)



#deathrattles:
spawn_of_nzoth = Card("Spawn Of n'Zoth", 2, 2, 2, 0)
infested_wolf = Card("Infested Wolf", 3, 3, 3, 3)
selfless_hero = Card("Selfless Hero", 2, 1, 1, 0)

# battlecry:
rockpool_hunter = Card("Rockpool Hunter", 2, 3, 1, 1)

alices_warband = [spawn_of_nzoth, dragonspawn_lieutenant, infested_wolf, murloc_warleader] 
bobs_warband = [rockpool_hunter, righteous_protector, glyph_guardian, selfless_hero, red_whelp]

Player_1 = Player("Alice", alices_warband)
Player_2 = Player("Bob", bobs_warband)



def attack(minion_1, minion_2):

	minion_1.life -= minion_2.attack
	minion_2.life -= minion_1.attack


	return minion_1, minion_2

def count_damage(warband):

	damage = 0

	for minion in warband:
		damage += minion.tier

	return damage



if len(Player_1.warband) > len(Player_2.warband):
	
	p1 = Player_1.warband
	p2 = Player_2.warband

	Player_1.warband = copy.deepcopy(p1)
	Player_2.warband = copy.deepcopy(p2)


elif len(Player_1.warband) < len(Player_2.warband):
	
	p1 = Player_2.warband
	p2 = Player_1.warband

	Player_1.warband = copy.deepcopy(p1)
	Player_2.warband = copy.deepcopy(p2)

else:
	
	p1 = random.choice([Player_2.warband, Player_2.warband])


	if p1 == Player_1.warband:
		p2 = Player_2.warband
	else:
		p2 = Player_1.warband


#game
index = 0
factor = 1

first_player_idx, second_player_idx = 0, 0

next_minion = first_player_idx

game = [p1, p2]

while p1 and p2:

	random_minion = random.randint(0, len(game[index + factor]) - 1)

	minion_1 = game[index][next_minion]
	minion_2 = game[index + factor][random_minion]

	minion_1, minion_2 = attack(minion_1, minion_2)

	if minion_1.life <= 0:
		del game[index][next_minion]
		next_minion -= 1

	if minion_2.life <= 0:
		del game[index + factor][random_minion]

	next_minion += 1

	if index == 0:
		index += 1
		factor -= 2

		first_player_idx = next_minion

		if second_player_idx >= len(game[1]):
			second_player_idx = 0

		next_minion = second_player_idx

	else:
		index -= 1
		factor += 2
		second_player_idx = next_minion
		
		if first_player_idx >= len(game[0]):
			first_player_idx = 0

		next_minion = first_player_idx

	if not p1 and not p2:
		print("NO WINNER")
		damage = 0

	elif not p2:
		print(Player_1.name, "WINNER")
		damage = count_damage(p1)

	elif not p1:
		print(Player_2.name, "WINNER")
		damage = count_damage(p2)

print("DAMAGE: ", damage)


# print()
# for z in p1:
# 	print(z.name)

# print()
# for z in p2:
# 	print(z.name)
# print()


# for z in Player_1.warband:
# 	print(z.name)

# print()

# for z in Player_2.warband:
# 	print(z.name)