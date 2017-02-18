from Tkinter import *
import constants
from logic import Logic
from header import Header


class Game(object):
    def __init__(self):
        self.root = Tk()
        self.root.title('SPACEgame')

        # initiate game
        self.game = Logic()

        # Available Resources
        # header
        Label(self.root, text='resource').grid(row=0, column=0)
        Label(self.root, text='per sec').grid(row=1, column=0)
        Label(self.root, text='Total').grid(row=2, column=0)
        for n, r in enumerate(self.game.resources):
            Label(self.root, text=r.name).grid(row=0, column=1 + n)
            r.l_per_s = Label(self.root, text=r.per_s)
            r.l_per_s.grid(row=1, column=1 + n)
            r.l_total = Label(self.root, text=r.total)
            r.l_total.grid(row=2, column=1 + n)

        # Header
        head = Header(self.root, 3, 0)
        for n, builting in enumerate(self.game.buildings):
            l = head.l + 2 + n
            Label(self.root, text=builting.name).\
                grid(row=l, column=head.c)
            # Level
            builting.l_lv = Label(self.root, text=builting.level)
            builting.l_lv.grid(row=l, column=head.c + 1)
            # evolving cost
            builting.l_cost = Label(self.root, text=int(builting.cost))
            builting.l_cost.grid(row=l, column=head.c_costs)
            # evolving time
            builting.l_t = Label(self.root, text=int(builting.time))
            builting.l_t.grid(row=l, column=head.c_t)
            # evolving
        # create buttons
        l = head.l + 2
        self.b_lv_metal_mine = \
            Button(text='evolve mine', command=lambda: self.evolve_building(self.game.metal_mine))
        self.b_lv_metal_mine.grid(row=l, column=head.c_evol)
        self.b_lv_robot_fac = \
            Button(text='evolve factory', command=lambda: self.evolve_building(self.game.robot_factory))
        self.b_lv_robot_fac.grid(row=l + 1, column=head.c_evol)

        self.update_resources()

        self.root.mainloop()

    def evolve_building(self, building):
        self.game.evolve_building(building)

        self.update_building(building)

    def update_resources(self):
        for r in self.game.resources:
            r.total += r.per_s
            r.l_total['text'] = int(r.total)

    def updating_resources(self):
        self.update_resources()
        self.root.after(1000, self.updating_resources)

    def update_building(self, building):
        building.l_lv['text'] = building.level
        building.l_cost['text'] = building.cost
        building.l_t['text'] = building.time
        self.game.metal.l_total['text'] = self.game.metal.total
        self.game.metal.l_per_s['text'] = self.game.metal.per_s

    def update_buildings(self):
        for builting in self.game.buildings:
            # e.t = e.left = (e.T * e.RATE_T ** e.lv) / (RATE_FB ** self.robot_fac.lv)
            #builting.l_t['text'] = int(e.t)
            pass
