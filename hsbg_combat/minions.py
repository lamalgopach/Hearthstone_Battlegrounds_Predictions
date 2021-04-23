import random 
from .card import *

class BolvarFireblood(Card):
	def __init__(self):
		super().__init__(name="Bolvar, Fireblood", attack_value=1, health=7, tier=4, 
						m_type=MinionType.MINION, has_ds=True, 
						has_effect="friend_ds_lost", effect=BolvarFirebloodEffect())
	def die(self, battle, status, j):
		super().die(battle, status, j)
		if status == 1:
			battle.attacking_player.effects_after_friend_lost_ds.pop(self)
		else:
			battle.attacked_player.effects_after_friend_lost_ds.pop(self)


class BrannBronzebeard(Card):
# add effect
	def __init__(self):
		super().__init__(name="Brann Bronzebeard", attack_value=2, health=4, tier=5, 
						m_type=MinionType.MINION)

class CrowdFavorite(Card):
	# add special function later
	def __init__(self):
		super().__init__(name="Crowd Favorite", attack_value=4, health=4, tier=3, 
						m_type=MinionType.MINION)

class Crystalweaver(Card):
	#btlcry
	def __init__(self):
		super().__init__(name="Crystalweaver", attack_value=5, health=4, tier=3, 
						m_type=MinionType.MINION)

class DefenderOfArgus(Card):
	#btlcry
	def __init__(self):
		super().__init__(name="Defender of Argus", attack_value=2, health=3, tier=4, 
						m_type=MinionType.MINION)

class Houndmaster(Card):
	#btlcry
	def __init__(self):
		super().__init__(name="Houndmaster", attack_value=4, health=3, tier=3, 
						m_type=MinionType.MINION)

class KangorsApprentice(Card):
	def __init__(self):
		super().__init__(name="Kangor's Apprentice", attack_value=3, health=6, tier=6, 
						m_type=MinionType.MINION, has_deathrattle=True)

	def deathrattle(self, battle, status):
		friendly_minions = battle.attacking_player.warband if status == 1 else battle.attacked_player.warband
		j = battle.attacking_player.dead_minions_dict[self] if status == 1 else battle.attacked_player.dead_minions_dict[self]
		warband = []
		warband = battle.attacking_player.dead_minions if status == 1 else battle.attacked_player.dead_minions
		mechs_to_summon = []
		for minion in warband:
			if minion.m_type == MinionType.MECH:
				mechs_to_summon.append(minion)
		if mechs_to_summon:
			mechs = []
			i = 0
			for mech in mechs_to_summon:
				if len(friendly_minions) < 7 and i < 2:
					summoned_mech = self.summon_minion(type(mech), battle, status)
					# summoned_mech.attack_value = mech.attack_value
					# summoned_mech.health = mech.health
					# summoned_mech.taunt = mech.taunt
					# summoned_mech.has_ds = mech.has_ds
					# summoned_mech.has_deathrattle = mech.has_deathrattle
					# summoned_mech.has_triggered_attack = mech.has_triggered_attack
					friendly_minions.insert(j + i, summoned_mech)
					i += 1
				else:
					break

class LightfangEnforcer(Card):
	# effect
	def __init__(self):
		super().__init__(name="Lightfang Enforcer", attack_value=2, health=2, tier=5, 
						m_type=MinionType.MINION)

class MenagerieMagician(Card):
	#btlcry
	def __init__(self):
		super().__init__(name="Menagerie Magician", attack_value=4, health=4, tier=4, 
						m_type=MinionType.MINION)

class NadinaTheRed(Card):
	def __init__(self):
		super().__init__(name="Nadina The Red", attack_value=7, health=4, tier=6, 
						m_type=MinionType.MINION, has_deathrattle=True)
	def deathrattle(self, battle, status):
		friendly_minions = battle.attacking_player.warband if status == 1 else battle.attacked_player.warband
		if friendly_minions:
			for minion in friendly_minions:
				if minion.m_type == MinionType.DRAGON:
					minion.has_ds = True

class PackLeader(Card):
	def __init__(self):
		super().__init__(name="Pack Leader", attack_value=3, health=3, tier=3, 
						m_type=MinionType.MINION, has_effect="friend_summoned", 
						effect=PackLeaderEffect())
	def die(self, battle, status, j):
		super().die(battle, status, j)
		if status == 1:
			battle.attacking_player.effects_after_friend_is_summoned.pop(self)
		else:
			battle.attacked_player.effects_after_friend_is_summoned.pop(self)

class RighteousProtector(Card):
	def __init__(self):
		super().__init__(name="Righteous Protector", attack_value=1, health=1, tier=1, 
						m_type=MinionType.MINION, taunt=True, has_ds =True)
	
class SelflessHero(Card):
	def __init__(self):
		super().__init__(name="Selfless Hero", attack_value=2, health=1, tier=1, 
						m_type=MinionType.MINION, has_deathrattle=True)
	def deathrattle(self, battle, status):
		friendly_minions = battle.attacking_player.warband if status == 1 else battle.attacked_player.warband
		if not friendly_minions:
			return
		minions_no_ds = [minion for minion in friendly_minions if not minion.has_ds]
		if not minions_no_ds:
			return
		minion = random.choice(minions_no_ds)
		minion.has_ds = True

class ShifterZerus(Card):
	# add effect
	def __init__(self):
		super().__init__(name="Shifter Zerus", attack_value=1, health=1, tier=3, 
						m_type=MinionType.MINION)

