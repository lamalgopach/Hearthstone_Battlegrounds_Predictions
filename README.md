# Hearthstone Battlegrounds combat simulator

This is a simple simulation of Hearthstone Battlegrounds combat phase. 

```python3
from hsbg_combat.combat import simulate
from hsbg_combat.minions import *

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


Currently 73 minion out of 92 types are supported (+ x summoned)

11 Dragons
	- Dragonspawn Lieutenant, Glyph Guardian, Red Whelp, Steward Of Time, Hangry Dragon
	Twilight Emissary, Cobalt Scalebane, Razorgore The Untamed, Kalecgos Arcane Aspect, Herald Of Flame, Murozond,

13 Beasts:
	- Infested Wolf, The Beast, Savannah Highmane, Maexxna, Ironhide Direhorn, Gentle Megasaur, Ghastcoiler, Goldrinn The GreatWolf, Alleycat, Cave Hydra, Rat Pack, Kindly Grandmother, Rabid Saurolisk, 
+ 6 summoned:
	- Big Bad Wolf, Hyena, Ironhide Runt, Rat, Spider, Tabbycat,

17 Minions:
	- Righteous Protector, Spawn Of n'Zoth, Selfless Hero, Kangor's Apprentice, Crystalweaver, Houndmaster, Menagerie Magician, Brann Bronzebeard, Strongshell Scavenger, Wrath Weaver, Crowd Favorite, Shifter Zerus, Defender Of Argus, Virmen Sensei, Lightfang Enforcer, Unstable Ghoul, Nadina The Red,
+ 1 summoned:
	- Finkle Einhorn

8 Murlocs:
	- Rockpool Hunter, Murloc Tidehunter, King Bagurgle, Felfin Navigator, Toxfin, Murloc Tidecaller, Coldlight Seer, Primalfin Lookout,
+ 1 summoned: 
	- Murloc Scout,


9 Demons:
	- Annihilan Battlemaster, Voidlord, Imp Mama, Floating Watcher, Fiendish Servant, Imp Gang Boss, Imprisoner, Nathrezim Overseer, 
+ 2 summoned:
	- Imp, Voidwalker,


15 Mechs: 
	- Metaltooth Leaper, Harvest Golem, Mechano-Egg, Mecharoo, Zoobot, Screwjank Clunker, Sneed's Old Shredder, Kaboom Bot, Micro Machine, Pogo-Hopper, Iron Sensei, 
	Piloted Shredder, Replicating Menace, Security Rover, Foe Reaper 4000,
+ 5 summoned: 
	- DamagedGolem, GuardBot, JoEBot, Microbot, Robosaur


The following special effects are supported:
 - deathrattles - events triggered by death, e.g. summon minions and others or add +1/+1 
 - taunts - attack priority
 - divine shield - first instance of damage is negated
 - start of combat - events triggered before attack phase begins
 - triggered attack - minions next to are also damaged
 - poisonus - attacked minion dies immidiately if doesn't have the divine shield

Combat logic is implemented in `combat.py`.
`simulate` function repeatedly simulates battles and outputs probabilities of winning for each of the players.

In the future I'm planning to implement the rest of the minions and make the simulation more interactive. 