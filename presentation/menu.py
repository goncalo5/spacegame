from Tkinter import *
import constants
from overview import Overview
from buildings import Buildings


class Menu(object):
    def __init__(self, root, game, resources, row_i, column_i):
        self.root = root
        self.game = game
        self.resources = resources

        self.buttons = []
        for i, item in enumerate(constants.MENU):
            self.buttons.append(\
                Button(text=item, command=lambda b=item: self.change_screen(b)))
            self.buttons[-1].grid(row=row_i + i, column=column_i)

        self.functions = {'overview': self.overview, 'buildings': self.buildings}


        self.b_quit = Button(text='quit', command=self.quit)
        self.b_quit.grid(row = row_i + len(constants.MENU) + 1, column=column_i)

    def quit(self):
        self.game.save()
        self.game.run = False
        
        self.root.destroy()

    def change_screen(self, item):
        self.functions[item]()

    def overview(self):
        self.overview = Overview(root=self.root,
            game=self.game, row_i=3, column_i=1)

    def buildings(self):
        self.buildings = Buildings(root=self.root,
            game=self.game, resources=self.resources, row_i=3, column_i=1)
