import threading
import constants
from resources import Resources
from buildings import Buildings, ResourceBuilding, Storage, Factory
from machines import Defense


class Planet(object):
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.empty = True
        self.star_distance = self.coordinates['planet'] + 1
        self.total_fields = self.star_distance * \
                            constants.UNIVERSE['planet']['rate_field'] + \
                            constants.UNIVERSE['planet']['fields']
        self.fields_left = self.total_fields
        self.fields_occupied = 0
        self.defenses = {}
        for i, defense in enumerate(constants.DEFENSES):
            new = Defense(**defense)
            self.defenses[new.name] = new
            self.defenses[new.name].n = 0

        # Buildings
        # create buildings's objects
        self.buildings = Buildings(constants.BUILDINGS)
        # Resources
        # create resources's objects
        self.resources = Resources(self, constants.RESOURCES)
        self.n_resources = len(constants.RESOURCES)

        self.run = False
        self.is_evolving = False  # just 1 building at the same time
        # start updating resources
        if not self.run and not self.empty:
            self.run = True
            self.updating_total()
        #up_total = threading.Timer(interval=1, function=self.updating_total)
        #up_total.start()

    def updating_total(self):
        for resource in self.resources.list:
            resource.total += resource.per_s
        if self.run:
            #self.storage.check_storage()
            t = threading.Timer(interval=1, function=self.updating_total)
            t.start()

        #self.metal.total += self.metal.per_s
        #if self.run:
        #   self.metal_storage.check_storage()
        #    t = threading.Timer(interval=1, function=self.updating_total)
        #    t.start()

    def evolve_building(self, building):
        if self.check_if_can_evolve(building):
            self.take_resources2evolve(building)
            self.loop_evolve(building)  # time to built

    def check_if_can_evolve(self, building):
        if not self.is_evolving:
            for i, resource in enumerate(self.resources):
                if resource.total < building.cost[i]:
                    return False
            return True

    def take_resources2evolve(self, building):
        for i, resource in enumerate(self.resources):
            resource.total -= building.cost[i]
        building.evolving = True

    def up1level(self, building):
        building.level += 1
        building.calculate_costs()
        self.update_per_s(building)  # for mines
        self.update_storage_capacity(building)  # for storages
        self.update_times(building)  # for factories

    # for mines
    def update_per_s(self, building):
        if building.kind == 'resource_building':
            for resource in self.resources:
                resource.update_per_s()

    # for storage
    def update_storage_capacity(self, building):
        if building.kind == 'storage':
            building.update_storage_capacity()

    # for factories
    def update_times(self, building):
        if building.kind == 'factory':
            self.update_all_times()
        else:
            self.update_time(building)

    def update_time(self, building):
        time = 1
        building.calculate_time2build()
        time *= building.time
        for building in self.buildings:
            if building.kind == 'factory':
                building.calculate_factor()
                time *= building.factor
        building.time = time

    def update_all_times(self):
        for b in self.buildings:
            self.update_time(b)
            b.left = b.time

    def loop_evolve(self, building):
        self.is_evolving = building.is_evolving = True
        if building.evolving:
            building.left -= 1
            if building.left <= 0:
                building.left = building.time
                self.is_evolving = building.is_evolving = False
                self.up1level(building)
                building.left = building.time
                return
            t = threading.Timer(interval=1, function=self.loop_evolve, kwargs={'building': building})
            t.start()

    def save(self):
        self.run = False

    def occupy1field(self):
        self.field_left -= 1
        self.fields_ocupided += 1

    def leave1field(self):
        self.field_left += 1
        self.fields_ocupided -= 1
