from Tkinter import *
import constants
from overview import Overview
from buildings import Buildings


class Menu(object):
    def __init__(self, root, menu, screen, planet, resources, row_i, column_i):
        # attributes
        self.root = root
        self.f_menu = menu
        self.f_screen = screen
        self.planet = planet
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
        self.planet.save()
        self.planet.run = False
        self.root.destroy()

    def clean_screen(self):
        self.f_screen.destroy()
        self.f_screen = Frame(master=self.root, width=300, height=300)
        self.f_screen.pack()

    def change_screen(self, item):
        self.functions[item]()

    def change2overview(self):
        self.clean_screen()
        self.overview = Overview(root=self.f_screen,
                                 planet=self.planet, row_i=3, column_i=1)

    def change2buildings(self):
        self.clean_screen()
        self.buildings = Buildings(root=self.f_screen, planet=self.planet,
                                   resources=self.resources, row_i=3, column_i=1)
