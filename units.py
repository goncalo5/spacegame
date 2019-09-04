# kivy:
from kivy.app import App
from kivy import properties as kp
from kivy.event import EventDispatcher
# mine:
from settings import DEFENSES, SHIPS


class Unit(EventDispatcher):
    costs = kp.DictProperty()
    n = kp.NumericProperty()
    queue = kp.StringProperty("units")
    def __init__(self):
        super().__init__()
        self.name = self.settings.get("name")
        self.costs = self.settings.get("costs")
        self.hull = self.settings.get("hull")
        self.shield = self.settings.get("shield")
        self.weapen = self.settings.get("weapen")
        self.time = self.settings.get("time")
        self.requirements = self.settings.get("requirements")

    def check_if_it_have_the_necessary_requirements(self):
        if not self.requirements:
            return True
        print(self.requirements)

    def upgraded(self):
        self.n += 1

    def on_n(self, *args):
        print("on_n")


class Defense(Unit):
    def __init__(self, defense_name):
        self._id = defense_name
        self.settings = DEFENSES.get(self._id)
        super().__init__()

    def __str__(self):
        return "Defense(name=%s)" % self._id


class Ship(Unit):
    def __init__(self, defense_name):
        self._id = defense_name
        self.settings = SHIPS.get(self._id)
        super().__init__()

    def __str__(self):
        return "Ship(name=%s)" % self._id

