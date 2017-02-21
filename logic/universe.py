import constants


class Universe(object):
    def __init__(self):
        self.n_galaxies = 9
        self.galaxies = []
        for i in xrange(self.n_galaxies):
            self.galaxy = Galaxy({'galaxy': i})
            self.galaxies.append(self.galaxy)


class Galaxy(object):
    def __init__(self, coordinates):
        self.galaxy.coordinates = coordinates
        self.n_planetary_system = 9
        self.planetary_systems = []
        for i in xrange(self.n_planetary_system):
            coord = self.galaxy.coordinates
            coord['planetary_systems'] = i
            self.planetary_systems.append(PlanetarySystem(coord))


class PlanetarySystem(objects):
    def __init__(self, coordinates):
        self.planetary_systems.coordinates = coordinates
        self.n_planets = 5
        self.planets = []
        for i in xrange(self.n_planets):
            coord = self.planetary_systems.coordinates
            coord['planet'] = i
            self.planets.append(Planet(coord))


class Planet(object):
    def __init__(self, star_distance):
        self.planet.coordinates = coordinates
        self.star_distance = self.coordinates['planet'] + 1
        self.total_fields = self.star_distance *
            constants.UNIVERSE['planets']['rate_field'] +
            constants.UNIVERSE['planets']['field']
        self.fields_left = self.n_fields
        self.fields_ocupided = 0
        self.defenses = {}
        for i, defense in enumerate(constants.DEFESENSES):
            new = Defense(defense)
            self.defenses[new.name] = new
            self.defense[new.name].n = 0

        def occupy1field(self):
            self.field_left -= 1
            self.fields_ocupided += 1

        def leave1field(self):
            self.field_left += 1
            self.fields_ocupided -= 1
