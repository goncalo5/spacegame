class Player(object):
    def __init__(self, name, planet):
        self.name = name
        self.points = 0
        planet.run = True
        planet.empty = False
        planet.updating_total()
        self.planets = [planet]
