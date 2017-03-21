from Tkinter import *
import time
import constants
from overview import Overview
from buildings import Buildings


class Menu(object):
    def __init__(self, planet, root, menu, resources, row_i, column_i):
        # attributes
        self.planet = planet

        self.root = root
        self.f_menu = menu
        self.resources = resources
        
        self.f_overview = Frame(master=self.root, width=300, height=300, bg='black')
        self.f_overview.pack()
        self.overview = Overview(root=self.f_overview,
                                 planet=self.planet, row_i=3, column_i=1)
        self.f_screen = self.f_overview
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
        self.f_screen.pack_forget()

    def change_screen(self, item):
        self.functions[item]()

    def change2overview(self):
        self.clean_screen()
        self.f_screen = self.f_overview
        self.f_overview.pack()

    def change2buildings(self):
        self.clean_screen()
        try:
            self.f_buildings.pack()
        except:
            self.f_buildings = Frame(master=self.root, width=300, height=300, bg='black')
            self.f_buildings.pack()
            self.buildings = Buildings(root=self.f_buildings, planet=self.planet,
                                       resources=self.resources, row_i=3, column_i=1)
        self.f_screen = self.f_buildings

