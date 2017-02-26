import constants


class Flight(object):
    def __init__(self, fleet, planet, target_planet):
        self.fleet = fleet
        self.planet = planet
        self.target_planet = target_planet
        self.distance = 0.
        self.calc_distance()
        self.left = self.distance / self.fleet.speed

    def flight_loop(self):
        while self.left

    def calc_distance(self):
        self.distance = max(
            abs(self.target_planet.coordinates['galaxy'] - self.planet.coordinates['galaxy']) * constants.DISTANCES['GALAXIES'],
            abs(self.target_planet.coordinates['planetary_system'] - self.planet.coordinates['planetary_system']) * constants.DISTANCES['PLANETARYSYSTEMS'],
            abs(self.target_planet.coordinates['planet'] - self.planet.coordinates['planet']) * constants.DISTANCES['PLANETS'])
