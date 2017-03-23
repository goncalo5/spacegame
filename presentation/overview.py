from Tkinter import *


class Overview(object):
    def __init__(self, universe, planet, presentation, root, row_i=0, column_i=0):
        self.universe, self.planet, self.presentation, self.root, self.i, self.j \
            = universe, planet, presentation, root, row_i, column_i
        self.player = ['Player', 'points', 'position']
        self.planets = ['Planets', 'coordinates', 'fields', 'temperature']
        self.all = self.player + self.planets
        for i, l in enumerate(self.all):
            Label(self.root, text=l).grid(row=self.i + i, column=self.j)
