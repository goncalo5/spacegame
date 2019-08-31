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
    cost = kp.DictProperty()
    time = kp.NumericProperty()
    def __init__(self, settings):
        super().__init__()
        self.name = settings.get("name")
        self.level = settings.get("level", 0)
        self.cost0 = settings.get("cost0")
        self.cost_rate = settings.get("cost_rate")
        self.time0 = settings.get("time0")
        self.time_rate = settings.get("time_rate")

        Clock.schedule_once(self.on_level, 0)

    def upgrade(self, construction_queue):
        print("upgrade", construction_queue)
        self.construction_queue = construction_queue
        self.app = App.get_running_app()
        if not self.app.check_if_can_pay(self.cost):
            return
        self.app.pay_the_resources(self.cost)
        self.construction_queue.size_hint_y = 0.1
        self.app.construction_building_name = self.name
        self.app.construction_time_left_s = self.time
        Clock.schedule_interval(self.update_time_left, 0.1)

    def update_time_left(self, dt):
        # print("update_time_left", dt)
        self.app.construction_time_left_s -= dt
        if self.app.construction_time_left_s <= 0:
            self.level += 1
            self.construction_queue.size_hint_y = None
            self.construction_queue.height = 0
            self.app.construction_building_name = ""
            self.app.construction_time_left = ""
            self.app.display_costs(self)
            return False

    def on_level(self, *args):
        print("on_level")
        self.app = App.get_running_app()
        # update resources:
        self.cost["metal"] = self.cost0["metal"] * self.cost_rate ** self.level
        self.cost["crystal"] =\
            self.cost0["crystal"] * self.cost_rate ** self.level
        self.cost["deuterium"] =\
            self.cost0["deuterium"] * self.cost_rate ** self.level
        # update time:
        self.time = self.time0 * self.time_rate ** self.level
        # self.update_feature()
        Clock.schedule_once(self.update_feature, 0)

    def update_feature(self, *args):
        pass


class MetalMine(Building):
    def __init__(self, settings):
        super().__init__(settings)
        self.metal_rate = settings.get("metal_rate")

    def update_feature(self, *args):
        self.app = App.get_running_app()
        self.app.metal_per_s =\
            self.app.metal_per_s0 * self.metal_rate ** self.level

class Game(ScreenManager):
    pass


class GameApp(App, ScreenManager):
    window = kp.ObjectProperty(Window)
    # resources:
    metal = kp.NumericProperty(RESOURCES.get("metal").get("init"))
    crystal = kp.NumericProperty(RESOURCES.get("crystal").get("init"))
    deuterium = kp.NumericProperty(RESOURCES.get("deuterium").get("init"))
    metal_per_s0 = kp.NumericProperty(RESOURCES.get("metal").get("per_s0"))
    crystal_per_s0 = kp.NumericProperty(RESOURCES.get("crystal").get("per_s0"))
    deuterium_per_s0 = kp.NumericProperty(RESOURCES.get("deuterium").get("per_s0"))
    metal_per_s = kp.NumericProperty(RESOURCES.get("metal").get("per_s0"))
    crystal_per_s = kp.NumericProperty(RESOURCES.get("crystal").get("per_s0"))
    deuterium_per_s = kp.NumericProperty(RESOURCES.get("deuterium").get("per_s0"))
    # buildings:
    metal_mine = kp.ObjectProperty(MetalMine(BUILDINGS.get("metal_mine")))
    crystal_mine = kp.ObjectProperty(Building(BUILDINGS.get("crystal_mine")))
    deuterium_mine = kp.ObjectProperty(Building(BUILDINGS.get("deuterium_mine")))
    # construction:
    construction_building_name = kp.StringProperty()
    construction_time_left_s = kp.NumericProperty()
    construction_time_left = kp.StringProperty()
    metal_cost = kp.StringProperty()
    crystal_cost = kp.StringProperty()
    deuterium_cost = kp.StringProperty()
    time_cost = kp.StringProperty()

    def build_config(self, *args):
        self.resources = {
            "metal": self.metal, "crystal": self.crystal,
            "deuterium": self.deuterium
        }

    def build(self):
        Clock.schedule_interval(self.update, 0.1)
        self.game = Game()
        return self.game
    
    def display_costs(self, building):
        self.metal_cost =  "metal: %s" % int(building.cost["metal"])
        self.crystal_cost =  "crystal: %s" % int(building.cost["crystal"])
        self.deuterium_cost =  "deuterium: %s" % int(building.cost["deuterium"])
        self.time_cost =  "time: %s" % int(building.time)

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
