# kivy:
from kivy.app import App
from kivy.event import EventDispatcher
from kivy import properties as kp
from kivy.clock import Clock
# mine:
from settings import RESEARCHES


class Research(EventDispatcher):
    name = kp.StringProperty()
    level = kp.NumericProperty()
    costs = kp.DictProperty()
    time = kp.NumericProperty()
    def __init__(self, research_name):
        super().__init__()
        print(research_name)
        self._id = research_name
        self.settings = RESEARCHES.get(self._id)
        self.name = self.settings.get("name")
        self.costs0 = self.settings.get("costs0")
        self.costs_rate = self.settings.get("costs_rate")
        self.time0 = self.settings.get("time0")
        self.time_rate = self.settings.get("time_rate")

        Clock.schedule_once(self.on_level, 0)
    
    def __repr__(self):
        return "Research(id=%s)" % self._id

    def upgrade(self, construction_queue, quantity=1):
        print("upgrade Research")
        self.construction_queue = construction_queue
        self.app = App.get_running_app()
        if not self.app.check_if_can_pay(self.costs):
            return
        self.app.pay_the_resources(self.costs)
        self.show_construction_queue()
        self.app.construction.name = self.name
        self.app.construction.time_left_s = self.time
        Clock.schedule_interval(self.update_time_left, 0.1)

    def update_time_left(self, dt):
        print("update_time_left")
        if self.app.construction.is_cancel:
            self.app.return_the_resources(self.costs)
            self.hide_construction_queue()
            self.app.construction.is_cancel = False
            return False
        self.app.construction.time_left_s -= dt
        if self.app.construction.time_left_s <= 0:
            self.level += 1
            self.hide_construction_queue()
            self.app.construction.display_costs(self)
            return False
    
    def show_construction_queue(self):
        print("show_construction_queue")
        self.construction_queue.size_hint_y = 0.1
        self.app.construction.have_queue = 1

    def hide_construction_queue(self):
        print("hide_construction_queue")
        self.construction_queue.size_hint_y = None
        self.construction_queue.height = 0
        self.app.construction.have_queue = 0

    def on_level(self, *args):
        print("on_level")
        self.app = App.get_running_app()
        # update resources:
        self.costs["metal"] = self.costs0["metal"] * self.costs_rate ** self.level
        self.costs["crystal"] =\
            self.costs0["crystal"] * self.costs_rate ** self.level
        self.costs["deuterium"] =\
            self.costs0["deuterium"] * self.costs_rate ** self.level
        self.update_time()

    def update_time(self):
        # update time:
        print("time", self.time)
        self.time = self.time0 * self.time_rate ** self.level
