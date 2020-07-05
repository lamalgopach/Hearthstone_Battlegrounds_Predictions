from minions import *

class AnnoyoModule(Card):
	# add magnetic
	def __init__(self):
		super().__init__(name="Annoy-o-Module", attack_value=2, health=4, tier=4, 
						m_type=MinionType.MECH, taunt=True, has_ds=True)	


class FoeReaper4000(Card):
	def __init__(self):
		super().__init__(name="Foe Reaper 4000", attack_value=6, health=9, tier=6, 
						has_triggered_attack=True, m_type=MinionType.MECH)


class HarvestGolem(Card):
	def __init__(self):
		super().__init__(name="Harvest Golem", attack_value=2, health=3, tier=2, 
						m_type=MinionType.MECH, has_deathrattle=True)

	def deathrattle(self, battle, status):
		friendly_minions = battle.attacking_player.warband if status == 1 else battle.attacked_player.warband
		j = battle.attacking_player.dead_minions_dict[self] if status == 1 else battle.attacked_player.dead_minions_dict[self]
		golem = self.summon_minion(DamagedGolem, battle, status)
		friendly_minions.insert(j, golem)


class IronSensei(Card):
	def __init__(self):
		super().__init__(name="Iron Sensei", attack_value=2, health=2, tier=4, 
						m_type=MinionType.MECH)


class KaboomBot(Card):
	def __init__(self):
		super().__init__(name="Kaboom Bot", attack_value=2, health=2, tier=2, 
						m_type=MinionType.MECH, has_deathrattle=True)

	def deathrattle(self, battle, status):
		enemy_minions = battle.attacked_player.warband if status == 1 else battle.attacking_player.warband
		if enemy_minions:
			enemy_random_minion = random.choice(enemy_minions)
			st = 2 if status == 1 else 1
			enemy_random_minion.take_damage(4, self.poisonous, battle, st)

		if status == 1:
			battle.attacking_player.effects_causing_next_death.append(self)
		else:
			battle.attacked_player.effects_causing_next_death.append(self)


class MicroMachine(Card):
	# tbd; gain 
	def __init__(self):
		super().__init__(name="Micro Machine", attack_value=1, health=2, tier=1, 
						m_type=MinionType.MECH)

class MechanoEgg(Card):
	def __init__(self):
		super().__init__(name="Mechano-Egg", attack_value=0, health=5, tier=4, 
						m_type=MinionType.MECH, has_deathrattle=True)

	def deathrattle(self, battle, status):
		friendly_minions = battle.attacking_player.warband if status == 1 else battle.attacked_player.warband
		j = battle.attacking_player.dead_minions_dict[self] if status == 1 else battle.attacked_player.dead_minions_dict[self]
		robosaur = self.summon_minion(Robosaur, battle, status)
		friendly_minions.insert(j, robosaur)



class Mecharoo(Card):
	def __init__(self):
		super().__init__(name="Mecharoo", attack_value=1, health=1, tier=1, 
						m_type=MinionType.MECH, has_deathrattle=True)

	def deathrattle(self, battle, status):
		friendly_minions = battle.attacking_player.warband if status == 1 else battle.attacked_player.warband
		j = battle.attacking_player.dead_minions_dict[self] if status == 1 else battle.attacked_player.dead_minions_dict[self]
		joebot = self.summon_minion(JoEBot, battle, status)
		friendly_minions.insert(j, joebot)


class MetaltoothLeaper(Card):
	# add the btlcry
	def __init__(self):
		super().__init__(name="Metaltooth Leaper", attack_value=3, health=3, tier=2, 
						m_type=MinionType.MECH)


class PogoHopper(Card):
	# add the btlcry
	def __init__(self):
		super().__init__(name="Pogo-Hopper", attack_value=1, health=1, tier=2, 
						m_type=MinionType.MECH)


class ReplicatingMenace(Card):
	# add magnetic
	def __init__(self):
		super().__init__(name="Replicating Menace", attack_value=3, health=1, tier=3, 
						m_type=MinionType.MECH, has_deathrattle=True)

	def deathrattle(self, battle, status):
		friendly_minions = battle.attacking_player.warband if status == 1 else battle.attacked_player.warband
		j = battle.attacking_player.dead_minions_dict[self] if status == 1 else battle.attacked_player.dead_minions_dict[self]
		i = 0
		while len(friendly_minions) < 7 and i != 3:
			microbot = self.summon_minion(Microbot, battle, status)
			friendly_minions.insert(j, microbot)
			i += 1



class SecurityRover(Card):
	def __init__(self):
		super().__init__(name="Security Rover", attack_value=2, health=6, tier=4, 
						m_type=MinionType.MECH)

	def take_damage(self, damage, poisonous, battle, status):
		super().take_damage(damage, poisonous, battle, status)
		friendly_minions = battle.attacking_player.warband if status == 1 else battle.attacked_player.warband
		if self not in friendly_minions:
			j = battle.attacking_player.dead_minions_dict[self] if status == 1 else battle.attacked_player.dead_minions_dict[self]
		else:
			j = battle.attacking_player.warband.index(self) if status == 1 else battle.attacked_player.warband.index(self)
		if len(friendly_minions) < 7:
			guard_bot = self.summon_minion(GuardBot, battle, status)
			friendly_minions.insert(j + 1, guard_bot)



class ScrewjankClunker(Card):
	# add the btlcry
	def __init__(self):
		super().__init__(name="Screwjank Clunker", attack_value=2, health=5, tier=3, 
						m_type=MinionType.MECH)


class Zoobot(Card):
	#btlcry
	def __init__(self):
		super().__init__(name="Zoobot", attack_value=3, health=3, tier=2, 
						m_type=MinionType.MECH)

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


class Microbot(Card):
	def __init__(self):
		super().__init__(name="Microbot", attack_value=1, health=1, tier=1, 
						m_type=MinionType.MECH)


class Robosaur(Card):
	def __init__(self):
		super().__init__(name="Robosaur", attack_value=8, health=8, tier=1, 
						m_type=MinionType.MECH)