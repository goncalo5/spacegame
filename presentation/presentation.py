from Tkinter import *
from logic.logic import Logic
from menu import Menu
from resources import Resources


class Presentation(object):
    def __init__(self, logic=Logic()):
        # initiate screen
        self.root = Tk()
        self.root.title('SPACEgame')
        self.root.geometry('600x400')
        self.root.configure(background='black')
        # create frames
        self.f_menu = Frame(master=self.root, width=100, height=400, bg='black')
        self.f_resources = Frame(master=self.root, width=300, height=100, bg='black')
        self.f_screen = Frame(master=self.root, width=300, height=300, bg='black')
        self.f_menu.pack(side=LEFT)
        self.f_resources.pack()
        self.f_screen.pack()

        # initiate game
        self.logic = logic
        # create_player
        self.logic.universe.create_player('gon')
        self.player = self.logic.universe.players[0]
        self.planet = self.player.planets[0]

        # Available Resources
        self.resources = Resources(self.f_resources, self.planet, 0, 1)

        # create MENU
        self.menu = Menu(root=self.root, menu=self.f_menu, screen=self.f_screen,
                         planet=self.planet, resources=self.resources,
                         row_i=0, column_i=0)

        self.root.mainloop()
