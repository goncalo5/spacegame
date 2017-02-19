from Tkinter import *


class Fill(object):
    def __init__(self, root, game, line_i, column_i):
        self.root = root
        # initiate game
        self.game = game

        for n, building in enumerate(self.game.buildings):
            l = line_i + n
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
            building.l_t.grid(row=l, column=column_i + 2 + self.game.n_resources)
            # evolving

    def update(self, building):
        building.l_lv['text'] = building.level
        building.l_cost['text'] = building.cost
        building.l_t['text'] = building.time

    def update_all(self):
        for building in self.game.buildings:
            self.update(building)