import random
from random import choice
from minions import minions_lst

def create_warband():
	warband = []
	while len(warband) != 7:
		s = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
		obj = minions_lst[s]
		warband.append(obj)

	return warband

# alices_warband = create_warband()
# bobs_warband = create_warband()

# print("Alices:")
# for minion in alices_warband:
# 	print(minion.name)
# print()

# print("Bobs:")
# for minion in bobs_warband:
# 	print(minion.name)