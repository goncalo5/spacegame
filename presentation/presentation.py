from Tkinter import *
import threading, time
from logic.logic import Logic
from menu import Menu
from resources import Resources
from buildings import Buildings


class Presentation(object):
    def __init__(self, logic=Logic()):
        # initiate screen
        self.root = Tk()
        self.root.title('SPACEgame')

        # initiate game
        self.logic = logic
        # create_player
        self.logic.universe.create_player('gon')
        self.player = self.logic.universe.players[0]
        self.game = self.player.planets[0]

        # Available Resources
        self.resources = Resources(self.root, self.game, 0, 1)

        # create MENU
        self.menu = Menu(root=self.root,
            game=self.game, resources=self.resources,
            line_i=0, column_i=0)

        self.root.mainloop()
