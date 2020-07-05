import random
from enum import Enum
import copy

class MinionType(Enum):
	MINION = 0
	MURLOC = 1
	DRAGON = 2
	BEAST = 3
	MECH = 4
	DEMON = 5


class Card:
	def __init__(self, *, name, attack_value, health, tier, m_type, taunt=False, 
		
		has_ds=False, has_deathrattle=False, has_triggered_attack=False, 
		has_overkill=False, poisonous=False, has_windfury=False, 
		
		has_effect=False,
		effect=None):

		self.name = name
		self.attack_value = attack_value
		self.health = health
		self.tier = tier
		self.m_type = m_type

		self.taunt = taunt
		self.has_ds = has_ds
		self.has_deathrattle = has_deathrattle

		self.has_triggered_attack = has_triggered_attack
		self.has_overkill = has_overkill
		self.poisonous = poisonous
		self.has_windfury = has_windfury

		#EFFECTS:
		self.has_effect = has_effect
		self.effect = effect


	def attack(self):
		# used in Glyph Guardian
		return

	def take_poison(self):
		
		if self.has_ds:
			self.has_ds = False

		else:
			self.health = 0

	def take_damage(self, damage, poisonous, battle, status):

		if damage == 0:
			return

		if self.has_ds:
			self.has_ds = False
			effects = battle.attacking_player.effects_after_friend_lost_ds if status == 1 else battle.attacked_player.effects_after_friend_lost_ds
			if effects:
				for k, v in effects.items():
					v.change_stats(self, battle, status)

		elif poisonous:
			self.health = 0
		else:
			self.health -= damage

		# ORIGINAL:
		# if self.has_ds:
		# 	self.has_ds = False
		# else:
		# 	self.health -= damage

	def triggered_attack(self, battle):

		enemy_minions = battle.attacked_player.warband
		x = battle.attacked_player.attacked_minion
		left_i = None
		right_i = None
		left_minion = None
		right_minion = None
		
		if x != 0 and x + 1 < len(enemy_minions):
			left_i = x - 1
			right_i = x + 1
		elif x == 0 and x + 1 <= len(enemy_minions):
			right_i = x + 1
		elif x == len(enemy_minions) - 1:
			left_i = x - 1
		
		if left_i:
			left_minion = enemy_minions[left_i]
		
		if right_i:
			right_minion = enemy_minions[right_i]

		main_minion = enemy_minions[x]
		main_minion.take_damage(self.attack_value, self.poisonous, battle, status=2)

		if left_minion:
			left_minion.take_damage(self.attack_value, self.poisonous, battle, status=2)

		if right_minion:
			right_minion.take_damage(self.attack_value, self.poisonous, battle, status=2)
	

	def die(self, battle, status, j):
		friendly_minions = battle.attacking_player.warband if status == 1 else battle.attacked_player.warband
		del friendly_minions[j]
		effects = battle.attacking_player.effects_after_friend_is_dead if status == 1 else battle.attacked_player.effects_after_friend_is_dead

		if effects:
			for k, v in effects.items():
				v.change_stats(self, battle, status)


	def summon_minion(self, minion_class, battle, status):
		minion = minion_class()
		effects = battle.attacking_player.effects_after_friend_is_summoned if status == 1 else battle.attacked_player.effects_after_friend_is_summoned
		if effects:
			for obj, effect_obj in effects.items():
				effect_obj.change_stats(minion, battle, status)
		return minion


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



class DeflectoBot(Card):
	def __init__(self):
		super().__init__(name="Deflect-o-Bot", attack_value=3, health=2, tier=3, 
						m_type=MinionType.MECH, has_ds=True, 
						has_effect="friend_summoned",
						effect=DeflectoBotChangeStats())

	def die(self, battle, status, j):
		super().die(battle, status, j)
		if status == 1:	
			battle.attacking_player.effects_after_friend_is_summoned.pop(self)
		else:
			battle.attacked_player.effects_after_friend_is_summoned.pop(self)

