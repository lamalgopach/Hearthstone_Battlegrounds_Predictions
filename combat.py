from enum import Enum
import random
from random import choice

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
righteous_protector = Minion("Righteous Protector", 1, 1, 2)
gosia = Minion("Goslawix", 3, 2, 3)
szymon = Minion("Szymbox", 2, 4, 1)
szuwar = Minion("Szubarux", 4, 2, 2)
meret = Minion("Meretux", 3, 3, 3)
gaben = Minion("Gaben", 1, 4, 1)
baben = Minion("Baben", 9, 1, 2)
maden = Minion("Maden", 1, 10, 3)

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


elif len(Player_1.minions) < len(Player_2.minions):
	p1 = Player_2.minions
	p2 = Player_1.minions

else:
	p1 = random.choice([Player_2.minions, Player_2.minions])


i = 1

k = 0
l = 0

while p1 and p2:
	print(k, l)


	if i % 2 != 0:


		j = random.randint(0, len(p2) - 1)


		minion_1 = p1[k]
		minion_2 = p2[j]


		minion_1, minion_2 = attack(minion_1, minion_2)


		if minion_1.life <= 0:
			del p1[k]
			k -= 1

		if minion_2.life <= 0:
			del p2[j]

		k += 1

	else:
		
		j = random.randint(0, len(p1) - 1)

		minion_1 = p2[l]
		minion_2 = p1[j]

		minion_1, minion_2 = attack(minion_1, minion_2)

		if minion_1.life <= 0:
			del p2[l]
			l -= 1

		if minion_2.life <= 0:
			del p1[j]

		l += 1


	if k >= len(p1):
		k = 0

	if l >= len(p2):
		l = 0

	i += 1


	if not p1 and not p2:
		print("NO WINNER")

	elif not p2:
		print(Player_1.name, "WINNER")
		damage = count_damage(p1)

	elif not p1:
		print(Player_2.name, "WINNER")
		damage = count_damage(p2)
		
print(damage)




