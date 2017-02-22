from Tkinter import *
import constants
from buildings import Buildings


class Menu(object):
    def __init__(self, root, game, resources, line_i, column_i):
        print 'menu'
        self.root = root
        self.game = game
        self.resources = resources

        self.buttons = []
        a = Label(self.root, text='aaa')
        a.grid(row=0, column=0)
        print constants.MENU
        for i, item in enumerate(constants.MENU):
            self.buttons.append(\
                Button(text=item, command=lambda b=item: self.change_screen(b)))
            self.buttons[-1].grid(row=line_i + i, column=column_i)

        self.functions = {'buildings': self.buildings}
        print type(self.buildings)
        print '...menu'



    def change_screen(self, item):
        print 'item', item
        self.functions[item]()

    def buildings(self):
        # Buildings
        self.buildings = Buildings(root=self.root,
        game=self.game, resources=self.resources, line_i=3, column_i=1)