class DrakonidEnforcer(Card):
	def __init__(self):
		super().__init__(name="Drakonid Enforcer", attack_value=3, health=6, tier=4, 
						m_type=MinionType.DRAGON, has_effect="friend_ds_lost", 
						effect=DrakonidEnforcerEffect())

	def die(self, battle, status, j):
		super().die(battle, status, j)
		if status == 1:
			battle.attacking_player.effects_after_friend_lost_ds.pop(self)
		else:
			battle.attacked_player.effects_after_friend_lost_ds.pop(self)


class Houndmaster(Card):
	#btlcry
	def __init__(self):
		super().__init__(name="Houndmaster", attack_value=4, health=3, tier=3, 
						m_type=MinionType.MINION)


class Junkbot(Card):
	def __init__(self):
		super().__init__(name="Junkbot", attack_value=1, health=5, tier=5, 
						m_type=MinionType.MECH, 
						has_effect="friend_death",
						effect=JunkbotEffect())

	def die(self, battle, status, j):
		super().die(battle, status, j)
		if status == 1:
			battle.attacking_player.effects_after_friend_is_dead.pop(self)
		else:
			battle.attacked_player.effects_after_friend_is_dead.pop(self)
	

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
					# if DeflectOBot in friendly_minions and random_deathrattle_minion.m_type == MinionType.MECH:
					# 	DeflectOBot.has_ds = True
					# 	DeflectOBot.attack_value += 1
					#	DeflectOBot.change_stats()
					i += 1
				else:
					break


class LightfangEnforcer(Card):
	# effect
	def __init__(self):
		super().__init__(name="Lightfang Enforcer", attack_value=2, health=2, tier=5, 
						m_type=MinionType.MINION)

class MamaBear(Card):
	def __init__(self):
		super().__init__(name="Mama Bear", attack_value=5, health=5, tier=6, 
						m_type=MinionType.BEAST, has_effect="friend_summoned",
						effect=MamaBearChangeStats())

	def die(self, battle, status, j):
		super().die(battle, status, j)
		if status == 1:
			battle.attacking_player.effects_after_friend_is_summoned.pop(self)
		else:
			battle.attacked_player.effects_after_friend_is_summoned.pop(self)


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
						m_type=MinionType.BEAST, has_effect="friend_summoned", 
						effect=PackLeaderChangeStats())

	def die(self, battle, status, j):
		super().die(battle, status, j)
		if status == 1:
			battle.attacking_player.effects_after_friend_is_summoned.pop(self)
		else:
			battle.attacked_player.effects_after_friend_is_summoned.pop(self)


class RedWhelp(Card):
	def __init__(self):
		super().__init__(name="Red Whelp", attack_value=1, health=2, tier=1, 
						m_type=MinionType.DRAGON)

	def add_damage_in_combat(self, friendly_minions):
		damage = 0
		for minion in friendly_minions:
			if minion.m_type == MinionType.DRAGON:
				damage += 1
		return damage


class RighteousProtector(Card):
	def __init__(self):
		super().__init__(name="Righteous Protector", attack_value=1, health=1, tier=1, 
						m_type=MinionType.MINION, taunt=True, has_ds =True)


class ScavengingHyena(Card):
	def __init__(self):
		super().__init__(name="Scavenging Hyena", attack_value=2, health=2, tier=1, 
						m_type=MinionType.BEAST, 
						has_effect="friend_death",
						effect=ScavengingHyenaEffect())

	def die(self, battle, status, j):
		super().die(battle, status, j)
		if status == 1:
			battle.attacking_player.effects_after_friend_is_dead.pop(self)
		else:
			battle.attacked_player.effects_after_friend_is_dead.pop(self)
	

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



# class SoulJuggler(Card):
# 	def __init__(self):
# 		super().__init__(name="Soul Juggler", attack_value=3, health=3, tier=3, 
# 						m_type=MinionType.MINION, 
# 						friend_death=True,
# 						effects_after_friend_is_dead=SoulJugglerEffect())

# 	def die(self, battle, status, j):
# 		super().die(battle, status, j)
# 		if status == 1:
# 			battle.attacking_player.effects_after_friend_is_dead.pop(self)
# 			battle.attacking_player.attack_after_deaths -= 1
# 		else:
# 			battle.attacked_player.effects_after_friend_is_dead.pop(self)
# 			battle.attacked_player.attack_after_deaths -= 1




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

