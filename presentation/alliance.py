class Alliance(object):
    def __init__(self, universe, planet, presentation, root, row_i=0, column_i=0):
        self.universe, self.planet, self.presentation, self.root, self.i, self.j \
            = universe, planet, presentation, root, row_i, column_i