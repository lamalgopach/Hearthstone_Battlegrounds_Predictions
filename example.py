from hsbg_combat.combat import simulate
from hsbg_combat.minions import *
from hsbg_combat.battle import *
from hsbg_combat.beasts import *
from hsbg_combat.demons import *
from hsbg_combat.dragons import *
from hsbg_combat.mechs import *
from hsbg_combat.murlocs import *
from hsbg_combat.multiple_types_deathrattle_minions import *

# from hsbg_combat import *


warband1 = [ 
	StewardOfTime(),
	GlyphGuardian(),
	HangryDragon(),
	TwilightEmissary(),
	CobaltScalebane(),

	AnnihilanBattlemaster(),
	Voidlord(),  
	ImpMama(),
	FloatingWatcher(),
	FiendishServant(),

	TheBeast(),
	SavannahHighmane(),
	InfestedWolf(),
	Maexxna(),
	IronhideDirehorn(),
	GentleMegasaur(),
	Ghastcoiler(),

	MetaltoothLeaper(),
	FoeReaper4000(),
	HarvestGolem(),
	Mecharoo(),
	Zoobot(),
	ScrewjankClunker(),
	SneedsOldShredder(),

	CrowdFavorite(),
	ShifterZerus(),
	DefenderOfArgus(),
	VirmenSensei(),
	LightfangEnforcer(),
	Crystalweaver(),
	Houndmaster(),
	MenagerieMagician(),
	BrannBronzebeard(),
	StrongshellScavenger(),

	MurlocTidehunter(),
	KingBagurgle(),
	FelfinNavigator(),
	Toxfin(),

	]

warband2 = [
	
	DragonspawnLieutenant(),
	HeraldOfFlame(),
	RedWhelp(),
	Murozond(),
	RazorgoreTheUntamed(),
	KalecgosArcaneAspect(),

	MurlocTidecaller(),
	ColdlightSeer(),
	RockpoolHunter(),
	PrimalfinLookout(),

	GoldrinnTheGreatWolf(),
	Alleycat(),
	CaveHydra(),
	RatPack(),
	KindlyGrandmother(),
	RabidSaurolisk(),

	SecurityRover(),
	MechanoEgg(),
	KaboomBot(),
	MicroMachine(),
	PogoHopper(),
	IronSensei(),
	PilotedShredder(),
	ReplicatingMenace(),

	ImpGangBoss(),
	Imprisoner(),  
	Voidlord(),
	NathrezimOverseer(),

	RighteousProtector(), 
	SpawnOfnZoth(),
	SelflessHero(), 
	UnstableGhoul(), 
	NadinaTheRed(),
	KangorsApprentice(),
	WrathWeaver(),
	]

print(f"equal warbands: {simulate(warband1, warband1, 100)}")
print(f"different warbands: {simulate(warband1, warband2, 100)}")
