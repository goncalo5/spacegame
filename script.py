# from Tkinter import *
# from constantes import *
from cabecalho import *


class Game(object):
    def __init__(self):
        self.i = Tk()
        self.i.title('SPACEgame')

        # Available Resources
        # header
        Label(self.i, text='resource').grid(row=0, column=0)
        Label(self.i, text='per sec').grid(row=1, column=0)
        Label(self.i, text='Total').grid(row=2, column=0)
        # create resources's objects
        self.metal = Resources(RESOURCES[0], METAL['TOTAL'],
                               METAL['PER_S'], METAL['RATE_PER_S'])
        self.resources = [self.metal]
        for n, r in enumerate(self.resources):
            Label(self.i, text=r.name).grid(row=0, column=1 + n)
            r.l_per_s = Label(self.i, text=r.per_s)
            r.l_per_s.grid(row=1, column=1 + n)
            r.l_total = Label(self.i, text=r.total)
            r.l_total.grid(row=2, column=1 + n)

        # Buildings
        # create buildings's objects
        self.metal_mine = Buildings(self.i, lv=0, evol=False,
                                    left=METAL_MINE['time'],
                                    **METAL_MINE)

        self.robot_fac = Buildings(self.i, lv=0, evol=False,
                                   left=ROBOT_FAC['time'], **ROBOT_FAC)

        # Header
        head = Header(self.i, 3, 0)
        self.buildings = [self.metal_mine, self.robot_fac]
        self.mines = [self.metal_mine]
        for n, e in enumerate(self.buildings):
            l = head.l + 2 + n
            Label(self.i, text=e.NAME).\
                grid(row=l, column=head.c)
            # Level
            e.l_lv = Label(self.i, text=e.lv)
            e.l_lv.grid(row=l, column=head.c + 1)
            # evolving cost
            e.l_cost = Label(self.i, text=int(e.cost))
            e.l_cost.grid(row=l, column=head.c_costs)
            # evolving time
            e.l_t = Label(self.i, text=int(e.t))
            e.l_t.grid(row=l, column=head.c_t)
            # evolving
        # create buttons
        l = head.l + 2
        self.metal_mine.b_lv = \
            Button(text='evolve mine', command=lambda: self.evolve(self.metal_mine))
        self.metal_mine.b_lv.grid(row=l, column=head.c_evol)
        self.robot_fac.b_lv = \
            Button(text='evolve factory', command=lambda: self.evolve(self.robot_fac))
        self.robot_fac.b_lv.grid(row=l + 1, column=head.c_evol)

        self.update_resources()

        self.i.mainloop()

    def evolve(self, e):
        if self.metal.total >= e.cost and not e.evol:
            self.metal.total -= e.cost
            self.metal.l_total['text'] = int(self.metal.total)
            e.evol = True
            self.loop_evolve(e)

    def loop_evolve(self, e):
        if e.evol:
            e.left -= 1
            if e.left <= 0:
                e.lv += 1
                e.cost = e.COST * e.RATE_COST ** e.lv
                e.t = (e.T * e.RATE_T ** e.lv) / \
                      (RATE_FB ** self.robot_fac.lv)
                # Labels
                e.l_lv['text'] = e.lv
                e.l_cost['text'] = int(e.cost)
                e.l_t['text'] = int(e.t)

                e.left = e.t
                e.evol = False

                # effects of evolution
                if e.NAME == 'metal mine':
                    self.metal.per_s = \
                        METAL['PER_S'] * METAL['RATE_PER_S']**self.metal_mine.lv
                    self.metal.l_per_s['text'] = int(self.metal.per_s)
                if e.NAME == 'robots factory':
                    self.update_buildings()
            e.l_t['text'] = int(e.left)

            self.i.after(1000, lambda: self.loop_evolve(e))

    def update_resources(self):
        for r in self.resources:
            r.total += r.per_s
            r.l_total['text'] = int(r.total)

    def updating_resources(self):
        self.update_resources()
        self.i.after(1000, self.updating_resources)

    def update_buildings(self):
        for e in self.buildings:
            e.t = e.left = (e.T * e.RATE_T ** e.lv) / (RATE_FB ** self.robot_fac.lv)
            e.l_t['text'] = int(e.t)


class Resources(object):
    def __init__(self, name, total, per_s, rate_per_s):
        self.l_total = self.l_per_s = None
        self.name = name
        self.total = total
        self.per_s = per_s
        self.rate_per_s = rate_per_s


class Buildings(object):
    def __init__(self, i, lv, left, evol,
                 name, cost, rate_cost, time, rate_t):
        self.i = i
        self.l_lv = self.l_cost = self.l_t = None

        # constants
        self.NAME = name
        self.COST = cost
        self.RATE_COST = rate_cost
        self.T = time
        self.RATE_T = rate_t

        # variables
        self.lv = lv  # level
        self.cost = self.COST * self.RATE_COST**self.lv
        self.t = self.T * self.RATE_T**self.lv
        self.evol = evol
        self.left = left


if __name__ == '__main__':
    Game()
