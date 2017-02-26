from Tkinter import *


class Overview(object):
    def __init__(self, root, planet, row_i, column_i):
        self.player = ['Player', 'points', 'position']
        self.planets = ['Planets', 'coordinates', 'fields', 'temperature']
        self.all = self.player + self.planets
        for i, l in enumerate(self.all):
            Label(root, text=l).grid(row=row_i + i, column=column_i)
