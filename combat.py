from enum import Enum
import random
from random import choice
import copy

class MinionType(Enum):
	BEAST = 1
	DEMON = 2
	DRAGON = 3
	MECH = 4
	MURLOC = 5



class Minion:

	name = None
	life = None
	attack = None
	# minion type = "demon" etc.

	def __init__(self, name, attack, life, tier):
		# minion_type
		self.name = name
		self.attack = attack
		self.life = life
		self.tier = tier
		# self.minion_type = minion_type
		#minion type

	# def attack(self):


	# def die(self):
	# 	if attack >= self.life:



# class *name_minion type(Minion):
	# this class can rewrite method from the Minion class
	# or can have different initializer than Minion
	# or:
	# def __init__(self, name, life, attack):
    	# super().__init__(name, life, attack, 'name_minion type')
    	# initializing with default minion type



# we have some number of minions, two opposite players
# so we start from the left and attack the random opposite minion
# after first minion, the first minion form the second player plays
# it attacks another random minion
# if minion

class Player:

	def __init__(self, name, minions):
		self.name = name
		self.minions = minions
		# self.warband = warband
		# ?wtf is warband?


rockpool_hunter = Minion("Rockpool Hunter", 2, 3, 1)
righteous_protector = Minion("Righteous Protector", 3, 2, 2)
gosia = Minion("Goslawix", 3, 2, 3)
szymon = Minion("Szymbox", 3, 4, 1)
szuwar = Minion("Szubarux", 4, 3, 2)
meret = Minion("Meretux", 3, 3, 3)
gaben = Minion("Gaben", 3, 2, 1)
baben = Minion("Baben", 4, 4, 2)
maden = Minion("Maden", 5, 4, 3)

minions_1 = [gosia, meret, szymon, szuwar, righteous_protector] 
minions_2 = [maden, baben, gaben, rockpool_hunter]

Player_1 = Player("Gosia", minions_1)
Player_2 = Player("Bob", minions_2)



def attack(minion_1, minion_2):

	minion_1.life -= minion_2.attack
	minion_2.life -= minion_1.attack


	return minion_1, minion_2

def count_damage(minions):

	damage = 0

	for minion in minions:
		damage += minion.tier

	return damage



if len(Player_1.minions) > len(Player_2.minions):
	
	p1 = Player_1.minions
	p2 = Player_2.minions

	Player_1.minions = copy.deepcopy(p1)
	Player_2.minions = copy.deepcopy(p2)


elif len(Player_1.minions) < len(Player_2.minions):
	
	p1 = Player_2.minions
	p2 = Player_1.minions

	Player_1.minions = copy.deepcopy(p1)
	Player_2.minions = copy.deepcopy(p2)

else:
	
	p1 = random.choice([Player_2.minions, Player_2.minions])
	# tbc

i = 0
f = 1

k, l = 0, 0

r = k

game = [p1, p2]

while p1 and p2:

	j = random.randint(0, len(game[i + f]) - 1)

	minion_1 = game[i][r]
	minion_2 = game[i + f][j]

	minion_1, minion_2 = attack(minion_1, minion_2)

	if minion_1.life <= 0:
		del game[i][r]
		r -= 1

	if minion_2.life <= 0:
		del game[i + f][j]

	r += 1

	if i == 0:
		i += 1
		f -= 2
		k = r

		if l >= len(game[1]):
			l = 0

		r = l

	else:
		i -= 1
		f += 2
		l = r
		
		if k >= len(game[0]):
			k = 0

		r = k

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


# for z in Player_1.minions:
# 	print(z.name)

# print()

# for z in Player_2.minions:
# 	print(z.name)