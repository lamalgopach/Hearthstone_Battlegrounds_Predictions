from hsbg_combat.combat import simulate
from hsbg_combat.minions import *

# warband1 = [
# 	RatPack(), 
# 	InfestedWolf(), 
# 	SelflessHero(), 
# 	GlyphGuardian(), 
# 	RedWhelp(), 
# 	DragonspawnLieutenant(),
# 	SpawnOfnZoth(),
# 	]

# warband2 = [
# 	SpawnOfnZoth(), 
# 	RockpoolHunter(), 
# 	InfestedWolf(), 
# 	SelflessHero(), 
# 	GlyphGuardian(),
# 	RedWhelp(), 
# 	RatPack(),
# 	]

warband1 = [
	SpawnOfnZoth(),  
	KindlyGrandmother(), 
	MechanoEgg(), 
	UnstableGhoul(),
	RockpoolHunter(),
	Voidlord(), 
	RatPack(),
	]

warband2 = [
	SelflessHero(),
	Mecharoo(),
	MechanoEgg(), 
	KangorsApprentice(), 
	RedWhelp(),
	InfestedWolf(),
	Voidlord(), 
	]

print(f"equal warbands: {simulate(warband1, warband1)}")
print(f"different warbands: {simulate(warband1, warband2)}")
