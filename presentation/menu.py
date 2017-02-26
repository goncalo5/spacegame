from Tkinter import *
import constants
from overview import Overview
from buildings import Buildings


class Menu(object):
    def __init__(self, root, menu, screen, game, resources, row_i, column_i):
        # attributes
        self.root = root
        self.f_menu = menu
        self.f_screen = screen
        self.game = game
        self.resources = resources
        # null attributes
        self.overview = self.buildings = None

        self.buttons = []
        for i, item in enumerate(constants.MENU):
            self.buttons.append(
                Button(self.f_menu, text=item, command=lambda b=item: self.change_screen(b)))
            self.buttons[-1].grid(row=row_i + i, column=column_i)

        self.functions = {'overview': self.change2overview, 'buildings': self.change2buildings}


        self.b_quit = Button(self.f_menu, text='quit', command=self.quit)
        self.b_quit.grid(row=row_i + len(constants.MENU) + 1, column=column_i)

    def quit(self):
        self.game.save()
        self.game.run = False
        self.root.destroy()

    def create_new_frame(self):
        self.f_screen = Frame(master=self.root, width=300, height=300)
        self.f_screen.pack()

    def change_screen(self, item):
        self.functions[item]()

    def change2overview(self):
        self.f_screen.destroy()
        self.create_new_frame()
        self.overview = Overview(root=self.f_screen,
                                  game=self.game, row_i=3, column_i=1)

    def change2buildings(self):
        self.f_screen.destroy()
        self.create_new_frame()
        self.buildings = Buildings(root=self.f_screen, game=self.game,
                                   resources=self.resources, row_i=3, column_i=1)
