from header import Header
from fill import Fill


class Buildings(object):
    def __init__(self, root, game, resources, row_i, column_i):
        self.root = root
        self.game = game

        self.header = Header(self.root, game, row_i, column_i)
        self.fill = Fill(self.root, game, resources, self.header, row_i + self.header.n_rows, column_i)
