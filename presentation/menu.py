from Tkinter import *
import time
import constants
from overview import Overview
from resources import MenuResources
from buildings import Buildings
from market import Market
from hangar import Hangar


class Menu(object):
    def __init__(self, universe, planet, presentation, row_i, column_i):
        # attributes
        # logic attributes
        self.universe = universe
        self.planet = planet
        # presentation attributes
        self.presentation = presentation
        self.presentation.menu = self
        self.frame = self.presentation.f_menu
        self.i, self.j = row_i, column_i

        # null attributes
        self.overview = self.buildings = None

        # initial methods
        self.create_buttons()
        self.create_menus()

        self.functions = {'overview': self.change2overview,
                          'resources': self.change2resources,
                          'buildings': self.change2buildings,
                          'market': self.change2market,
                          'hangar': self.change2hangar}


        self.b_quit = Button(self.frame, text='quit', command=self.quit)
        self.b_quit.grid(row=row_i + len(constants.MENU) + 1, column=column_i)

    # initial methods
    def create_buttons(self):
        self.buttons = []
        for i, item in enumerate(constants.MENU):
            self.buttons.append(
                Button(self.frame, text=item, command=lambda b=item: self.change_screen(b)))
            self.buttons[-1].grid(row=self.i + i, column=self.j)

    def create_menus(self):
        self.f_overview = Frame(master=self.presentation.root, width=300, height=300, bg='black')
        self.f_overview.pack()
        self.overview = Overview(root=self.f_overview, planet=self.planet, row_i=3, column_i=1)
        self.f_screen = self.f_overview

        self.f_resources = Frame(master=self.presentation.root, width=300, height=300, bg='black')
        self.resources = MenuResources(planet=self.planet, root=self.f_resources,
                                       resources=self.presentation.resources, row_i=3, column_i=1)

        self.f_buildings = Frame(master=self.presentation.root, width=300, height=300, bg='black')
        self.buildings = Buildings(planet=self.planet,
                                   presentation=self.presentation, row_i=3, column_i=1)

        self.f_market = Frame(master=self.presentation.root, width=300, height=300, bg='black')
        self.market = Market(universe=self.universe, planet=self.planet,
                             root=self.f_market, resources=self.presentation.resources,
                             row_i=3, column_i=1)

        self.f_hangar = Frame(master=self.presentation.root, width=300, height=300, bg='black')
        self.hangar = Hangar(root=self.f_hangar, planet=self.planet,
                             resources=self.presentation.resources, row_i=3, column_i=1)

    # others methods
    def clean_screen(self):
        self.f_screen.pack_forget()

    def change_screen(self, item):
        self.functions[item]()

    def change2overview(self):
        self.clean_screen()
        self.f_screen = self.f_overview
        self.f_overview.pack()

    def change2resources(self):
        self.clean_screen()
        self.resources.create_fill()
        self.f_resources.pack()
        self.f_screen = self.f_resources

    def change2buildings(self):
        self.clean_screen()
        self.f_buildings.pack()
        self.f_screen = self.f_buildings

    def change2market(self):
        self.clean_screen()
        self.f_market.pack()
        self.f_screen = self.f_market

    def change2hangar(self):
        self.clean_screen()
        self.f_hangar.pack()
        self.f_screen = self.f_hangar

    def quit(self):
        self.planet.save()
        self.planet.run = False
        self.presentation.root.destroy()
