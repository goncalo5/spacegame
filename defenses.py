# kivy:
from kivy.app import App
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

    def upgrade(self, construction_queue, quantity=1):
        print("upgrade Defense", construction_queue)
        self.construction_queue = construction_queue
        self.app = App.get_running_app()
        try:
            quantity = int(quantity)
        except ValueError:
            print("ValueError please input an integer")
            return
        if not self.app.check_if_can_pay(self.costs):
            print("cant pay")
            return
        self.app.pay_the_resources(self.costs, quantity)
        self.show_construction_queue()
        self.app.construction.name = self.name
        self.app.construction.defenses_queue.append([self, int(quantity)])
        print("end", self.app.construction.defenses_queue)

    def show_construction_queue(self):
        print("show_construction_queue")
        self.construction_queue.size_hint_y = 0.1
        self.app.construction.have_queue = 1

    def hide_construction_queue(self):
        print("hide_construction_queue")
        self.construction_queue.size_hint_y = None
        self.construction_queue.height = 0
        self.app.construction.have_queue = 0
