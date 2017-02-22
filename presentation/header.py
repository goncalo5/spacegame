from Tkinter import *
from constants import *


class Header(object):
    def __init__(self, root, game, line_i, column_i):
        self.root = root
        # initiate game
        self.game = game

        self.l = line_i  # upper Header line
        self.c = column_i  # initial Header column
        self.n_lines = 2
        Label(self.root, text='Building').grid(row=self.l, column=self.c, rowspan=2)
        Label(self.root, text='Level').grid(row=self.l, column=self.c + 1, rowspan=2)

        # initial costs column
        self.c_costs = self.c + 2
        Label(self.root, text='evolving cost'). \
            grid(row=self.l, column=self.c_costs, columnspan=self.game.n_resources)
        for n, r in enumerate(self.game.resources):
            # costs
            Label(self.root, text=r.name).grid(row=self.l + 1, column=self.c_costs + n)
        # Column of construction times
        self.c_t = self.c_costs + self.game.n_resources
        Label(self.root, text='Time'). \
            grid(row=self.l, column=self.c_t, rowspan=2)
        # evolving column
        self.c_evol = self.c_t + 1
        Label(self.root, text='Evolve').\
            grid(row=self.l, column=self.c_evol, rowspan=2)
