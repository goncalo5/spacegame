from header import Header
from fill import Fill


class Buildings(object):
    def __init__(self, root, game, line_i, column_i):
        self.root = root
        self.game = game

        self.head = Header(self.root, line_i, column_i)
        self.fill = Fill(self.root, game, line_i + self.head.n_lines, column_i)


