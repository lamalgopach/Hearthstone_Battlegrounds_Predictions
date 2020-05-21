# Hearthstone Battlegrounds combat simulator

This is a simple simulation of Hearthstone Battlegrounds combat phase. 

```python3
from combat import simulate
from minions import *

warband1 = [RockpoolHunter(), InfestedWolf(), RedWhelp(), RedWhelp()]
warband2 = [SpawnOfnZoth(), InfestedWolf(), SelflessHero(), GlyphGuardian()] 
print(f"equal warbands: {simulate(warband1, warband1)}")
print(f"different warbands: {simulate(warband1, warband2)}")
```

Above code outputs:

```
equal warbands: {'first_wins': 0.32, 'tie': 0.34, 'second_wins': 0.34}
different warbands: {'first_wins': 0.23, 'tie': 0.18, 'second_wins': 0.59}
```


Currently 8 minion types are supported: Dragonspawn Lieutenant, Glyph Guardian, Infested Wolf, RedWhelp, Righteous Protector, Rockpool Hunter, Spawn Of n'Zoth, Selfless Hero.

The following special effects are supported:
 - deathrattles - events triggered by death, e.g. summon minions and others or add +1/+1 
 - taunts - attack priority
 - divine shield - first instance of damage is negated
 - start of combat - events triggered before attack phase begins

Combat logic is implemented in `combat.py`.
`simulate` function repeatedly simulates battles and outputs probabilities of winning for each of the players.

In the future I'm planning to implement more minions and make the simulation more interactive. 