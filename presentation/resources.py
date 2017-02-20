from Tkinter import *
import threading


class Resources(object):
    def __init__(self, root, game, line_i, column_i):
        self.root = root
        # initiate game
        self.game = game

        # Available Resources
        # header
        Label(self.root, text='resource').grid(row=0, column=0)
        Label(self.root, text='per sec').grid(row=1, column=0)
        Label(self.root, text='Total').grid(row=2, column=0)
        for n, r in enumerate(self.game.resources):
            Label(self.root, text=r.name).grid(row=0, column=1 + n)
            r.l_per_s = Label(self.root, text=r.per_s)
            r.l_per_s.grid(row=1, column=1 + n)
            r.l_total = Label(self.root, text=self.game.metal.total)
            r.l_total.grid(row=2, column=1)

    def update(self, resource):
        resource.l_total['text'] = int(self.game.metal.total)
        resource.l_per_s['text'] = resource.per_s

    def update_all(self):
        for r in self.game.resources:
            self.update(r)

    def updating(self):
        self.update_all()
        #print 'updating ... ', self.game.metal.total
        # always use after method in Tkinter
        self.root.after(1000, self.updating)
