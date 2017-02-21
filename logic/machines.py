import constants


class Machine(object):
    def __init__(self, name):
        self.name = name
        self.attack = constants.SPACESHIPS[self.name]['attack']
        self.shield = constants.SPACESHIPS[self.name]['shield']
        self.structure = 0
        self.cost = constants.SPACESHIPS[self.name]['cost']
        self.time2build = 5  # constants.SPACESHIPS[self.name]['time2built']
        self.calculate_structure()

    def calculate_structure(self):
        for resource_cost in constants.SPACESHIPS[self.name]['cost']:
            self.structure += resource_cost


class SpaceShip(Machine):
    def __init__(self, name):
        super(SpaceShip, self).__init__(name)
        self.cargo_capacity = constants.SPACESHIPS[self.name]['cargo_capacity']
        self.speed = None
        self.engine = Engine(constants.SPACESHIPS[self.name]['motor'])

    def calculate_speed(self):
        self.speed = self.engine.power / self.structure


class Defense(Machine):
    def __init__(self, name):
        super(Defense, self).__init__(name)


class Engine(object):
    def __init__(self, name):
        self.name = name
        self.power = constants.ENGINE[self.name]
