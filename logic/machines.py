import constants


class Machine(object):
    def __init__(self, name, cost, attack, shield):
        self.name = name
        self.cost = cost
        self.n = 0  # number of machines
        self.attack = attack
        self.shield = shield
        self.structure = 0
        self.time2build = 5  # constants.SPACESHIPS[self.name]['time2built']
        self.calculate_structure()

    def calculate_structure(self):
        self.structure = sum(self.cost[:2])


class SpaceShip(Machine):
    def __init__(self, name, cost, attack, shield, speed, cargo_capacity, fuel_usage, engine):
        super(SpaceShip, self).__init__(name, cost, attack, shield)
        self.speed = speed
        self.cargo_capacity = cargo_capacity
        self.fuel_usage = fuel_usage
        self.engine = Engine(engine)

    def calculate_speed(self):
        self.speed = self.engine.power / self.structure


class Defense(Machine):
    def __init__(self, name, cost, attack, shield):
        super(Defense, self).__init__(name, cost, attack, shield)


class Engine(object):
    def __init__(self, name, power):
        self.name = name
        self.power = power
