from hsbg_combat.combat import simulate
from hsbg_combat.minions import *

warband1 = [
	RatPack(), 
	InfestedWolf(), 
	SelflessHero(), 
	GlyphGuardian(), 
	RedWhelp(), 
	DragonspawnLieutenant(),
	SpawnOfnZoth(),
	]

warband2 = [
	SpawnOfnZoth(), 
	RockpoolHunter(), 
	InfestedWolf(), 
	SelflessHero(), 
	GlyphGuardian(),
	RedWhelp(), 
	RatPack(),
	]

print(f"equal warbands: {simulate(warband1, warband1)}")
print(f"different warbands: {simulate(warband1, warband2)}")
