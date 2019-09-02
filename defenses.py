# kivy:
from kivy import properties as kp
from kivy.event import EventDispatcher
# mine:
from settings import RESOURCES, DEFENSES


class Defense(EventDispatcher):
    costs = kp.DictProperty()
    n = kp.NumericProperty()
    def __init__(self, defense_name):
        super().__init__()
        self._id = defense_name
        self.settings = DEFENSES.get(defense_name)
        self.name = self.settings.get("name")
        self.costs = self.settings.get("costs")
        self.hull = self.settings.get("hull")
        self.shield = self.settings.get("shield")
        self.weapen = self.settings.get("weapen")
        self.time = self.settings.get("time")

    def __str__(self):
        return "Defense(name=%s)" % self.name

    def on_n(self, *args):
        print("on_n")

    def upgrade(self, queue):
        print("upgrade Defense")
        return
