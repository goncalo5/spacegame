import database
import constants


class Building(object):
    def __init__(self, name):
        # initiate variables
        self.name = name
        self.type = constants.BUILDINGS[self.name]['type']
        # get constants
        self.cost_lv0 = constants.BUILDINGS[self.name]['cost']
        self.rate_cost = constants.BUILDINGS[self.name]['rate_cost']
        self.time_lv0 = constants.BUILDINGS[self.name]['time']
        self.rate_time = constants.BUILDINGS[self.name]['rate_time']
        # Null variables
        self.level = None
        self.cost  = None
        self.time = None
        self.metal = None

        # initial methods
        self.see_level_in_db()
        self.see_metal_in_db()

        self.calculate_cost()
        self.calculate_time2build()

        #
        self.is_evolving = False
        self.left = self.time

    # Data Base
    # GET
    def see_level_in_db(self):
        self.level = database.BUILDINGS[self.name]['level']

    def see_metal_in_db(self):
        self.metal = database.RESOURCES['metal']

    # calculators
    def calculate_cost(self):
        self.cost = self.cost_lv0 * self.rate_cost**self.level

    def calculate_time2build(self):
        self.time = self.time_lv0 * self.rate_time**self.level


class Mine(Building):
    def __init__(self, name, resource):
        super(Mine, self).__init__(name)
        self.resource = resource

    def update_per_s(self):
        self.resource.per_s = self.resource.per_s0 * self.resource.rate_per_s ** self.level


class Factory(Building):
    def __init__(self, name):
        super(Factory, self).__init__(name)
        self.factor0 = constants.BUILDINGS[self.name]['factor']
        self.rate_factor = constants.BUILDINGS[self.name]['rate_factor']
        self.factor = None

    def calculate_factor(self):
        # level - 1, because it's a inverso
        self.factor = 1. / (self.factor0 * self.rate_factor ** (self.level - 1))


class Storage(Building):
    def __init__(self, name, resource):
        super(Storage, self).__init__(name)
        self.name = name
        self.resource = resource
        self.capacity = self.capacity0 = constants.BUILDINGS[self.name]['capacity']
        self.rate_capacity = constants.BUILDINGS[self.name]['rate_capacity']

    def is_full(self):
        return self.resource.total > self.capacity

    def update_storage_capacity(self):
        self.capacity = self.capacity0 * self.rate_capacity ** self.level

    def check_storage(self):
        if self.is_full():
            self.resource.total = self.capacity
