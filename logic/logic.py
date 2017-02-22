import threading
# import constants
from universe import  Universe, Galaxy, PlanetarySystem
from buildings import Building, Mine, Factory, Storage
from resources import Resource


class Logic(object):
    def __init__(self):
        print 'Logic\n'

        # new Universe
        self.universe = Universe()
