# kivy:
from kivy.app import App
from kivy.event import EventDispatcher
from kivy import properties as kp
from kivy.clock import Clock


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
        print("construction_queue.cancel_construction",
            construction_queue.cancel_construction)
        self.construction_queue = construction_queue
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
        if self.app.construction_is_cancel:
            self.app.return_the_resources(self.costs)
            self.hide_construction_queue()
            self.app.construction_is_cancel = False
            return False

        self.app.construction_time_left_s -= dt
        if self.app.construction_time_left_s <= 0:
            self.level += 1
            self.hide_construction_queue()
            self.app.display_costs(self)
            return False
    
    def hide_construction_queue(self):
        self.construction_queue.size_hint_y = None
        self.construction_queue.height = 0
        self.app.construction_building_name = ""
        self.app.construction_time_left = ""


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
        self.app.metal.per_s =\
            self.app.metal.per_s0 * self.metal_rate ** self.level


class CrystalMine(Building):
    def __init__(self, settings):
        super().__init__(settings)
        self.crystal_rate = settings.get("crystal_rate")

    def update_feature(self, *args):
        self.app = App.get_running_app()
        self.app.crystal.per_s =\
            self.app.crystal.per_s0 * self.crystal_rate ** self.level


class DeuteriumMine(Building):
    def __init__(self, settings):
        super().__init__(settings)
        self.deuterium_rate = settings.get("deuterium_rate")

    def update_feature(self, *args):
        self.app = App.get_running_app()
        self.app.deuterium.per_s =\
            self.app.deuterium.per_s0 * self.deuterium_rate ** self.level


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
        self.app.metal.cap =\
            self.app.metal.cap0 * self.metal_rate ** self.level


class CrystalStorage(Storage):
    def __init__(self, settings):
        super().__init__(settings)
        self.crystal_rate = settings.get("crystal_rate")

    def update_feature(self, *args):
        self.app = App.get_running_app()
        self.app.crystal.cap =\
            self.app.crystal.cap0 * self.crystal_rate ** self.level


class DeuteriumStorage(Storage):
    def __init__(self, settings):
        super().__init__(settings)
        self.deuterium_rate = settings.get("deuterium_rate")

    def update_feature(self, *args):
        self.app = App.get_running_app()
        self.app.deuterium.cap =\
            self.app.deuterium.cap0 * self.deuterium_rate ** self.level


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
