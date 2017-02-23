import constants


class Battle(object):
    def __init__(self, attacking_fleet, planet):
        self.attacker = attacking_fleet
        self.defender = Forces(dict(planet.hangar.spaceships, **planet.defenses)
        self.n_rounds = constants.N_ROUNDS

    def calc_damage(self):
        self.attacker.damage = self.attacker.attack - self.defender.shield
        self.defender.damage = self.defender.attack - self.attacker.shield

    def calc_rate_destried(self):
        self.defender.rate_destroied = 1. * self.attacker.damage / self.defender.structure
        self.attacker.rate_destroied = 1. * self.defender.damage / self.attacker.structure

    def apply_damage(self):
        for spaceship in self.attacker.fleet:
            spaceship.n *= self.attacker.rate_destroied
        for machine in self.defender.forces:
            machine.n *= self.defender.rate_destroied

    def rounds(self):
        if self.n_rounds > 0:
            self.calc_damage()
            self.calc_rate_destried()
            self.apply_damage()
            self.n_rounds = -1
            self.rounds()
        else:
            self.attacker.flight_back()
