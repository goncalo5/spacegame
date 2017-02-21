from planet import  Planet

class Player(object):
    def __init__(self, name, planet):
        self.name = name
        self.points = 0
        self.planets = [planet]
