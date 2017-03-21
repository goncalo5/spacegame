from Tkinter import *


class Hangar(object):
    def __init__(self, planet, root, resources, row_i, column_i):
        # logic attributes
        self.planet = planet
        # presentation attributes
        self.root = root
        self.resources = resources
        self.i = row_i
        self.j = column_i

        self.unit_being_trained = False
        text = "Hangar (level %i)" % self.planet.buildings.list[11].level
        Label(self.root, text=text).grid(row=self.i, column=self.j)
        if self.unit_being_trained:
            self.create_units_being_trained()
        self.create_units4training()
        self.create_units_not_available()

    def create_units_being_trained(self):
        Recruitment(root=self.root, i=2, j=0)

    def create_units4training(self):
        Available(planet=self.planet, root=self.root, i=6, j=0)

    def create_units_not_available(self):
        pass


class Recruitment(object):
    def __init__(self, root, i, j):  # i(row), j(column)
        Label(root, text="Recruitment").\
            grid(row=i + 2, column=j, columnspan=2)
        header = ['Training', 'Duration', 'Completion', 'Cancel']
        for i, h in header:
            Label(root, text=h).\
                grid(row=i + 3, column=j * i, columnspan=2)


class Available(object):
    def __init__(self, planet, root, i, j):
        self.planet = planet
        self.root = root
        self.i, self.j = i, j
        self.create_header()
        self.create_fill()

    def create_header(self):
        AvailableHeader(planet=self.planet, root=self.root, i=self.i, j=self.j)

    def create_fill(self):
        AvailableFill(planet=self.planet, root=self.root, i=self.i, j=self.j)


class AvailableHeader(object):
    def __init__(self, planet, root, i, j):
        self.planet = planet
        self.root = root
        self.i, self.j = i, j
        self.i = 6
        Label(self.root, text='Unit').\
            grid(row=self.i, column=self.j)
        self.create_requirements()
        Label(self.root, text='In the \nplanet/total'). \
            grid(row=self.i,
                 column=self.j + self.planet.resources.n + 2,
                 rowspan=2)
        Label(self.root, text='Recruit'). \
            grid(row=self.i,
                 column=self.j + self.planet.resources.n + 3,
                 columnspan=2)

    def create_requirements(self):
        Label(self.root, text='Requirements'). \
            grid(row=self.i, column=self.j + 1,
                 columnspan=self.planet.resources.n + 1)  # + 1, because of time
        for i, resource in enumerate(self.planet.resources.list):
            Label(self.root, text=resource.name). \
                grid(row=self.i + 1, column=self.j + i + 1)
        Label(self.root, text='time'). \
            grid(row=self.i + 1,
                 column=self.j + self.planet.resources.n + 1)


class AvailableFill(object):
    def __init__(self, planet, root, i, j):
        self.planet = planet
        self.root = root
        self.i, self.j = i, j
        for i, spaceship in enumerate(self.planet.spaceships):
            self.create_n_available_type(i, spaceship, self.planet.spaceships[spaceship])

    def create_n_available_type(self, i, spaceship, n_spaceships):
        Label(self.root, text=spaceship.name).grid(row=self.i + i + 2, column=self.j)
        for j, cost in enumerate(spaceship.costs):
            Label(self.root, text=cost).grid(row=self.i + i + 2, column= self.j + j + 1)
        Label(self.root, text=spaceship.time).grid(row=self.i + i + 2, column=self.j + self.planet.resources.n + 1)
