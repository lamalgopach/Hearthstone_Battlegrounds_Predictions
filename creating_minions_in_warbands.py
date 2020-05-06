import random
from random import choice
from minions import DragonspawnLieutenant, GlyphGuardian, InfestedWolf, MurlocWarleader
from minions import RedWhelp, RighteousProtector, RockpoolHunter, SpawnOfnZoth, SelflessHero
import copy


def create_minion():
	class_types = [DragonspawnLieutenant(), GlyphGuardian(), InfestedWolf(), 
				MurlocWarleader(),RedWhelp(), RighteousProtector(), RockpoolHunter(), 
				SpawnOfnZoth(), SelflessHero()]
	return random.choice(class_types)

def create_warband():
	warband = []
	while len(warband) != 7:
		minion = create_minion()
		warband.append(minion)
	return warband