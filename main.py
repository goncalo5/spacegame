# kivy:
from kivy.app import App
from kivy.core.window import Window
from kivy import properties as kp
from kivy.clock import Clock
from kivy.event import EventDispatcher
# kivy.uix:
from kivy.uix.screenmanager import ScreenManager
# mine:
from settings import RESOURCES, DEFENSES
from buildings import MetalMine, CrystalMine, DeuteriumMine,\
    MetalStorage, CrystalStorage, DeuteriumStorage,\
    RoboticsFactory, Shipyard, NaniteFactory, ResearchLab, Terraformer
from resources import Resource
from constructions import Construction


class Defense(EventDispatcher):
    costs = kp.DictProperty()
    n = kp.NumericProperty()
    def __init__(self, settings):
        super().__init__()
        print(settings)
        self.name = settings.get("name")
        self.costs = settings.get("costs")
        self.hull = settings.get("hull")
        self.shield = settings.get("shield")
        self.weapen = settings.get("weapen")
        self.time = settings.get("time")

    def __str__(self):
        return "Defense(name=%s)" % self.name

    def on_n(self, *args):
        print("on_n")


class Game(ScreenManager):
    pass


class GameApp(App, ScreenManager):
    window = kp.ObjectProperty(Window)
    # resources:
    metal = kp.ObjectProperty(Resource("metal"))
    crystal = kp.ObjectProperty(Resource("crystal"))
    deuterium = kp.ObjectProperty(Resource("deuterium"))
    # buildings:
    metal_mine = kp.ObjectProperty(MetalMine())
    crystal_mine = kp.ObjectProperty(CrystalMine())
    deuterium_mine = kp.ObjectProperty(DeuteriumMine())
    metal_storage = kp.ObjectProperty(MetalStorage())
    crystal_storage = kp.ObjectProperty(CrystalStorage())
    deuterium_storage = kp.ObjectProperty(DeuteriumStorage())
    robotics_factory = kp.ObjectProperty(RoboticsFactory())
    shipyard = kp.ObjectProperty(Shipyard())
    nanite_factory = kp.ObjectProperty(NaniteFactory())
    research_lab = kp.ObjectProperty(ResearchLab())
    terraformer = kp.ObjectProperty(Terraformer())
    # construction:
    construction = kp.ObjectProperty(Construction())
    # defenses:
    rocketlauncher =\
        kp.ObjectProperty(Defense(DEFENSES.get("rocketlauncher")))

    def build_config(self, *args):
        self.resources = [
            self.metal.current, self.crystal, self.deuterium
        ]
        self.buildings = [
            self.metal_mine, self.crystal_mine, self.deuterium_mine,
            self.metal_storage, self.crystal_storage, self.deuterium_storage,
            self.robotics_factory
        ]

    def build(self):
        Clock.schedule_interval(self.update, 0.1)
        Clock.schedule_interval(self.update_defense_time_left, 0.1)
        self.game = Game()
        return self.game

    def update(self, dt):
        # update resources:
        if self.metal.current + self.metal.per_s * dt <= self.metal.cap:
            self.metal.current += self.metal.per_s * dt
        else:
            self.metal = self.metal.cap
        if self.crystal.current + self.crystal.per_s * dt <= self.crystal.cap:
            self.crystal.current += self.crystal.per_s * dt
        else:
            self.crystal.current = self.crystal.cap
        if self.deuterium.current + self.deuterium.per_s * dt <= self.deuterium.cap:
            self.deuterium.current += self.deuterium.per_s * dt
        else:
            self.deuterium.current = self.deuterium.cap
    
    def check_if_can_pay(self, resources, quantity=1):
        # check if can pay:
        if self.metal.current < (resources["metal"] * quantity) or\
            self.crystal.current < (resources["crystal"] * quantity) or\
            self.deuterium.current < (resources["deuterium"] * quantity):
            return False
        return True

    def pay_the_resources(self, resources, quantity=1):
        self.metal.current -= resources["metal"] * quantity
        self.crystal.current -= resources["crystal"] * quantity
        self.deuterium.current -= resources["deuterium"] * quantity

    def return_the_resources(self, resources):
        self.metal.current += resources["metal"]
        self.crystal.current += resources["crystal"]
        self.deuterium.current += resources["deuterium"]

    def cancel_construction(self):
        self.construction_is_cancel = True
    
    def construct_defense(self, quantity):
        print("construct_defense")
        try:
            quantity = int(quantity)
        except ValueError:
            print("ValueError please input an integer")
            return
        try:
            # check if can pay:
            print(self.construction.current_selected.costs)
            costs = self.construction.current_selected.costs
            if self.check_if_can_pay(costs, quantity):
                print("can pay")
                self.pay_the_resources(costs, quantity)
            else:
                print("cant pay")
                return
        except AttributeError:
            return

        self.construction.defenses_queue.append([self.construction.current_selected, int(quantity)])
        print(self.construction.defenses_queue)

    
    def update_defense_time_left(self, dt):
        if self.construction.defenses_queue_time <= 0:
            return
        self.construction.defenses_queue_time -= dt



if __name__ == "__main__":
    GameApp().run()
