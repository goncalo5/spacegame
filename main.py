from kivy.app import App
from kivy.core.window import Window
from kivy import properties as kp
from kivy.clock import Clock
from kivy.event import EventDispatcher
# uix:
from kivy.uix.screenmanager import ScreenManager
# mine:
from settings import RESOURCES, BUILDINGS, DEFENSES


class Building(EventDispatcher):
    name = kp.StringProperty()
    level = kp.NumericProperty()
    costs = kp.DictProperty()
    time = kp.NumericProperty()
    def __init__(self, settings):
        super().__init__()
        self.name = settings.get("name")
        self.level = settings.get("level", 0)
        self.costs0 = settings.get("costs0")
        self.costs_rate = settings.get("costs_rate")
        self.time0 = settings.get("time0")
        self.time_rate = settings.get("time_rate")

        Clock.schedule_once(self.on_level, 0)

    def upgrade(self, construction_queue):
        print("upgrade", construction_queue)
        self.construction_queue = construction_queue
        self.app = App.get_running_app()
        if not self.app.check_if_can_pay(self.costs):
            return
        self.app.pay_the_resources(self.costs)
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
        self.costs["metal"] = self.costs0["metal"] * self.costs_rate ** self.level
        self.costs["crystal"] =\
            self.costs0["crystal"] * self.costs_rate ** self.level
        self.costs["deuterium"] =\
            self.costs0["deuterium"] * self.costs_rate ** self.level
        self.update_time()
        Clock.schedule_once(self.update_feature, 0)

    def update_time(self):
        # update time:
        print("time", self.time)
        print(self.app.robotics_factory.building_time_factor)
        print(self.app.robotics_factory.level)
        robotics_factory_factor =\
            self.app.robotics_factory.building_time_factor **\
                self.app.robotics_factory.level
        nanite_factory_factor =\
            self.app.nanite_factory.building_time_factor **\
                self.app.nanite_factory.level
        self.time = self.time0 * self.time_rate ** self.level *\
            robotics_factory_factor * nanite_factory_factor
        print("time", self.time, robotics_factory_factor)


    def update_feature(self, *args):
        pass


class Mine(Building):
    def __init__(self, settings):
        super().__init__(settings)


class MetalMine(Mine):
    def __init__(self, settings):
        self.metal_rate = settings.get("metal_rate")
        super().__init__(settings)

    def update_feature(self, *args):
        self.app = App.get_running_app()
        self.app.metal_per_s =\
            self.app.metal_per_s0 * self.metal_rate ** self.level


class CrystalMine(Building):
    def __init__(self, settings):
        super().__init__(settings)
        self.crystal_rate = settings.get("crystal_rate")

    def update_feature(self, *args):
        self.app = App.get_running_app()
        self.app.crystal_per_s =\
            self.app.crystal_per_s0 * self.crystal_rate ** self.level


class DeuteriumMine(Building):
    def __init__(self, settings):
        super().__init__(settings)
        self.deuterium_rate = settings.get("deuterium_rate")

    def update_feature(self, *args):
        self.app = App.get_running_app()
        self.app.deuterium_per_s =\
            self.app.deuterium_per_s0 * self.deuterium_rate ** self.level


class Storage(Building):
    pass


class MetalStorage(Storage):
    def __init__(self, settings):
        print("settings", settings)
        super().__init__(settings)
        self.metal_rate = settings.get("metal_rate")
        print("self.metal_rate", self.metal_rate)

    def update_feature(self, *args):
        self.app = App.get_running_app()
        self.app.metal_cap =\
            self.app.metal_cap0 * self.metal_rate ** self.level


class CrystalStorage(Storage):
    def __init__(self, settings):
        super().__init__(settings)
        self.crystal_rate = settings.get("crystal_rate")

    def update_feature(self, *args):
        self.app = App.get_running_app()
        self.app.crystal_cap =\
            self.app.crystal_cap0 * self.crystal_rate ** self.level


class DeuteriumStorage(Storage):
    def __init__(self, settings):
        super().__init__(settings)
        self.deuterium_rate = settings.get("deuterium_rate")

    def update_feature(self, *args):
        self.app = App.get_running_app()
        self.app.deuterium_cap =\
            self.app.deuterium_cap0 * self.deuterium_rate ** self.level


class Factory(Building):
    def __init__(self, settings):
        super().__init__(settings)
        self.update_factor()
        Clock.schedule_once(self.update_feature, 0)

    def update_factor(self):
        self.building_time_factor = self.building_time_factor0 ** self.level


class RoboticsFactory(Factory):
    def __init__(self, settings):
        self.building_time_factor0 = settings.get("building_time_factor0")
        super().__init__(settings)

    def update_feature(self, *args):
        self.app = App.get_running_app()
        self.building_time_factor = self.building_time_factor0 ** self.level
        for building in self.app.buildings:
            building.update_time()


class Shipyard(Factory):
    def __init__(self, settings):
        self.building_time_factor0 = settings.get("building_time_factor0")
        super().__init__(settings)

    def update_feature(self, *args):
        self.app = App.get_running_app()
        self.building_time_factor = self.building_time_factor0 ** self.level
        for building in self.app.buildings:
            building.update_time()


class NaniteFactory(Factory):
    def __init__(self, settings):
        self.building_time_factor0 = settings.get("building_time_factor0")
        super().__init__(settings)

    def update_feature(self, *args):
        self.app = App.get_running_app()
        for building in self.app.buildings:
            building.update_time()


class ResearchLab(Building):
    def __init__(self, settings):
        super().__init__(settings)
        self.reasearch_time_factor0 = settings.get("reasearch_time_factor0")
        self.update_factor()

    def update_factor(self):
        self.reasearch_time_factor =\
            self.reasearch_time_factor0 ** self.level

    def update_feature(self, *args):
        self.app = App.get_running_app()


class Terraformer(Building):
    def __init__(self, settings):
        super().__init__(settings)
        self.fields_added_per_level = settings.get("fields_added_per_level")
        self.update_factor()

    def update_factor(self):
        self.fields_added =\
            self.fields_added_per_level * self.level

    def update_feature(self, *args):
        self.app = App.get_running_app()


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
