from header import Header
from fill import Fill


class Buildings(object):
    def __init__(self, root, planet, resources, row_i, column_i):
        self.root = root
        self.planet = planet

        self.header = Header(self.root, planet, row_i, column_i)
        self.fill = Fill(self.root, planet, resources, self.header, row_i + self.header.n_rows, column_i)
