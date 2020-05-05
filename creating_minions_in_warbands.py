import random
from random import choice
from minions import minions_lst
import copy

def create_warband():
	warband = []
	while len(warband) != 7:
		s = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
		obj = copy.copy(minions_lst[s])
		warband.append(obj)

	return warband
