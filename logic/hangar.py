import constants
from buildings import Building
from machines import SpaceShip


# where de the spaceships is built and stored
class Hangar(Building):
    def __init__(self, name):
        super(Hangar, self).__init__(name)
        self.spaceships = {}
        for i, spaceship in enumerate(constants.SPACESHIPS):
            new = SpaceShip(spaceship)
            self.spaceships(spaceship)[new.name] = new
            self.spaceships[new.name].n = 0

    def build_spaceship(self, name, number=1):
        self.spaceships[name].n += number

    def destroy_spaceships(self, name, number=1):
        self.spaceships[name].n -= number

