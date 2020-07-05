from card import *

class CobaltScalebane(Card):
	#add effect
	def __init__(self):
		super().__init__(name="Cobalt Scalebane", attack_value=5, health=5, tier=4, 
						m_type=MinionType.DRAGON)

class DragonspawnLieutenant(Card):
	def __init__(self):
		super().__init__(name="Dragonspawn Lieutenant", attack_value=2, health=3, 
						tier=1, m_type=MinionType.DRAGON, taunt=True)

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

class GlyphGuardian(Card):
	def __init__(self):
		super().__init__(name="Glyph Guardian", attack_value=2, health=4, tier=2, 
						m_type=MinionType.DRAGON)
	def attack(self):
		self.attack_value = 2 * self.attack_value

class HangryDragon(Card):
	def __init__(self):
		super().__init__(name="Hangry Dragon", attack_value=4, health=4, tier=3, 
						m_type=MinionType.DRAGON)

class HeraldOfFlame(Card):
# to be continued
	def __init__(self):
		super().__init__(name="Herald Of Flame", attack_value=5, health=6, tier=4, 
						m_type=MinionType.DRAGON, has_overkill=True)	
	def overkill(self, battle):
		k = battle.attacked_player.attacked_minion
		if len(battle.attacked_player.warband) > 1:
			for i in range(len(battle.attacked_player.warband)):
				if i == k:
					continue
				else:
					leftmost_minion = battle.attacked_player.warband[i]
					if leftmost_minion.health > 0:
						leftmost_minion.take_damage(3, self.poisonous, battle, 2)
						if leftmost_minion.health >= 0:
							break
						else:
							continue

class KalecgosArcaneAspect(Card):
	#effect
	def __init__(self):
		super().__init__(name="Kalecgos, Arcane Aspect", attack_value=4, health=12, 
						tier=6, m_type=MinionType.DRAGON)	 

class Murozond(Card):
	#btlcry
	def __init__(self):
		super().__init__(name="Murozond", attack_value=5, health=5, tier=5, 
						m_type=MinionType.DRAGON)	

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

class RazorgoreTheUntamed(Card):
	#effect
	def __init__(self):
		super().__init__(name="Razorgore, the Untamed", attack_value=2, health=4, 
						tier=5, m_type=MinionType.DRAGON)	

class StewardOfTime(Card):
	# add effect
	def __init__(self):
		super().__init__(name="Steward Of Time", attack_value=3, health=4, tier=2, 
						m_type=MinionType.DRAGON)

class TwilightEmissary(Card):
	#btlcry
	def __init__(self):
		super().__init__(name="Twilight Emissary", attack_value=4, health=4, tier=3, 
						m_type=MinionType.DRAGON)	

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