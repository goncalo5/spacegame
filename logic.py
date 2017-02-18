import time
import threading
import database
import constants


class Logic(object):
    def __init__(self):
        # Resources
        # create resources's objects
        self.metal = Resources('metal')
        self.resources = [self.metal]

        # Buildings
        # create buildings's objects
        self.metal_mine = Buildings('metal_mine')
        self.robot_factory = Buildings('robot_factory')
        self.buildings = [self.metal_mine, self.robot_factory]
        self.mines = [self.metal_mine]

        # start updating resources
        self.p_updating_metal = threading.Thread(target=self.updating_total)
        self.p_updating_metal.start()

    def updating_total(self):
        #print self.metal.total
        self.metal.total += self.metal.per_s
        time.sleep(1)
        self.updating_total()

    def evolve_building(self, building):
        self.check_if_can_evolve(building)
        self.take_resources2evolve(building)
        self.loop_evolve(building)  # time to built
        self.up1level(building)
        building.calculate_cost()
        building.calculate_time2build()
        self.metal.calculate_per_s()

    def check_if_can_evolve(self, building):
        if self.metal >= building.cost and not building.evolving:
            return True

    def take_resources2evolve(self, building):
        self.metal.total -= building.cost
        building.evolving = True

    def up1level(self, building):
        building.level += 1

    def loop_evolve(self, building):
        if building.evolving:
            building.left -= 1
            if building.left <= 0:
                building.left = building.time
                building.evolving = False
                return
            time.sleep(1)
            self.loop_evolve(building)


class Resources(object):
    def __init__(self, name):
        self.name = name

        # Null variables
        self.total = None
        self.per_s = None

        # initial methods
        self.see_total_in_db()
        self.calculate_per_s()

    # calculators
    def calculate_per_s(self):
        self.per_s = 1

    # Data Base
    # GET
    def see_total_in_db(self):
        self.total = database.RESOURCES[self.name]

    # PUT
    def save_total_in_db(self):
        database.BUILDINGS[self.name]['total'] = self.total

    def updating_total_in_db(self):
        self.save_total_in_db()
        time.sleep(constants.TIME2UPDATE_DB)
        self.updating_total_in_db()


class Buildings(object):
    def __init__(self, name):
        # initiate variables
        self.name = name
        # Null variables
        self.level = None
        self.cost = self.cost_lv0 = self.rate_cost = None
        self.time_lv0 = self.rate_time = self.time = None
        self.metal = None

        # initial methods
        self.see_level_in_db()
        self.see_metal_in_db()

        self.calculate_cost()
        self.calculate_time2build()

        #
        self.evolving = False
        self.left = self.time

    # Data Base
    # GET
    def see_level_in_db(self):
        self.level = database.BUILDINGS[self.name]['level']

    def see_metal_in_db(self):
        self.metal = database.RESOURCES['metal']

    # calculators
    def calculate_cost(self):
        self.cost_lv0 = constants.BUILDINGS[self.name]['cost']
        self.rate_cost = constants.BUILDINGS[self.name]['rate_cost']
        self.cost = self.cost_lv0 * self.rate_cost**self.level

    def calculate_time2build(self):
        self.time_lv0 = constants.BUILDINGS[self.name]['time']
        self.rate_time = constants.BUILDINGS[self.name]['rate_time']
        self.time = self.time_lv0 * self.rate_time**self.level


class Mines(Buildings):
    def __init__(self, name):
        super(Mines, self).__init__(name)
        self.rate_per_s = None

    def calculate_rate_per_s(self):
        self.rate_per_s = 1.5
