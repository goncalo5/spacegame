from Tkinter import *
from constants import *


class Header(object):
    def __init__(self, i, linha_i, coluna_i):
        self.i = i
        self.l = linha_i  # upper Header line
        self.c = coluna_i  # initial Header column
        Label(self.i, text='Building').grid(row=self.l, column=self.c, rowspan=2)
        Label(self.i, text='Level').grid(row=self.l, column=self.c + 1, rowspan=2)

        # initial costs column
        self.c_costs = 2
        Label(self.i, text='evolving cost'). \
            grid(row=self.l, column=self.c_costs, columnspan=len(RESOURCES))
        for n, r in enumerate(RESOURCES):
            # costs
            Label(self.i, text=r).grid(row=self.l + 1, column=self.c_costs + n)
        # Column of construction times
        self.c_t = self.c_costs + len(RESOURCES)
        Label(self.i, text='Time'). \
            grid(row=self.l, column=self.c_t, rowspan=2)
        # evolving column
        self.c_evol = self.c_t + 1
        Label(self.i, text='Evolutions').\
            grid(row=self.l, column=self.c_evol, rowspan=2)

