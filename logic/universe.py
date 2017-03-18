import constants
from player import Player
from planet import Planet


class Universe(object):
    def __init__(self):
        self.n_galaxies = constants.UNIVERSE['n_galaxies']
        self.galaxies = []

        self.players = []

        self.trader = Trader()

        for i in xrange(self.n_galaxies):
            self.galaxy = Galaxy({'galaxy': i})
            self.galaxies.append(self.galaxy)

    def create_player(self, name):
        planet = self.find_a_planet()
        self.players.append(Player(name, planet))

    def find_a_planet(self):
        for g in self.galaxies:
            for ps in g.planetary_systems:
                for p in ps.planets:
                    if not p.run:
                        return p

    def coordinates2planet(self, coordinates):
        for g in self.galaxies:
            for ps in g.planetary_systems:
                for p in ps.planets:
                    if p.coordinates == coordinates:
                        return p


class Galaxy(object):
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.n_planetary_system = 9
        self.planetary_systems = []
        for i in xrange(self.n_planetary_system):
            coord = self.coordinates
            coord['planetary_systems'] = i
            self.planetary_systems.append(PlanetarySystem(coord))


class PlanetarySystem(object):
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.n_planets = 5
        self.planets = []
        for i in xrange(self.n_planets):
            coord = self.coordinates
            coord['planet'] = i
            self.planets.append(Planet(coord))


# to control all market's offers and do his own offers
class Trader(object):
    def __init__(self):
        self.ratios = constants.TRADER['ratios']
        self.profit = constants.TRADER['profit']
        self.offers = {}

    # his own offers
    # resource_send, resource_receive = 'wood', 'food'
    def calculate_ratio(self, resource_send, resource_receive):
        return (1 + self.profit) * self.ratios[resource_send] / self.ratios[resource_receive]

    # resource = 1000
    def calculate_receive(self, resource_send, ratio=None):
        if ratio is None:
            ratio = self.calculate_ratio(resource_send, resource_send)
        return float(resource_send) / ratio
