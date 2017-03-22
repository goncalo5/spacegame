from Tkinter import *


class Resources(object):
    def __init__(self, root, planet, row_i, column_i):
        self.root = root
        # initiate planet
        self.planet = planet
        n_resources = self.planet.resources.n

        # Available Resources
        # header
        Label(self.root, text='resource').grid(row=row_i, column=column_i)
        Label(self.root, text='Total').grid(row=row_i + 1, column=column_i)
        Label(self.root, text='per sec').grid(row=row_i + 2, column=column_i)
        # fill
        for n, resource in enumerate(self.planet.resources):
            Label(self.root, text=resource.name).grid(row=row_i, column=column_i + 1 + n)
            resource.l_total = Label(self.root, text=resource.total)
            resource.l_total.grid(row=row_i + 1, column=column_i + 1 + n)
            resource.l_per_s = Label(self.root, text=resource.per_s)
            resource.l_per_s.grid(row=row_i + 2, column=column_i + 1 + n)

        self.updating()

    def update_resource(self, resource):
        resource.l_total['text'] = int(resource.total)
        resource.l_per_s['text'] = int(resource.per_s)

    def update_all(self):
        for resource in self.planet.resources:
            self.update_resource(resource)

    def updating(self):
        if self.planet.run:
            self.update_all()
            self.root.after(1000, self.updating)


class MenuResources(object):
    def __init__(self, planet, root, resources, row_i=0, column_i=0):
        self.planet, self.root, self.resources, self.i, self.j \
            = planet, root, resources, row_i, column_i
        self.create_header()
        self.create_fill()

    def create_header(self):
        for i, resource in enumerate(self.planet.resources.list):
            Label(master=self.root, text=resource.name).grid(row=self.i, column=self.j + i + 1)

    def create_fill(self):
        Label(master=self.root, text='Basic').grid(row=self.i + 1, column=self.j)
        for i, resource in enumerate(self.planet.resources):
            Label(master=self.root, text=resource.per_s0).grid(row=self.i + 1, column=self.j + i + 1)
        for i, resource_building in enumerate(self.planet.buildings.resource_buildings):
            Label(master=self.root, text=resource_building.name).grid(row=self.i + i + 2, column=self.j)
            for j, resource in enumerate(self.planet.resources):
                Label(master=self.root, text=resource_building.per_s[j]).grid(row=self.i + i + 2, column=self.j + j + 1)
