from flight import Flight

class Forces(object):
    def __init__(self, planet, forces):
        self.forces = forces
        self.attack = 0
        self.shield = 0
        self.structure = 0
        # null attributes
        self.damage = self.rate_destroyed = None

        for machine in self.forces:
            self.attack += machine.attack * machine.n
            self.shield += machine.shield * machine.n
            self.structure += machine.structure * machine.n


class Fleet(Forces):
    def __init__(self, planet, forces, universe):
        super(Fleet, self).__init__(planet, forces)
        self.universe = universe
        self.planet = planet
        self.fleet = forces
        self.speed = 0

    def calc_speed(self):
        for spaceship in self.fleet:
            if spaceship.speed > self.speed:
                self.speed = spaceship.speed

    def start_flight(self, coordinates_target_planet):
        target_planet = self.universe.coordinates2planet(coordinates_target_planet)
        Flight(fleet=self, planet=self.planet, target_planet=target_planet)

    def flight_back(self):
        pass
