from Tkinter import *
import threading


class Resources(object):
    def __init__(self, root, game, row_i, column_i):
        print 'Resources'
        self.root = root
        # initiate game
        self.game = game

        # Available Resources
        # header
        print column_i
        Label(self.root, text='resource').grid(row=row_i, column=column_i)
        Label(self.root, text='Total').grid(row=row_i + 1, column=column_i)
        Label(self.root, text='per sec').grid(row=row_i + 2, column=column_i)
        for n, r in enumerate(self.game.resources):
            Label(self.root, text=r.name).grid(row=row_i, column=column_i + 1 + n)
            r.l_total = Label(self.root, text=self.game.metal.total)
            r.l_total.grid(row=row_i + 1, column=column_i + 1)
            r.l_per_s = Label(self.root, text=r.per_s)
            r.l_per_s.grid(row=row_i + 2, column=column_i + 1 + n)

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
