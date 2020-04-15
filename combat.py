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

	def __init__(self, name, attack, life):
		# minion_type
		self.name = name
		self.attack = attack
		self.life = life
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


rockpool_hunter = Minion("Rockpool Hunter", 2, 3)
righteous_protector = Minion("Righteous Protector", 1, 1)
gosia = Minion("Goslawix", 3, 2)
szymon = Minion("Szymbox", 2, 4)
szuwar = Minion("Szuwarex", 4, 2)
meret = Minion("Meretux", 3, 3)
bob = Minion("Bob", 1, 4)
rafal = Minion("Rafson", 9, 1)
greg = Minion("Gregson", 1, 10)

minions_1 = [gosia, meret, szymon, szuwar, righteous_protector] 
minions_2 = [rafal, greg, bob, rockpool_hunter]

Player_1 = Player("Gosia", minions_1)
Player_2 = Player("Bob", minions_2)



def attack(minion_1, minion_2):

	minion_1.life -= minion_2.attack
	minion_2.life -= minion_1.attack


	return minion_1, minion_2



if len(Player_1.minions) > len(Player_2.minions):
	p1 = Player_1.minions
	p2 = Player_2.minions


elif len(Player_1.minions) < len(Player_2.minions):
	p1 = Player_2.minions
	p2 = Player_1.minions

else:
	p1 = random.choice([Player_2.minions, Player_2.minions])


i = 1

while p1 and p2:
	print()

	if i == 0:
		
		j = random.randint(0, len(p2) - 1)
		minion_1 = p1[0]
		minion_2 = p2[j]

		print(minion_1.name, minion_1.attack, minion_1.life)
		print(minion_2.name, minion_2.attack, minion_2.life)

		minion_1, minion_2 = attack(minion_1, minion_2)

		print(minion_1.name, minion_1.attack, minion_1.life)
		print(minion_2.name, minion_2.attack, minion_2.life)

		if minion_1.life <= 0:
			p1 = p1[1:]

		if minion_2.life <= 0:
			del p2[j]


	elif i % 2 == 0:

		j = random.randint(0, len(p2) - 1)

		minion_1 = p1.next
		minion_2 = p2[j]
		print(minion_1.name, minion_1.attack, minion_1.life)
		print(minion_2.name, minion_2.attack, minion_2.life)

		minion_1, minion_2 = attack(minion_1, minion_2)

		print(minion_1.name, minion_1.attack, minion_1.life)
		print(minion_2.name, minion_2.attack, minion_2.life)

		if minion_1.life <= 0:
			p1 = p1[1:]

		if minion_2.life <= 0:
			del p2[j]

	else:

		j = random.randint(0, len(p1) - 1)


		minion_1 = p2.next
		minion_2 = p1[j]
		print(minion_1.name, minion_1.attack, minion_1.life)
		print(minion_2.name, minion_2.attack, minion_2.life)

		minion_1, minion_2 = attack(minion_1, minion_2)

		print(minion_1.name, minion_1.attack, minion_1.life)
		print(minion_2.name, minion_2.attack, minion_2.life)

		if minion_2.life <= 0:
			del p1[j]

		if minion_1.life <= 0:
			p2 = p2[1:]


	i += 1

