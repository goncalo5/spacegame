from Tkinter import *
import threading, time
from logic.logic import Logic
from resources import Resources
from buildings import Buildings


class Presentation(object):
    def __init__(self):
        # initiate screen
        self.root = Tk()
        self.root.title('SPACEgame')

        # initiate game
        self.logic = Logic()
        print 'univ:', self.logic.universe
        self.logic.universe.create_player('gon')
        self.player = self.logic.universe.players[0]
        self.game = self.player.planets[0]

        # Available Resources
        self.resources = Resources(self.root, self.game, 0, 0)

        # Buildings
        self.buildings = Buildings(self.root, self.game, 3, 0)

        # create buttons
        l = self.buildings.head.l + 2
        self.b_buildings = []
        for i, building in enumerate(self.game.buildings):
            self.b_buildings.append(\
                Button(text=building.type, command=lambda b=building: self.evolve_building(b)))
            self.b_buildings[-1].grid(row=l + i, column=self.buildings.head.c_evol)

        self.b_quit = Button(text='quit', command=self.quit)
        self.b_quit.grid(row = 10, column=10)

        self.resources.updating()

        self.root.mainloop()

    def evolve_building(self, building):
        print 'evolve_building', building.name
        self.game.evolve_building(building)
        self.update(building)

    def update(self, building):
        self.buildings.fill.update(building)
        self.resources.update_all()

    def quit(self):
        print 'quit ............................\n\n'
        self.game.save()
        self.game.metal.total = 40
        self.game.run = False
        self.root.destroy()
