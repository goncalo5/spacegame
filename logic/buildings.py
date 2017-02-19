import database
import constants


class Building(object):
    def __init__(self, name):
        # initiate variables
        self.name = name
        # Null variables
        self.level = None
        self.cost = self.cost_lv0 = self.rate_cost = None
        self.time_lv0 = self.rate_time = self.time = None
        self.metal = None

        # initial methods
        self.see_level_in_db()
        self.see_metal_in_db()

        self.calculate_cost()
        self.calculate_time2build()

        #
        self.evolving = False
        self.left = self.time

    # Data Base
    # GET
    def see_level_in_db(self):
        self.level = database.BUILDINGS[self.name]['level']

    def see_metal_in_db(self):
        self.metal = database.RESOURCES['metal']

    # calculators
    def calculate_cost(self):
        self.cost_lv0 = constants.BUILDINGS[self.name]['cost']
        self.rate_cost = constants.BUILDINGS[self.name]['rate_cost']
        self.cost = self.cost_lv0 * self.rate_cost**self.level

    def calculate_time2build(self):
        self.time_lv0 = constants.BUILDINGS[self.name]['time']
        self.rate_time = constants.BUILDINGS[self.name]['rate_time']
        self.time = self.time_lv0 * self.rate_time**self.level


class Mine(Building):
    def __init__(self, name):
        super(Mine, self).__init__(name)
        self.rate_per_s = None

    def calculate_rate_per_s(self):
        self.rate_per_s = 1.5
