import time
import threading
# import constants
from buildings import Building, Mine
from resources import Resource


class Logic(object):
    def __init__(self):
        print 'Logic\n'
        # Resources
        # create resources's objects
        self.metal = Resource('metal')
        self.resources = [self.metal]
        self.n_resources = len(self.resources)

        # Buildings
        # create buildings's objects
        self.metal_mine = Mine('metal_mine')
        self.robot_factory = Building('robot_factory')
        self.buildings = [self.metal_mine, self.robot_factory]
        self.mines = [self.metal_mine]

        self.run = True
        self.is_evolving = False  # just 1 building at the same time
        # start updating resources
        up_total = threading.Timer(interval=1, function=self.updating_total)
        up_total.start()

    def updating_total(self):
        #print threading.active_count()
        #print 'updating_total:', self.metal.total, self.metal.per_s, self.run
        self.metal.total += self.metal.per_s
        if self.run:
            #print 'esta a entrar'
            t = threading.Timer(interval=1, function=self.updating_total)
            t.start()

    def evolve_building(self, building):
        if self.check_if_can_evolve(building):
            self.take_resources2evolve(building)
            self.loop_evolve(building)  # time to built
            self.up1level(building)

    def check_if_can_evolve(self, building):
        print 'check...'
        if not self.is_evolving:
            print '\n nao esta a evoluir nada neste momento', self.is_evolving
            if self.metal >= building.cost and not building.is_evolving:
                return True
        else:
            print '\n\n\nainda esta a evoluir', self.is_evolving, building.is_evolving

    def take_resources2evolve(self, building):
        self.metal.total -= building.cost
        building.evolving = True

    def up1level(self, building):
        building.level += 1
        building.calculate_cost()
        building.calculate_time2build()
        self.metal.calculate_per_s()

    def loop_evolve(self, building):
        self.is_evolving = building.is_evolving = True
        print building.left
        if building.evolving:
            building.left -= 1
            if building.left <= 0:
                building.left = building.time
                self.is_evolving = building.is_evolving = False
                return
            t = threading.Timer(interval=1, function=self.loop_evolve, kwargs={'building': building})
            t.start()

    def save(self):
        self.run =  False