class SoulJuggler(Card):
	def __init__(self):
		super().__init__(name="Soul Juggler", attack_value=3, health=3, tier=3, 
						m_type=MinionType.MINION, has_effect="friend_death", 
						effect=SoulJugglerEffect())

	def die(self, battle, status, j):
		super().die(battle, status, j)
		if status == 1:
			battle.attacking_player.effects_after_friend_is_dead.pop(self)
			print(battle.attacking_player.effects_after_friend_is_dead, "effects effects")

		else:
			battle.attacked_player.effects_after_friend_is_dead.pop(self)
			print(battle.attacked_player.effects_after_friend_is_dead, "effects effects")

class SpawnOfnZoth(Card):
	def __init__(self):
		super().__init__(name="Spawn Of n'Zoth", attack_value=2, health=2, tier=2, 
						m_type=MinionType.MINION, has_deathrattle=True)
	def deathrattle(self, battle, status):
		friendly_minions = battle.attacking_player.warband if status == 1 else battle.attacked_player.warband
		if friendly_minions:
			for minion in friendly_minions:
				minion.attack_value += 1
				minion.health += 1

class StrongshellScavenger(Card):
	# btlcry
	def __init__(self):
		super().__init__(name="Strongshell Scavenger", attack_value=2, health=3, tier=5,
						m_type=MinionType.MINION)

class UnstableGhoul(Card):
	def __init__(self):
		super().__init__(name="Unstable Ghoul", attack_value=1, health=3, tier=2, 
						m_type=MinionType.MINION, has_deathrattle=True)
	def deathrattle(self, battle, status):
		friendly_minions = battle.attacking_player.warband if status == 1 else battle.attacked_player.warband
		enemy_minions = battle.attacked_player.warband if status == 1 else battle.attacking_player.warband
		f_m = tuple(friendly_minions)
		e_m = tuple(enemy_minions)
		if f_m:
			for m in f_m:
				m.take_damage(1, self.poisonous, battle, status)
		if e_m:
			st = 2 if status == 1 else 1
			for m in e_m:
				m.take_damage(1, self.poisonous, battle, st)
		if status == 1:
			battle.attacking_player.effects_causing_next_death.append(self)
		else:
			battle.attacked_player.effects_causing_next_death.append(self)

class VirmenSensei(Card):
	#btlcry
	def __init__(self):
		super().__init__(name="Virmen Sensei", attack_value=4, health=5, tier=4, 
						m_type=MinionType.MINION)

class WaxriderTogwaggle(Card):
	def __init__(self):
		super().__init__(name="Waxrider Togwaggle", attack_value=1, health=2, tier=2, 
						m_type=MinionType.MINION)
	def change_stats_after_attack(self, minion1, minion2, battle, status):
		if minion.m_type == MinionType.DRAGON:
			self.health += 2
			self.attack_value += 2

class WrathWeaver(Card):
	#btlcry damage
	def __init__(self):
		super().__init__(name="Wrath Weaver", attack_value=1, health=1, tier=1, 
						m_type=MinionType.MINION)

class ZappSlywick(Card):
	def __init__(self):
		super().__init__(name="ZappSlywick", attack_value=7, health=10, tier=6, 
						m_type=MinionType.MINION, has_windfury=True)	

# class(es) not imported to create minions in warbands
class FinkleEinhorn(Card):
	def __init__(self):
		super().__init__(name="Finkle Einhorn", attack_value=3, health=3, tier=1, 
						m_type=MinionType.MINION)

class PackLeaderEffect(Effect):
	def __init__(self):
		super().__init__(class_type=PackLeader)

	def change_stats(self, minion, battle, status):
		if minion.m_type == MinionType.BEAST:
			minion.attack_value += 3
		return minion

class SoulJugglerEffect(Effect):
	def __init__(self):
		super().__init__(class_type=SoulJuggler)
	def change_stats(self, minion, battle, status):
		if minion.m_type == MinionType.DEMON:
			random_enemy_minion = None
			if status == 1:
				player = battle.attacked_player
			else:
				player = battle.attacking_player
			if player.warband:
				minions_no_negative_health = [minion for minion in player.warband if minion.health > 0]
				if minions_no_negative_health:
					random_enemy_minion = random.choice(minions_no_negative_health)
				else:
					random_enemy_minion = None
				if random_enemy_minion:
					st = 1 if status == 2 else 2
					random_enemy_minion.take_damage(3, False, battle, st)
					if random_enemy_minion.health < 1:
						player.effects_causing_next_death.append(random_enemy_minion)
						if isinstance(random_enemy_minion, SoulJuggler):
							j = player.warband.index(random_enemy_minion)
							random_enemy_minion.die(battle, st, j)


# gain sth after losing DS:
class BolvarFirebloodEffect(Effect):
	def __init__(self):
		super().__init__(class_type=BolvarFireblood)
	def change_stats(self, minion, battle, status):
		if status == 1:
			dict_ = battle.attacking_player.effects_after_friend_lost_ds
		else:
			dict_ = battle.attacked_player.effects_after_friend_lost_ds
		obj = list(dict_.keys())[list(dict_.values()).index(self)]
		obj.attack_value += 2

# Jakub:
# minion = SpawnOfnZoth()
# if minion.deathrattle is not None:
# if minion.deathrattle:
# # if hasattr(minion, "deathrattle"):
# 	minion.deathrattle(friendly_minions, j)

# 	def attack(self, game_state, target):
# 		target.health -= self.attack_value
# 		self.health -= target.attack_value
# 		return game_state

# class GlyphGuardian(Minion):
# 	def attack(*args, **kwargs):
# 		self.attack_value *= 2
# 		super().attack(*args, **kwargs)