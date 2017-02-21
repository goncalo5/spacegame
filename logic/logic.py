import time
import threading
# import constants
from buildings import Building, Mine, Factory
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
        self.metal_mine = Mine('metal_mine', self.metal)
        self.robot_factory = Factory('robot_factory')
        self.buildings = [self.metal_mine, self.robot_factory]
        self.mines = [self.metal_mine]
        self.factories = [self.robot_factory]

        self.run = True
        self.is_evolving = False  # just 1 building at the same time
        # start updating resources
        up_total = threading.Timer(interval=1, function=self.updating_total)
        up_total.start()

    def update_per_s(self, building):
        if building in self.mines:
            for mine in self.mines:
                mine.update_per_s()

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
            #print 'evolve building, time before:', building.time
            self.loop_evolve(building)  # time to built
            #print 'evolve building, time after:', building.time

    def check_if_can_evolve(self, building):
        #print 'check...'
        if not self.is_evolving:
            #print '\n nao esta a evoluir nada neste momento', self.is_evolving
            if self.metal >= building.cost and not building.is_evolving:
                return True
        else:
            pass

    def take_resources2evolve(self, building):
        self.metal.total -= building.cost
        building.evolving = True

    def up1level(self, building):
        building.level += 1
        building.calculate_cost()
        self.update_times(building)
        self.update_per_s(building)

    def update_times(self, building):
        if building in self.factories:
            self.update_all_times()
        else:
            #print 'i m not a factory'
            self.update_time(building)

    def update_time(self, building):
        print 'time...', building.time, 'level:', building.level
        time = 1
        building.calculate_time2build()
        time *= building.time
        #print 'time:', time, 'level:', building.level
        for f in self.factories:
            f.calculate_factor()
            time *= f.factor
        building.time = time
        #print 'update time', building.time

    def update_all_times(self):
        for b in self.buildings:
            #print b.name, b.time
            self.update_time(b)
            b.left = b.time
            #print b.name, b.time


    def loop_evolve(self, building):
        self.is_evolving = building.is_evolving = True
        #print 'loop evolve: left:', building.left
        print 'loop_evolve, per s', self.metal.per_s
        if building.evolving:
            building.left -= 1
            if building.left <= 0:
                building.left = building.time
                self.is_evolving = building.is_evolving = False
                #print 'time defore:', building.time
                self.up1level(building)
                #print 'time after:', building.time
                building.left = building.time
                print 'loop_evolve, per s', self.metal.per_s
                return
            t = threading.Timer(interval=1, function=self.loop_evolve, kwargs={'building': building})
            t.start()

    def save(self):
        self.run =  False
