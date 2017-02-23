class Forces(object):
    def __init__(self, forces):
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

    def start_flight(self, target_planet):
        pass

    def flight_back(self):
        pass


class Fleet(Forces):
    def __init__(self, fleet):
        super(Fleet, self).__init__(self)
        self.fleet = fleet
        self.speed = 0

    def calc_speed(self):
        for spaceship in self.fleet:
            if spaceship.speed > self.speed:
                self.speed = spaceship.speed