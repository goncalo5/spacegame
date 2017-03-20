from Tkinter import *
import time
from constants import SCREEN
from logic.logic import Logic
from menu import Menu
from resources import Resources


class Presentation(object):
    def __init__(self, logic=Logic()):
        t = []
        t.append(time.time())
        # initiate screen
        self.root = Tk()  # 83 % of all time
        t.append(time.time())
        self.root.title('SPACEgame')
        t.append(time.time())
        self.root.geometry(SCREEN)
        t.append(time.time())
        self.root.configure(background='black')
        t.append(time.time())
        # create frames
        self.f_menu = Frame(master=self.root, width=100, height=400, bg='black')
        self.f_resources = Frame(master=self.root, width=300, height=100, bg='black')
        self.f_screen = Frame(master=self.root, width=300, height=300, bg='black')
        self.f_menu.pack(side=LEFT)
        self.f_resources.pack()
        #self.f_screen.pack()
        t.append(time.time())

        # initiate game
        self.logic = logic
        # create_player
        self.logic.universe.create_player('gon')
        self.player = self.logic.universe.players[0]
        self.planet = self.player.planets[0]
        t.append(time.time())

        # Available Resources
        self.resources = Resources(self.f_resources, self.planet, 0, 1)  # 15 % off all time
        t.append(time.time())

        # create MENU
        self.menu = Menu(root=self.root, menu=self.f_menu,#, screen=self.f_screen,
                         planet=self.planet, resources=self.resources,
                         row_i=0, column_i=0)
        t.append(time.time())
        for i in xrange(len(t) - 1):
            pass
            #print t[i + 1] - t[i],
        #print t[-1] - t[0]

        self.root.mainloop()
