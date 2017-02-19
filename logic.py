import time
import threading
import constants
from buildings import Building, Mine
from resources import Resource


class Logic(object):
    def __init__(self):
        # Resources
        # create resources's objects
        self.metal = Resource('metal')
        self.resources = [self.metal]

        # Buildings
        # create buildings's objects
        self.metal_mine = Mine('metal_mine')
        self.robot_factory = Building('robot_factory')
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
