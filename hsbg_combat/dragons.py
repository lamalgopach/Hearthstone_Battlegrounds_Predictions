from minions import *


class DragonspawnLieutenant(Card):
	def __init__(self):
		super().__init__(name="Dragonspawn Lieutenant", attack_value=2, health=3, 
						tier=1, m_type=MinionType.DRAGON, taunt=True)


class GlyphGuardian(Card):
	def __init__(self):
		super().__init__(name="Glyph Guardian", attack_value=2, health=4, tier=2, 
						m_type=MinionType.DRAGON)
		
	def attack(self):
		self.attack_value = 2 * self.attack_value


class HangryDragon(Card):
	def __init__(self):
		super().__init__(name="Hangry Dragon ", attack_value=4, health=4, tier=3, 
						m_type=MinionType.DRAGON)


class HeraldOfFlame(Card):
# to be continued
	def __init__(self):
		super().__init__(name="Herald Of Flame", attack_value=5, health=6, tier=4, 
						m_type=MinionType.DRAGON, has_overkill=True)	

	def overkill(self, battle, j, k):

		any_died = False

		for i in range(len(battle.attacked_warband.warband)):
			if i == k:
				continue
			else:
				leftmost_minion = battle.attacked_warband.warband[i]
				leftmost_minion.take_damage(3, self.poisonous)
				
				if leftmost_minion.health > 0:
					break

				elif leftmost_minion.health == 0:
					any_died = True
					break

				elif leftmost_minion.health < 0:
					any_died = True
				
		return any_died


class RedWhelp(Card):
	def __init__(self):
		super().__init__(name="Red Whelp", attack_value=1, health=2, tier=1, 
						m_type=MinionType.DRAGON)

	def add_damage_in_combat(self, minions):
		damage = 0
		for minion in minions:
			if minion.m_type == MinionType.DRAGON:
				damage += 1
		return damage

	def attack_in_start_of_combat(self, friendly_minions, enemy_minions, dead_warband, battle):
		damage = self.add_damage_in_combat(friendly_minions.warband)
		attacked_minion = random.choice(enemy_minions.warband)
		j = enemy_minions.warband.index(attacked_minion)
		attacked_minion.take_damage(damage, self.poisonous)

		if attacked_minion.health < 1:
			attacked_minion.die(enemy_minions.warband, j, dead_warband)
			if attacked_minion.has_deathrattle:
				attacked_minion.deathrattle(battle, enemy_minions, friendly_minions, j)
				if isinstance(attacked_minion, KaboomBot) or isinstance(attacked_minion, UnstableGhoul):
					return True


class StewardOfTime(Card):
	def __init__(self):
		super().__init__(name="Steward Of Time", attack_value=3, health=4, tier=2, 
						m_type=MinionType.DRAGON)