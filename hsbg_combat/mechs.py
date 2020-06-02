from minions import *

class FoeReaper4000(Card):
	def __init__(self):
		super().__init__(name="Foe Reaper 4000", attack_value=6, health=9, tier=6, 
						has_triggered_attack=True, m_type=MinionType.MECH)


class HarvestGolem(Card):
	def __init__(self):
		super().__init__(name="Harvest Golem", attack_value=2, health=3, tier=2, 
						m_type=MinionType.MECH, has_deathrattle=True)

	def deathrattle(self, battle, friendly_minions, enemy_minions, j):
		golem = self.summon_minion(DamagedGolem)
		friendly_minions.warband.insert(j, golem)


class KaboomBot(Card):
	def __init__(self):
		super().__init__(name="Kaboom Bot", attack_value=2, health=2, tier=2, 
						m_type=MinionType.MECH, has_deathrattle=True)

	def deathrattle(self, battle, friendly_minions, enemy_minions, j):
		if enemy_minions.warband:
			enemy_random_minion = random.choice(enemy_minions.warband)
			i = enemy_minions.warband.index(enemy_random_minion)
			enemy_random_minion.take_damage(4, self.poisonous)

class MicroMachine(Card):
	# tbd; gain 
	def __init__(self):
		super().__init__(name="Micro Machine", attack_value=1, health=2, tier=1, 
						m_type=MinionType.MECH)

class MechanoEgg(Card):
	def __init__(self):
		super().__init__(name="Mechano-Egg", attack_value=0, health=5, tier=4, 
						m_type=MinionType.MECH, has_deathrattle=True)

	def deathrattle(self, battle, friendly_minions, enemy_minions, j):
		robosaur = self.summon_minion(Robosaur)
		friendly_minions.warband.insert(j, robosaur)


class Mecharoo(Card):
	def __init__(self):
		super().__init__(name="Mecharoo", attack_value=1, health=1, tier=1, 
						m_type=MinionType.MECH, has_deathrattle=True)

	def deathrattle(self, battle, friendly_minions, enemy_minions, j):
		joebot = self.summon_minion(JoEBot)
		friendly_minions.warband.insert(j, joebot)


class SecurityRover(Card):
	def __init__(self):
		super().__init__(name="Security Rover", attack_value=2, health=6, tier=4, 
						m_type=MinionType.MECH, damage_effect=True)

	def act_after_damage(self, battle, friendly_minions, enemy_minions, j):
		if len(friendly_minions.warband) < 7:
			guard_bot = self.summon_minion(GuardBot)
			friendly_minions.warband.insert(j + 1, guard_bot)


# summoned:
class DamagedGolem(Card):
	def __init__(self):
		super().__init__(name="Damaged Golem", attack_value=2, health=1, tier=1, 
						m_type=MinionType.MECH)


class GuardBot(Card):
	def __init__(self):
		super().__init__(name="Guard Bot", attack_value=2, health=3, tier=1, 
						m_type=MinionType.MECH, taunt=True)	


class JoEBot(Card):
	def __init__(self):
		super().__init__(name="Jo-E Bot", attack_value=1, health=1, tier=1, 
						m_type=MinionType.MECH)


class Robosaur(Card):
	def __init__(self):
		super().__init__(name="Robosaur", attack_value=8, health=8, tier=1, 
						m_type=MinionType.MECH)