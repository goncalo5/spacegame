import time
import database
import constants


class Resources(object):
    def __init__(self, name):
        self.name = name

        self.total = None


class Buildings(object):
    def __init__(self, name):
        # initiate variables
        self.name = name
        # Null variables
        self.level = None
        self.cost = self.cost_lv0 = self.rate_cost = None
        self.time_lv0 = self.rate_time = self.time = None

        # initial methods
        self.see_level_in_db()

        self.calculate_cost()
        self.calculate_time2build()

        #
        self.evolving = False

    # Data Base
    # GET
    def see_level_in_db(self):
        self.level = database.BUILDINGS[self.name]['level']

    # calculators
    def calculate_cost(self):
        self.cost_lv0 = constants.BUILDINGS[self.name]['cost']
        self.rate_cost = constants.BUILDINGS[self.name]['rate_cost']
        self.cost = self.cost_lv0 * self.rate_cost**self.level

    def calculate_time2build(self):
        self.time_lv0 = constants.BUILDINGS[self.name]['time']
        self.rate_time = constants.BUILDINGS[self.name]['rate_time']
        self.time = self.time_lv0 * self.rate_time**self.level

    # evolutions
    def evolve(self):
        self.check_if_can_evolve()
        self.take_resources2evolve()
        self.up1level()

    def check_if_can_evolve(self):
        if self.metal >= self.cost and not self.evolving:
            return True

    def take_resources2evolve(self):
        pass

    def up1level(self):
        pass


class Mines(Buildings):
    def __init__(self, name):
        super(Mines, self).__init__(name)
        # Null variables
        self.total = None
        self.per_s = self.rate_per_s = None

        # initial methods
        self.see_total_in_db()

    def updating_total(self):
        self.total += self.per_s
        time.sleep(1)
        self.updating_total()

    def calculate_per_s(self):
        self.per_s = 1

    def calculate_rate_per_s(self):
        self.rate_per_s = 1.5

    # Data Base
    # GET
    def see_total_in_db(self):
        self.total = database.BUILDINGS[self.name]['total']

    # PUT
    def save_total_in_db(self):
        database.BUILDINGS[self.name]['total'] = self.total

    def updating_total_in_db(self):
        self.save_total_in_db()
        time.sleep(constants.TIME2UPDATE_DB)
        self.updating_total_in_db()

