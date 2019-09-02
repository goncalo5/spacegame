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
from researches import Research


class Defense(EventDispatcher):
    costs = kp.DictProperty()
    n = kp.NumericProperty()
    def __init__(self, defense_name):
        super().__init__()
        self._id = defense_name
        self.settings = DEFENSES.get(defense_name)
        self.name = self.settings.get("name")
        self.costs = self.settings.get("costs")
        self.hull = self.settings.get("hull")
        self.shield = self.settings.get("shield")
        self.weapen = self.settings.get("weapen")
        self.time = self.settings.get("time")

    def __str__(self):
        return "Defense(name=%s)" % self.name

    def on_n(self, *args):
        print("on_n")

    def upgrade(self, queue):
        return


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
    rocketlauncher = kp.ObjectProperty(Defense("rocketlauncher"))
    light_laser = kp.ObjectProperty(Defense("light_laser"))
    heavy_laser = kp.ObjectProperty(Defense("heavy_laser"))
    ion_cannon = kp.ObjectProperty(Defense("ion_cannon"))
    gauss_cannon = kp.ObjectProperty(Defense("gauss_cannon"))
    plasma_turret = kp.ObjectProperty(Defense("plasma_turret"))
    small_shield_dome = kp.ObjectProperty(Defense("small_shield_dome"))
    large_shield_dome = kp.ObjectProperty(Defense("large_shield_dome"))
    # Research:
    energy_technology = kp.ObjectProperty(Research("energy_technology"))
    laser_technology = kp.ObjectProperty(Research("laser_technology"))
    ion_technology = kp.ObjectProperty(Research("ion_technology"))
    hyperspace_technology = kp.ObjectProperty(Research("hyperspace_technology"))
    plasma_technology = kp.ObjectProperty(Research("plasma_technology"))
    combustion_drive = kp.ObjectProperty(Research("combustion_drive"))
    impulse_drive = kp.ObjectProperty(Research("impulse_drive"))
    hyperspace_drive = kp.ObjectProperty(Research("hyperspace_drive"))
    espionage_technology = kp.ObjectProperty(Research("espionage_technology"))
    computer_technology = kp.ObjectProperty(Research("computer_technology"))
    astrophysics = kp.ObjectProperty(Research("astrophysics"))
    intergalactic_research_network = kp.ObjectProperty(Research("intergalactic_research_network"))
    graviton_technology = kp.ObjectProperty(Research("graviton_technology"))
    armour_technology = kp.ObjectProperty(Research("armour_technology"))
    weapons_technology = kp.ObjectProperty(Research("weapons_technology"))
    shielding_technology = kp.ObjectProperty(Research("shielding_technology"))


    def build_config(self, *args):
        self.resources = [
            self.metal, self.crystal, self.deuterium
        ]
        self.buildings = [
            self.metal_mine, self.crystal_mine, self.deuterium_mine,
            self.metal_storage, self.crystal_storage, self.deuterium_storage,
            self.robotics_factory
        ]
        self.defenses = [
            self.rocketlauncher, self.light_laser, self.heavy_laser,
            self.ion_cannon, self.gauss_cannon, self.plasma_turret,
            self.small_shield_dome, self.large_shield_dome
        ]
        self.researches = [
            self.energy_technology, self.laser_technology, self.ion_technology,
            self.hyperspace_technology, self.plasma_technology, self.combustion_drive,
            self.impulse_drive, self.hyperspace_drive, self.espionage_technology, self.computer_technology,
            self.astrophysics, self.intergalactic_research_network, self.graviton_technology,
            self.armour_technology, self.weapons_technology, self.shielding_technology
        ]

    def build(self):
        Clock.schedule_interval(self.update, 0.1)
        Clock.schedule_interval(self.update_defense_time_left, 0.1)
        self.game = Game()
        return self.game

    def update(self, dt):
        # update resources:
        for resource in self.resources:
            if resource.current + resource.per_s * dt <= resource.cap:
                resource.current += resource.per_s * dt
            else:
                resource = resource.cap
    
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
