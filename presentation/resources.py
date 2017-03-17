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
            # always use after method in Tkinter
            #print self.planet.resources.energy
            #print self.planet.resources.energy.static
            #print self.planet.resources.energy.dynamic
            #print self.planet.resources.energy.total
            self.root.after(1000, self.updating)
