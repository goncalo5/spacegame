import functions


class Resources(object):
    def __init__(self, planet, resources_list):
        self.planet = planet
        self.list = []
        self.dictionary = {}
        self.n = None
        self.create_resources_objects(resources_list)

    def create_resources_objects(self, resources_list):
        for resource in resources_list:
            self.add_resource(resource)
        self.n = len(self.list)

    def add_resource(self, resource):
        self.list.append(Resource(self.planet, **resource))
        new = self.list[-1]
        self.__dict__[functions.transform_name(new.name)] = new
        self.dictionary[new.name] = new

    def updating_total(self):
        for resource in self.list:
            resource.dynamic += resource.per_s
            resource.total = resource.static + resource.dynamic

    def update_total(self):
        for resource in self.list:
            resource.update_total()

    def update_per_s(self):
        for resource in self.list:
            resource.update_per_s()

    def __iter__(self):
        return iter(self.list)


class Resource(object):
    def __init__(self, planet, index, name, total):
        self.planet = planet
        self.index = index
        self.name = name
        # static resource: resources that only change when a new building/spaceship is constructed/evolved
        self.static = 0
        # dynamic resource: resources that change over time (affected by per s)
        self.dynamic = total
        self.total = self.static + self.dynamic

        # Null variables
        self.per_s0 = 0
        self.per_s = self.rate_per_s = None

        # initial methods
        self.calculate_per_s0()
        self.update_per_s()
        self.update_total()
        self.see_total_in_db()

    def calculate_per_s0(self):
        for building in self.planet.buildings.resource_buildings:
            per_s0 = building.earned_resources['per_s0'][self.index]
            # create total per_s0 for each resource
            self.per_s0 += per_s0

    def update_per_s(self):
        self.per_s = 0
        for building in self.planet.buildings.resource_buildings:
            per_s = building.per_s[self.index]
            # create total per_s for each resource
            self.per_s += per_s

    def update_total(self):
        self.static = 0
        for building in self.planet.buildings.resource_buildings:
            self.static += \
                building.earned_resources['total0'][self.index] +\
                building.earned_resources['total1'][self.index] *\
                building.earned_resources['rate_total'][self.index] **\
                building.level - \
                building.earned_resources['total1'][self.index]
        self.total = self.static + self.dynamic


    # Data Base
    # GET
    def see_total_in_db(self):
        pass

    # PUT
    def save_total_in_db(self):
        pass

    def updating_total_in_db(self):
        pass
