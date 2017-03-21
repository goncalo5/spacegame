class Player(object):
    def __init__(self, name, planet):
        self.name = name
        self.points = 0
        planet.run = True
        planet.empty = False
        # Buildings
        # create buildings's objects
        planet.create_buildings_objects()
        # Resources
        # create resources's objects
        planet.create_resources_objects()
        # Spaceships
        # create spaceship's objects
        planet.create_spaceships_objects()
        planet.updating_total()
        self.planets = [planet]
