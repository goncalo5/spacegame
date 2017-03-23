from Tkinter import *
import constants
import functions
from overview import Overview
from resources import MenuResources
from buildings import Buildings
from market import Market
from research import Research
from hangar import Hangar
from defense import Defense
from fleet import Fleet
from universe import Universe
from alliance import Alliance


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
        # null
        self.f_overview = None
        # initial methods
        self.create_buttons()
        self.create_menus()

    # initial methods
    def create_buttons(self):
        self.buttons = []
        for i, item in enumerate(constants.MENU):
            self.buttons.append(
                Button(self.frame, text=item,
                       command=lambda b=functions.transform_name(item): self.change_screen(b)))
            self.buttons[-1].grid(row=self.i + i, column=self.j)
        # quit button
        self.b_quit = Button(self.frame, text='quit', command=self.quit)
        self.b_quit.grid(row=self.i + len(constants.MENU) + 1, column=self.j)

    def create_menus(self):
        self.change2class = {'overview': Overview, 'resources': MenuResources,
                             'buildings': Buildings, 'market': Market,
                             'research': Research, 'hangar': Hangar,
                             'defense': Defense, 'fleet': Fleet,
                             'universe': Universe, 'alliance': Alliance}

        for item in constants.MENU:
            self.create_menu(functions.transform_name(item))
        self.f_overview.pack()
        self.f_screen = self.f_overview

    def create_menu(self, item):
        setattr(self, 'f_' + item, Frame(master=self.presentation.root, width=300, height=300, bg='black'))
        setattr(self, item, self.change2class[item](
            universe=self.universe, planet=self.planet,
            presentation=self.presentation, root=getattr(self, 'f_' + item),
            row_i=3, column_i=1))

    # others methods
    def clean_screen(self):
        self.f_screen.pack_forget()

    def change_screen(self, item):
        self.clean_screen()
        self.f_screen = getattr(self, 'f_' + item)
        getattr(self, 'f_' + item).pack()

    def quit(self):
        self.planet.save()
        self.planet.run = False
        self.presentation.root.destroy()
