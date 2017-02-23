import constants


class Machine(object):
    def __init__(self, name):
        self.name = name
        self.n = 0  # number of machines
        self.attack = constants.MACHINES[self.name]['attack']
        self.shield = constants.MACHINES[self.name]['shield']
        self.structure = 0
        self.cost_metal = constants.MACHINES[self.name]['cost']['metal']
        self.cost_crystal = constants.MACHINES[self.name]['cost']['crystal']
        self.costs = [self.cost_metal, self.cost_crystal]
        self.time2build = 5  # constants.SPACESHIPS[self.name]['time2built']
        self.calculate_structure()

    def calculate_structure(self):
        for resource_cost in constants.MACHINES[self.name]['cost']:
            self.structure += constants.MACHINES[self.name]['cost'][resource_cost]


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
