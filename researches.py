# kivy:
from kivy.app import App
from kivy.event import EventDispatcher
from kivy import properties as kp
from kivy.clock import Clock
# mine:
from settings import RESEARCHES
from buildings import UpgradingEvent


class Research(UpgradingEvent):
    queue = kp.StringProperty("researches")
    def __init__(self, research_name):
        self._id = research_name
        self.settings = RESEARCHES.get(self._id)
        super().__init__()
        self.name = self.settings.get("name")
        self.costs0 = self.settings.get("costs0")
        self.costs_rate = self.settings.get("costs_rate")
        self.time0 = self.settings.get("time0")
        self.time_rate = self.settings.get("time_rate")

        Clock.schedule_once(self.on_level, 0)
    
    def __repr__(self):
        return "Research(id=%s)" % self._id

    def update_time(self):
        # update time:
        print("time", self.time)
        self.time = self.time0 * self.time_rate ** self.level
