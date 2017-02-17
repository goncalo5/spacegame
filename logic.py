from database import *
from constants import *


class Resources(object):
    def __init__(self, name, total, per_s, rate_per_s):
        self.l_total = self.l_per_s = None
        self.name = name
        self.total = total
        self.per_s = per_s
        self.rate_per_s = rate_per_s


class Buildings(object):
    def __init__(self, i, lv, left, evol,
                 name, cost, rate_cost, time, rate_t):
        self.i = i
        self.l_lv = self.l_cost = self.l_t = None

        # constants
        self.NAME = name
        self.COST = cost
        self.RATE_COST = rate_cost
        self.T = time
        self.RATE_T = rate_t

        # variables
        self.lv = lv  # level
        self.cost = self.COST * self.RATE_COST**self.lv
        self.t = self.T * self.RATE_T**self.lv
        self.evol = evol
        self.left = left
