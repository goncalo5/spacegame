import constants
from forces import Forces

class Battle(object):
    def __init__(self, attacking_fleet, planet):
        self.attacker = attacking_fleet
        self.defender = Forces(dict(planet.hangar.spaceships, **planet.defenses))
        self.n_rounds = constants.N_ROUNDS

    def calc_damage(self):
        self.attacker.damage = self.attacker.attack - self.defender.shield
        self.defender.damage = self.defender.attack - self.attacker.shield

    def calc_rate_destroyed(self):
        self.defender.rate_destroyed = 1. * self.attacker.damage / self.defender.structure
        self.attacker.rate_destroyed = 1. * self.defender.damage / self.attacker.structure

    def apply_damage(self):
        for spaceship in self.attacker.fleet:
            spaceship.n *= self.attacker.rate_destroyed
        for machine in self.defender.forces:
            machine.n *= self.defender.rate_destroyed

    def rounds(self):
        if self.n_rounds > 0:
            self.calc_damage()
            self.calc_rate_destroyed()
            self.apply_damage()
            self.n_rounds = -1
            self.rounds()
        else:
            self.attacker.flight_back()
