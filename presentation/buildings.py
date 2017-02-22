from header import Header
from fill import Fill


class Buildings(object):
    def __init__(self, root, game, resources, line_i, column_i):
        self.root = root
        self.game = game

        self.header = Header(self.root, game, line_i, column_i)
        self.fill = Fill(self.root, game, resources, self.header, line_i + self.header.n_lines, column_i)
