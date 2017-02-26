from Tkinter import *


class Fill(object):
    def __init__(self, root, planet, resources, header, row_i, column_i):
        self.root = root
        # initiate planet
        self.planet = planet
        self.resources = resources
        self.header = header

        for n, building in enumerate(self.planet.buildings):
            l = row_i + n
            Label(self.root, text=building.name). \
                grid(row=l, column=column_i)
            # Level
            building.l_lv = Label(self.root, text=building.level)
            building.l_lv.grid(row=l, column=column_i + 1)
            # evolving cost
            building.l_cost = Label(self.root, text=int(building.cost))
            building.l_cost.grid(row=l, column=column_i + 2)
            # evolving time
            building.l_t = Label(self.root, text=int(building.time))
            building.l_t.grid(row=l, column=column_i + 2 + self.planet.n_resources)
            # evolving

        self.updating()

        # create buttons
        l = self.header.l + 2
        self.b_buildings = []
        for i, building in enumerate(self.planet.buildings):
            self.b_buildings.append(
                Button(self.root, text=building.type, command=lambda b=building: self.evolve_building(b)))
            self.b_buildings[-1].grid(row=l + i, column=self.header.c_evol)

        self.resources.updating()

    def evolve_building(self, building):
        self.planet.evolve_building(building)
        self.update(building)

    def update(self, building):
        self.fill.update(building)
        self.resources.update_all()

    def quit(self):
        self.planet.save()
        self.planet.metal.total = 40
        self.planet.run = False
        self.root.destroy()

    def update(self, building):
        building.l_lv['text'] = int(building.level)
        building.l_cost['text'] = int(building.cost)
        building.l_t['text'] = int(building.left)

    def update_all(self):
        for building in self.planet.buildings:
            self.update(building)

    def updating(self):
        self.update_all()
        self.root.after(1000, self.updating)
