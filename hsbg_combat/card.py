import random
from enum import Enum

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

		if minion.has_effect:
			player = battle.attacking_player if status == 1 else battle.attacked_player
			player.add_to_effect_dict(minion, minion.has_effect)

		effects = battle.attacking_player.effects_after_friend_is_summoned if status == 1 else battle.attacked_player.effects_after_friend_is_summoned
		if effects:
			for obj, effect_obj in effects.items():
				effect_obj.change_stats(minion, battle, status)
		return minion

#effects:
class Effect:
	def __init__(self, class_type):
		self.class_type = class_type