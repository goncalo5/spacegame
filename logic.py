import time
from database import *
from constants import *


class Buildings(object):
    def __init__(self, name):
        # constants
        self.name = name
        self.cost = 10
        self.rate_cost = 1.5
        self.time = time
        self.rate_t = 1.2

        # variables
        self.evol = evol
        self.left = left

        self.see_level_in_db()

    def calculate_cost(self):
        self.cost = self.COST * self.RATE_COST**self.lv

    def calculate_time2build(self):
        self.t = self.T * self.RATE_T**self.lv

    # Data Base
    # GET
    def see_level_in_db(self):
        self.level = RESOURCES[self.name]['level']


class Resources(Buildings):
    def __init__(self):
        self.name = name

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
        self.total = RESOURCES[self.name]['total']

    # PUT
    def save_total_in_db(self):
        RESOURCES[self.name.upper()] = self.total

    def updating_total_in_db(self):
        self.save_total_in_db()
        time.sleep(TIME2UPDATE_DB)
        self.updating_total_in_db()

