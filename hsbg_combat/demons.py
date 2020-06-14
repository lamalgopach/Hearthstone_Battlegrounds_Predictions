from minions import *


class AnnihilanBattlemaster(Card): 
	# bttlcry
	def __init__(self):
		super().__init__(name="Annihilan Battlemaster", attack_value=3, health=1, 
						tier=5, m_type=MinionType.DEMON)


class FiendishServant(Card):
	def __init__(self):
		super().__init__(name="Fiendish Servant", attack_value=2, health=1, tier=1, 
						m_type=MinionType.DEMON, has_deathrattle=True)
	
	def deathrattle(self, battle, status):
		friendly_minions = battle.attacking_player.warband if status == 1 else battle.attacked_player.warband

		if friendly_minions:
			friendly_random_minion = random.choice(friendly_minions)
			friendly_random_minion.attack_value += self.attack_value


class FloatingWatcher(Card):
	def __init__(self):
		super().__init__(name="Floating Watcher", attack_value=4, health=4, tier=4, 
						m_type=MinionType.DEMON)


class ImpGangBoss(Card):
	def __init__(self):
		super().__init__(name="Imp Gang Boss", attack_value=2, health=4, tier=3, 
						m_type=MinionType.DEMON, damage_effect=True)	

	def act_after_damage(self, battle, status):
		friendly_minions = battle.attacking_player.warband if status == 1 else battle.attacked_player.warband
		j = battle.attacking_player.attack_index if status == 1 else battle.attacked_player.attacked_minion
		if len(friendly_minions) < 7:
			imp = self.summon_minion(Imp)
			friendly_minions.insert(j + 1, imp)


class ImpMama(Card):
	def __init__(self):
		super().__init__(name="Imp Mama", attack_value=6, health=10, tier=6, 
						m_type=MinionType.DEMON, damage_effect=True)	

	def act_after_damage(self, battle, status):
		demons = [
			AnnihilanBattlemaster,
			FiendishServant, 
			FloatingWatcher,
			ImpGangBoss, 
			Imprisoner, 
			# Mal'Ganis, 
			NathrezimOverseer,
			# Siegebreaker,
			Voidlord, 
			VulgarHomunculus,
			]
		random_demon = random.choice(demons)
		friendly_minions = battle.attacking_player.warband if status == 1 else battle.attacked_player.warband
		j = battle.attacking_player.attack_index if status == 1 else battle.attacked_player.attacked_minion

		if len(friendly_minions) < 7:
			demon = self.summon_minion(random_demon)

			if not demon.taunt:
				demon.taunt = True

			friendly_minions.insert(j + 1, demon)


class Imprisoner(Card):
	def __init__(self):
		super().__init__(name="Imprisoner", attack_value=3, health=3, tier=2, 
						m_type=MinionType.DEMON, taunt=True, has_deathrattle=True)

	def deathrattle(self, battle, status):
		friendly_minions = battle.attacking_player.warband if status == 1 else battle.attacked_player.warband
		j = battle.attacking_player.attack_index if status == 1 else battle.attacked_player.attacked_minion

		imp = self.summon_minion(Imp)
		friendly_minions.insert(j, imp)



class NathrezimOverseer(Card):
	#btlcry
	def __init__(self):
		super().__init__(name="Nathrezim Overseer", attack_value=2, health=3, tier=2, 
						m_type=MinionType.DEMON)


class Voidlord(Card):
	def __init__(self):
		super().__init__(name="Voidlord", attack_value=3, health=9, tier=5, 
						m_type=MinionType.DEMON, taunt=True, has_deathrattle=True)

	def deathrattle(self, battle, status):
		friendly_minions = battle.attacking_player.warband if status == 1 else battle.attacked_player.warband
		j = battle.attacking_player.attack_index if status == 1 else battle.attacked_player.attacked_minion
		i = 0
		while len(friendly_minions) < 7 and i != 3:
			voidwalker = self.summon_minion(Voidwalker)
			friendly_minions.insert(j, voidwalker)
			i += 1

class VulgarHomunculus(Card):
	# add btlcry
	def __init__(self):
		super().__init__(name="VulgarHomunculus", attack_value=2, health=4, tier=1, 
						m_type=MinionType.DEMON, taunt=True)



# summoned:
class Imp(Card):
	def __init__(self):
		super().__init__(name="Imp", attack_value=1, health=1, tier=1, 
						m_type=MinionType.DEMON)


class Voidwalker(Card):
	def __init__(self):
		super().__init__(name="Voidwalker", attack_value=1, health=3, tier=1, 
						m_type=MinionType.DEMON, taunt=True)