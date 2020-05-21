from combat import simulate
from minions import *

warband1 = [RockpoolHunter(), InfestedWolf(), RedWhelp(), RedWhelp()]
warband2 = [SpawnOfnZoth(), InfestedWolf(), SelflessHero(), GlyphGuardian()] 
print(f"equal warbands: {simulate(warband1, warband1)}")
print(f"different warbands: {simulate(warband1, warband2)}")
