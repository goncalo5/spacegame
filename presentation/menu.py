from buildings import Buildings


class Menu(object):
    def __init__(self, root, game, resources, line_i, column_i):
            self.root = root
            self.game = game
            self.resources = resources

            # Buildings
            self.buildings = Buildings(root=self.root,
                game=self.game, resources=self.resources, line_i=3, column_i=0)