#effects:
class Effect:
	def __init__(self, class_type):
		self.class_type = class_type


class DeflectoBotChangeStats(Effect):
	def __init__(self):
		super().__init__(class_type=DeflectoBot)


	def change_stats(self, minion, battle, status):
		if minion.m_type == MinionType.MECH:
			if status == 1:
				dict_ = battle.attacking_player.effects_after_friend_is_summoned
			else:
				dict_ = battle.attacked_player.effects_after_friend_is_summoned

			obj = list(dict_.keys())[list(dict_.values()).index(self)]
			obj.attack_value += 1
			obj.has_ds = True


class MamaBearChangeStats(Effect):
	def __init__(self):
		super().__init__(class_type=MamaBear)

	def change_stats(self, minion, battle, status):
		if minion.m_type == MinionType.BEAST:
			minion.health += 5
			minion.attack_value += 5
		return minion


class PackLeaderChangeStats(Effect):
	def __init__(self):
		super().__init__(class_type=PackLeader)

	def change_stats(self, minion, battle, status):
		if minion.m_type == MinionType.BEAST:
			minion.attack_value += 3
		return minion

##### gain sth after death:
class JunkbotEffect(Effect):
	def __init__(self):
		super().__init__(class_type=Junkbot)

	def change_stats(self, minion, battle, status):
		if minion.m_type == MinionType.MECH:
			if status == 1:
				dict_ = battle.attacking_player.effects_after_friend_is_dead
			else:
				dict_ = battle.attacked_player.effects_after_friend_is_dead

			obj = list(dict_.keys())[list(dict_.values()).index(self)]
			obj.attack_value += 2
			obj.health += 2



class ScavengingHyenaEffect(Effect):
	def __init__(self):
		super().__init__(class_type=ScavengingHyena)

	def change_stats(self, minion, battle, status):
		if minion.m_type == MinionType.BEAST:
			if status == 1:
				dict_ = battle.attacking_player.effects_after_friend_is_dead
			else:
				dict_ = battle.attacked_player.effects_after_friend_is_dead

			obj = list(dict_.keys())[list(dict_.values()).index(self)]
			obj.attack_value += 2
			obj.health += 1


# gain sth after losing DS:
class DrakonidEnforcerEffect(Effect):
	def __init__(self):
		super().__init__(class_type=DrakonidEnforcer)

	def change_stats(self, minion, battle, status):

		if status == 1:
			dict_ = battle.attacking_player.effects_after_friend_lost_ds
		else:
			dict_ = battle.attacked_player.effects_after_friend_lost_ds

		obj = list(dict_.keys())[list(dict_.values()).index(self)]
		obj.attack_value += 2
		obj.health += 2


# class SoulJugglerEffect(Effect):
# 	def __init__(self):
# 		super().__init__(class_type=SoulJuggler)

# 	def change_stats(self, minion, battle, status):
# 		pass
		
		# if minion.m_type == MinionType.DEMON:
		# 	random_enemy_minion = None
		# 	if status == 1:
		# 		if battle.attacked_player.warband:
		# 			battle.attacking_player.attack_after_deaths += 1
		# 			# random_enemy_minion = random.choice(battle.attacked_player.warband)
		# 			# j = battle.attacked_player.warband.index(random_enemy_minion)
		# 	else:
		# 		if battle.attacking_player.warband:
		# 			battle.attacked_player.attack_after_deaths += 1
					# random_enemy_minion = random.choice(battle.attacking_player.warband)
					# j = battle.attacking_player.warband.index(random_enemy_minion)

			# if random_enemy_minion:
			# 	random_enemy_minion.take_damage(3, False)
			# 	if random_enemy_minion.health < 1:
			# 		print("[[[[[[[[[[[[", random_enemy_minion.name, "]]]]]]]]]]]]")
			# 		print("[[[[[[[[[[[[", random_enemy_minion.health, "]]]]]]]]]]]]")
			# 		player = battle.attacking_player if status == 2 else battle.attacked_player
			# 		player.effects_causing_next_death.append(random_enemy_minion)



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

