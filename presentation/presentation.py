from Tkinter import *
from logic.logic import Logic
from resources import Resources
from buildings import Buildings


class Presentation(object):
    def __init__(self):
        # initiate screen
        self.root = Tk()
        self.root.title('SPACEgame')

        # initiate game
        self.game = Logic()

        # Available Resources
        self.resources = Resources(self.root, self.game, 0, 0)

        # Buildings
        self.buildings = Buildings(self.root, self.game, 3, 0)

        # create buttons
        l = self.buildings.head.l + 2
        self.b_lv_metal_mine = \
            Button(text='evolve mine', command=lambda: self.evolve_building(self.game.metal_mine))
        self.b_lv_metal_mine.grid(row=l, column=self.buildings.head.c_evol)
        self.b_lv_robot_fac = \
            Button(text='evolve factory', command=lambda: self.game.robot_factory)
        self.b_lv_robot_fac.grid(row=l + 1, column=self.buildings.head.c_evol)

        self.resources.updating()

        self.root.mainloop()

    def evolve_building(self, building):
        self.game.evolve_building(building)
        self.update(building)

    def update(self, building):
        self.buildings.fill.update(building)
        self.resources.update_all()
