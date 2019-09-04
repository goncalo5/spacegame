# kivy:
from kivy.event import EventDispatcher
from kivy import properties as kp
# mine:
from settings import RESOURCES


class Resource(EventDispatcher):
    current = kp.NumericProperty()
    per_s = kp.NumericProperty()
    cap = kp.NumericProperty()
    def __init__(self, resource_name):
        super().__init__()
        self.name = resource_name
        self.current = RESOURCES.get(resource_name).get("init")
        self.per_s0 = RESOURCES.get(resource_name).get("per_s0")
        self.per_s = RESOURCES.get(resource_name).get("per_s0")
        self.cap0 = RESOURCES.get(resource_name).get("cap0")
        self.cap = RESOURCES.get(resource_name).get("cap0")
