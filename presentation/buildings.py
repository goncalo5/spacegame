from Tkinter import *
import time


class Buildings(object):
    def __init__(self, universe, planet, presentation, root, row_i=0, column_i=0):
        self.universe, self.planet, self.presentation, self.root, self.i, self.j \
            = universe, planet, presentation, root, row_i, column_i
        t = []
        t.append(time.time())
        self.planet = planet
        self.presentation = presentation

        self.header = BuildingsHeader(self.presentation.menu.f_buildings, planet, row_i, column_i)
        self.fill = BuildingsFill(planet, presentation, self.header, row_i + self.header.n_rows, column_i)
        t.append(time.time())
        for i in xrange(len(t) - 1):
            pass
            #print t[i + 1] - t[i],
        #print t[-1] - t[0]


class BuildingsHeader(object):
    def __init__(self, root, planet, row_i, column_i):
        self.root = root
        # initiate planet
        self.planet = planet

        self.l = row_i  # upper Header row
        self.c = column_i  # initial Header column
        self.n_rows = 2
        Label(self.root, text='Building').grid(row=self.l, column=self.c, rowspan=2)
        Label(self.root, text='Level').grid(row=self.l, column=self.c + 1, rowspan=2)

        # initial costs column
        self.c_costs = self.c + 2
        Label(self.root, text='evolving cost'). \
            grid(row=self.l, column=self.c_costs, columnspan=self.planet.n_resources)
        for n, r in enumerate(self.planet.resources):
            # costs
            Label(self.root, text=r.name).grid(row=self.l + 1, column=self.c_costs + n)
        # Column of construction times
        self.c_t = self.c_costs + self.planet.n_resources
        Label(self.root, text='Time'). \
            grid(row=self.l, column=self.c_t, rowspan=2)
        # evolving column
        self.c_evol = self.c_t + 1
        Label(self.root, text='Evolve').\
            grid(row=self.l, column=self.c_evol, rowspan=2)


class BuildingsFill(object):
    def __init__(self, planet, presentation, header, row_i, column_i):
        # initiate planet
        self.planet = planet
        self.presentation = presentation
        self.root = self.presentation.menu.f_buildings
        self.header = header

        for n, building in enumerate(self.planet.buildings):
            l = row_i + n
            Label(self.root, text=building.name). \
                grid(row=l, column=column_i)
            # Level
            building.l_lv = Label(self.root, text=building.level)
            building.l_lv.grid(row=l, column=column_i + 1)
            # evolving cost
            building.l_cost = {}
            for i, resource in enumerate(self.planet.resources.list):  # r = resource name
                text = building.cost[i]
                building.l_cost[i] = Label(self.root, text=int(text))
                building.l_cost[i].grid(row=l, column=column_i + i + 2)
            building.l_t = Label(self.root, text=int(building.time))
            building.l_t.grid(row=l, column=column_i + 2 + self.planet.resources.n)

        self.updating()

        # create buttons
        l = self.header.l + 2
        self.b_buildings = []
        for i, building in enumerate(self.planet.buildings):
            self.b_buildings.append(
                Button(self.root, text=building.kind, command=lambda b=building: self.evolve_building(b)))
            self.b_buildings[-1].grid(row=l + i, column=self.header.c_evol)

        self.presentation.resources.updating()

    def evolve_building(self, building):
        print building.name, building.left
        self.planet.evolve_building(building)
        self.update(building)

    def update(self, building):
        building.l_lv['text'] = int(building.level)
        for i, resource in enumerate(self.planet.resources.list):  # r = resource name
            building.l_cost[i]['text'] = int(building.cost[i])
            #getattr(building.l_cost, r)['text'] = int(getattr(building.cost, r))
        building.l_t['text'] = int(building.left)

        #building.l_lv['text'] = int(building.level)
        #building.l_cost['text'] = int(building.cost)
        #building.l_t['text'] = int(building.left)

    def update_all(self):
        for building in self.planet.buildings:
            self.update(building)

    def updating(self):
        self.update_all()
        self.root.after(1000, self.updating)