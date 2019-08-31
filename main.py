from kivy.app import App
from kivy.core.window import Window
from kivy import properties as kp
from kivy.clock import Clock
from kivy.event import EventDispatcher
# uix:
from kivy.uix.screenmanager import ScreenManager
# mine:
from settings import RESOURCES, BUILDINGS


class Building(EventDispatcher):
    name = kp.StringProperty()
    level = kp.NumericProperty()
    def __init__(self, settings):
        super().__init__()
        self.name = settings.get("name")
        self.level = settings.get("level", 0)
        self.cost0 = settings.get("cost0")
        self.cost_rate = settings.get("cost_rate")
        self.time0 = settings.get("time0")
        self.rate_time = settings.get("rate_time")


    def upgrade(self, construction_queue):
        print("upgrade", construction_queue)
        self.construction_queue = construction_queue
        self.app = App.get_running_app()
        if not self.app.check_if_can_pay(self.cost0):
            return
        self.app.pay_the_resources(self.cost0)
        self.construction_queue.size_hint_y = 0.1
        self.app.construction_building_name = self.name
        self.app.construction_time_left_s = self.time0
        Clock.schedule_interval(self.update_time_left, 0.1)

    def update_time_left(self, dt):
        print("update_time_left", dt)
        self.app.construction_time_left_s -= dt
        if self.app.construction_time_left_s <= 0:
            self.level += 1
            self.construction_queue.size_hint_y = None
            self.construction_queue.height = 0
            self.app.construction_building_name = ""
            self.app.construction_time_left = ""
            return False

class Game(ScreenManager):
    pass


class GameApp(App):
    window = kp.ObjectProperty(Window)
    # resources:
    metal = kp.NumericProperty(RESOURCES.get("metal").get("init"))
    crystal = kp.NumericProperty(RESOURCES.get("crystal").get("init"))
    deuterium = kp.NumericProperty(RESOURCES.get("deuterium").get("init"))
    metal_per_s = kp.NumericProperty(RESOURCES.get("metal").get("per_s"))
    crystal_per_s = kp.NumericProperty(RESOURCES.get("crystal").get("per_s"))
    deuterium_per_s = kp.NumericProperty(RESOURCES.get("deuterium").get("per_s"))
    # buildings:
    metal_mine = kp.ObjectProperty(Building(BUILDINGS.get("metal_mine")))
    crystal_mine = kp.ObjectProperty(Building(BUILDINGS.get("crystal_mine")))
    deuterium_mine = kp.ObjectProperty(Building(BUILDINGS.get("deuterium_mine")))
    # construction:
    construction_building_name = kp.StringProperty()
    construction_time_left_s = kp.NumericProperty()
    construction_time_left = kp.StringProperty()

    def build_config(self, *args):
        self.resources = {
            "metal": self.metal, "crystal": self.crystal,
            "deuterium": self.deuterium
        }

    def build(self):
        Clock.schedule_interval(self.update, 0.1)
        return Game()

    def update(self, dt):
        # update resources:
        self.metal += self.metal_per_s * dt
        self.crystal += self.crystal_per_s * dt
        self.deuterium += self.deuterium_per_s * dt
    
    def check_if_can_pay(self, resources):
        # check if can pay:
        if self.metal < resources["metal"] or\
            self.crystal < resources["crystal"] or\
            self.deuterium < resources["deuterium"]:
            return False
        return True

    def pay_the_resources(self, resources):
        self.metal -= resources["metal"]
        self.crystal -= resources["crystal"]
        self.deuterium -= resources["deuterium"]
    
    def on_construction_time_left_s(self, *args):
        self.construction_time_left = "%s" % int(self.construction_time_left_s)




if __name__ == "__main__":
    GameApp().run()
