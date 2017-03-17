import database
import constants


class Buildings(object):
    def __init__(self, buildings_list):
        self.list = []
        self.dictionary = {}
        self.n = None
        self.create_buildings_objects(buildings_list)

    def create_buildings_objects(self, buildings_list):
        for building in buildings_list:
            self.add_building(building)
        self.n = len(self.list)

    def add_building(self, building):
        kinds = {'resource_building': ResourceBuilding,
                 'storage': Storage,
                 'factory': Factory,
                 'other': Building}
        self.list.append(kinds[building['kind']](**building))
        new = self.list[-1]
        self.__dict__[new.name] = new
        self.dictionary[new.name] = new

    def __iter__(self):
        return iter(self.list)


class Building(object):
    def __init__(self, name, kind, time, rate_time, cost, rate_cost):
        # initiate variables
        self.name, self.kind, self.time, self.rate_time, self.cost, self.rate_cost =\
            name, kind, time, rate_time, cost, rate_cost
        self.cost_lv0 = list(self.cost)  # list <=> copy
        self.rate_cost = self.rate_cost
        self.time_lv0 = self.time
        self.rate_time = self.rate_time
        self.level = 0

        # initial methods
        self.calculate_costs()
        self.calculate_time2build()

        #
        self.is_evolving = False
        self.left = self.time

    # Data Base
    # GET
    def see_level_in_db(self):
        self.level = database.BUILDINGS[self.name]['level']

    def see_metal_in_db(self):
        self.metal = database.RESOURCES['metal']

    # calculators
    def calculate_costs(self):
        cost =[]
        for i, cost_lv0 in enumerate(self.cost_lv0):
            cost.append(cost_lv0 * self.rate_cost[i]**self.level)
        self.cost = cost

    def calculate_time2build(self):
        self.time = self.time_lv0 * self.rate_time**self.level


class ResourceBuilding(Building):
    def __init__(self, name, kind, time, rate_time, cost, rate_cost, resource_gain):
        super(ResourceBuilding, self).__init__(name, kind, time, rate_time, cost, rate_cost)
        self.resource_gain = resource_gain


class Factory(Building):
    def __init__(self, name, kind, time, rate_time, cost, rate_cost, factor, rate_factor):
        super(Factory, self).__init__(name, kind, time, rate_time, cost, rate_cost)
        self.factor0 = factor
        self.rate_factor = rate_factor
        self.factor = None

    def calculate_factor(self):
        # level - 1, because it's a inverso
        self.factor = 1. / (self.factor0 * self.rate_factor ** (self.level - 1))


class Storage(Building):
    def __init__(self, name, kind, time, rate_time, cost, rate_cost, resource_storage):
        super(Storage, self).__init__(name, kind, time, rate_time, cost, rate_cost)
        self.name = name
        self.resource = resource_storage

    def is_full(self):
        return self.resource.total > self.capacity

    def update_storage_capacity(self):
        self.capacity = self.capacity0 * self.rate_capacity ** self.level

    def check_storage(self):
        if self.is_full():
            self.resource.total = self.capacity
