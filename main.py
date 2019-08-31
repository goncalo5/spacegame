# kivy:
from kivy.app import App
from kivy.core.window import Window
from kivy import properties as kp
from kivy.clock import Clock
from kivy.event import EventDispatcher
# kivy.uix:
from kivy.uix.screenmanager import ScreenManager
# mine:
from settings import RESOURCES, BUILDINGS, DEFENSES
from buildings import MetalMine, CrystalMine, DeuteriumMine,\
    MetalStorage, CrystalStorage, DeuteriumStorage,\
    RoboticsFactory, Shipyard, NaniteFactory, ResearchLab, Terraformer


class Defense(EventDispatcher):
    costs = kp.DictProperty()
    def __init__(self, settings):
        super().__init__()
        print(settings)
        self.name = settings.get("name")
        self.costs = settings.get("costs")
        self.hull = settings.get("hull")
        self.shield = settings.get("shield")
        self.weapen = settings.get("weapen")
        self.time = settings.get("time")


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
    metal_cap0 = kp.NumericProperty(RESOURCES.get("metal").get("cap0"))
    crystal_cap0 = kp.NumericProperty(RESOURCES.get("metal").get("cap0"))
    deuterium_cap0 = kp.NumericProperty(RESOURCES.get("metal").get("cap0"))
    metal_cap = kp.NumericProperty(RESOURCES.get("metal").get("cap0"))
    crystal_cap = kp.NumericProperty(RESOURCES.get("metal").get("cap0"))
    deuterium_cap = kp.NumericProperty(RESOURCES.get("metal").get("cap0"))
    # buildings:
    metal_mine = kp.ObjectProperty(MetalMine(BUILDINGS.get("metal_mine")))
    crystal_mine = kp.ObjectProperty(CrystalMine(BUILDINGS.get("crystal_mine")))
    deuterium_mine = kp.ObjectProperty(DeuteriumMine(BUILDINGS.get("deuterium_mine")))
    metal_storage =\
        kp.ObjectProperty(MetalStorage(BUILDINGS.get("metal_storage")))
    crystal_storage =\
        kp.ObjectProperty(CrystalStorage(BUILDINGS.get("crystal_storage")))
    deuterium_storage =\
        kp.ObjectProperty(DeuteriumStorage(BUILDINGS.get("deuterium_storage")))
    robotics_factory =\
        kp.ObjectProperty(RoboticsFactory(BUILDINGS.get("robotics_factory")))
    shipyard =\
        kp.ObjectProperty(Shipyard(BUILDINGS.get("shipyard")))
    nanite_factory =\
        kp.ObjectProperty(NaniteFactory(BUILDINGS.get("nanite_factory")))
    research_lab =\
        kp.ObjectProperty(ResearchLab(BUILDINGS.get("research_lab")))
    terraformer =\
        kp.ObjectProperty(Terraformer(BUILDINGS.get("terraformer")))
    # construction:
    construction_building_name = kp.StringProperty()
    construction_time_left_s = kp.NumericProperty()
    construction_time_left = kp.StringProperty()
    construction_name = kp.StringProperty()
    metal_cost = kp.StringProperty()
    crystal_cost = kp.StringProperty()
    deuterium_cost = kp.StringProperty()
    time_cost = kp.StringProperty()
    # defenses:
    rocketlauncher =\
        kp.ObjectProperty(Defense(DEFENSES.get("rocketlauncher")))

    def build_config(self, *args):
        self.resources = {
            "metal": self.metal, "crystal": self.crystal,
            "deuterium": self.deuterium
        }
        self.buildings = [
            self.metal_mine, self.crystal_mine, self.deuterium_mine,
            self.metal_storage, self.crystal_storage, self.deuterium_storage,
            self.robotics_factory
        ]

    def build(self):
        Clock.schedule_interval(self.update, 0.1)
        self.game = Game()
        return self.game

    def display_costs(self, building):
        print("display_costs", building)
        self.construction_name = building.name
        self.metal_cost =  "metal: %s" % int(building.costs.get("metal"))
        self.crystal_cost =  "crystal: %s" % int(building.costs.get("crystal"))
        self.deuterium_cost =  "deuterium: %s" % int(building.costs.get("deuterium"))
        self.time_cost =  "time: %s" % int(building.time)

    def update(self, dt):
        # update resources:
        if self.metal + self.metal_per_s * dt <= self.metal_cap:
            self.metal += self.metal_per_s * dt
        else:
            self.metal = self.metal_cap
        if self.crystal + self.crystal_per_s * dt <= self.crystal_cap:
            self.crystal += self.crystal_per_s * dt
        else:
            self.crystal = self.crystal_cap
        if self.deuterium + self.deuterium_per_s * dt <= self.deuterium_cap:
            self.deuterium += self.deuterium_per_s * dt
        else:
            self.deuterium = self.deuterium_cap
    
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
