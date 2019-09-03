# kivy:
from kivy.app import App
from kivy.event import EventDispatcher
from kivy import properties as kp
from kivy.clock import Clock
# mine:
from settings import BUILDINGS


class UpgradingEvent(EventDispatcher):
    name = kp.StringProperty()
    level = kp.NumericProperty()
    costs = kp.DictProperty()
    time = kp.NumericProperty()

    # def upgrade(self, construction_queue, quantity=1):
    #     print("upgrade", self.name)
    #     self.construction_queue = construction_queue
    #     self.app = App.get_running_app()
    #     if not self.app.check_if_can_pay(self.costs):
    #         print("cant pay")
    #         return
    #     self.app.pay_the_resources(self.costs)
    #     self.show_construction_queue()
    #     self.app.construction.name = self.name
    #     self.app.construction.time_left_s = self.time
    #     Clock.schedule_interval(self.update_time_left, 0.1)

    # def update_time_left(self, dt):
    #     if self.app.construction.is_cancel:
    #         self.app.return_the_resources(self.costs)
    #         self.hide_construction_queue()
    #         self.app.construction.is_cancel = False
    #         return False
    #     self.app.construction.time_left_s -= dt
    #     if self.app.construction.time_left_s <= 0:
    #         self.level += 1
    #         self.hide_construction_queue()
    #         self.app.construction.display_costs(self)
    #         return False

    # def show_construction_queue(self):
    #     print("show_construction_queue")
    #     self.construction_queue.size_hint_y = 0.1
    #     self.app.construction.have_queue = 1

    # def hide_construction_queue(self):
    #     print("hide_construction_queue")
    #     self.construction_queue.size_hint_y = None
    #     self.construction_queue.height = 0
    #     self.app.construction.have_queue = 0

    def upgraded(self):
        self.level += 1

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

    def update_feature(self, *args):
        pass


class Building(UpgradingEvent):
    def __init__(self):
        super().__init__()
        self.settings = BUILDINGS.get(self._id)
        self.name = self.settings.get("name")
        self.level = self.settings.get("level", 0)
        self.costs0 = self.settings.get("costs0")
        self.costs_rate = self.settings.get("costs_rate")
        self.time0 = self.settings.get("time0")
        self.time_rate = self.settings.get("time_rate")

        Clock.schedule_once(self.on_level, 0)

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


class Mine(Building):
    def __init__(self):
        super().__init__()


class MetalMine(Mine):
    def __init__(self):
        self._id = "metal_mine"
        super().__init__()
        self.metal_rate = self.settings.get("metal_rate")

    def update_feature(self, *args):
        self.app = App.get_running_app()
        self.app.metal.per_s =\
            self.app.metal.per_s0 * self.metal_rate ** self.level


class CrystalMine(Building):
    def __init__(self):
        self._id = "crystal_mine"
        super().__init__()
        self.crystal_rate = self.settings.get("crystal_rate")

    def update_feature(self, *args):
        self.app = App.get_running_app()
        self.app.crystal.per_s =\
            self.app.crystal.per_s0 * self.crystal_rate ** self.level


class DeuteriumMine(Building):
    def __init__(self):
        self._id = "deuterium_mine"
        super().__init__()
        self.deuterium_rate = self.settings.get("deuterium_rate")

    def update_feature(self, *args):
        self.app = App.get_running_app()
        self.app.deuterium.per_s =\
            self.app.deuterium.per_s0 * self.deuterium_rate ** self.level


class Storage(Building):
    pass


class MetalStorage(Storage):
    def __init__(self):
        self._id = "metal_storage"
        super().__init__()
        self.metal_rate = self.settings.get("metal_rate")

    def update_feature(self, *args):
        self.app = App.get_running_app()
        self.app.metal.cap =\
            self.app.metal.cap0 * self.metal_rate ** self.level


class CrystalStorage(Storage):
    def __init__(self):
        self._id = "crystal_storage"
        super().__init__()
        self.crystal_rate = self.settings.get("crystal_rate")

    def update_feature(self, *args):
        self.app = App.get_running_app()
        self.app.crystal.cap =\
            self.app.crystal.cap0 * self.crystal_rate ** self.level


class DeuteriumStorage(Storage):
    def __init__(self):
        self._id = "deuterium_storage"
        super().__init__()
        self.deuterium_rate = self.settings.get("deuterium_rate")

    def update_feature(self, *args):
        self.app = App.get_running_app()
        self.app.deuterium.cap =\
            self.app.deuterium.cap0 * self.deuterium_rate ** self.level


class Factory(Building):
    def __init__(self):
        super().__init__()
        self.building_time_factor0 = self.settings.get("building_time_factor0")
        self.update_factor()
        Clock.schedule_once(self.update_feature, 0)

    def update_factor(self):
        self.building_time_factor = self.building_time_factor0 ** self.level


class RoboticsFactory(Factory):
    def __init__(self):
        self._id = "robotics_factory"
        super().__init__()

    def update_feature(self, *args):
        self.app = App.get_running_app()
        self.building_time_factor = self.building_time_factor0 ** self.level
        for building in self.app.buildings:
            building.update_time()


class Shipyard(Factory):
    def __init__(self):
        self._id = "shipyard"
        super().__init__()

    def update_feature(self, *args):
        self.app = App.get_running_app()
        self.building_time_factor = self.building_time_factor0 ** self.level
        for building in self.app.buildings:
            building.update_time()


class NaniteFactory(Factory):
    def __init__(self):
        self._id = "nanite_factory"
        super().__init__()

    def update_feature(self, *args):
        self.app = App.get_running_app()
        for building in self.app.buildings:
            building.update_time()


class ResearchLab(Building):
    def __init__(self):
        self._id = "research_lab"
        super().__init__()
        self.reasearch_time_factor0 = self.settings.get("reasearch_time_factor0")
        self.update_factor()

    def update_factor(self):
        self.reasearch_time_factor =\
            self.reasearch_time_factor0 ** self.level

    def update_feature(self, *args):
        self.app = App.get_running_app()


class Terraformer(Building):
    def __init__(self):
        self._id = "terraformer"
        super().__init__()
        self.fields_added_per_level = self.settings.get("fields_added_per_level")
        self.update_factor()

    def update_factor(self):
        self.fields_added =\
            self.fields_added_per_level * self.level

    def update_feature(self, *args):
        self.app = App.get_running_app()
