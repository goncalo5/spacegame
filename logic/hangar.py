import constants
from buildings import Building
from forces import Fleet
from machines import SpaceShip


# where de the spaceships is built and stored
class Hangar(Building):
    def __init__(self, name):
        super(Hangar, self).__init__(name)
        self.spaceships = {}
        for i, spaceship in enumerate(constants.SPACESHIPS):
            new = SpaceShip(spaceship['name'])
            self.spaceships[new.name] = new
        self.fleet = {}

    def build_spaceships(self, name, number=1):
        self.spaceships[name].n += number

    def destroy_spaceships(self, name, number=1):
        self.spaceships[name].n -= number

    def create_fleet(self, num_of_spaceships):
        # num_of_spaceships = {'light_fighter': 1...}
        for spaceship in self.spaceships:
            num = num_of_spaceships[spaceship.name]
            spaceship.n -= num
            spaceship_fleet = SpaceShip(spaceship.name)
            spaceship_fleet.n = num
            self.fleet[spaceship.name] = spaceship_fleet
        self.fleet = Fleet(self.fleet)

    def delete_fleet(self):
        self.fleet = {}
