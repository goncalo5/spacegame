# kivy:
from kivy.app import App
from kivy.core.window import Window
from kivy import properties as kp
from kivy.clock import Clock
from kivy.event import EventDispatcher
# kivy.uix:
from kivy.uix.screenmanager import ScreenManager
# mine:
from buildings import MetalMine, CrystalMine, DeuteriumMine,\
    MetalStorage, CrystalStorage, DeuteriumStorage,\
    RoboticsFactory, Shipyard, NaniteFactory, ResearchLab, Terraformer
from resources import Resource
from constructions import Construction
from units import Defense, Ship
from researches import Research


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
    # Ships:
    light_fighter = kp.ObjectProperty(Ship("light_fighter"))
    heavy_fighter = kp.ObjectProperty(Ship("heavy_fighter"))
    cruiser = kp.ObjectProperty(Ship("cruiser"))
    battleship = kp.ObjectProperty(Ship("battleship"))
    battlecruiser = kp.ObjectProperty(Ship("battlecruiser"))
    bomber = kp.ObjectProperty(Ship("bomber"))
    destroyer = kp.ObjectProperty(Ship("destroyer"))
    deathstar = kp.ObjectProperty(Ship("deathstar"))
    small_cargo_ship = kp.ObjectProperty(Ship("small_cargo_ship"))
    large_cargo_ship = kp.ObjectProperty(Ship("large_cargo_ship"))
    colony_ship = kp.ObjectProperty(Ship("colony_ship"))
    recycler = kp.ObjectProperty(Ship("recycler"))
    espionage_probe = kp.ObjectProperty(Ship("espionage_probe"))
    solar_satellite = kp.ObjectProperty(Ship("solar_satellite"))

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
        self.ships = [
            self.light_fighter, self.heavy_fighter, self.cruiser, self.battleship,
            self.battlecruiser, self.bomber, self.destroyer, self.deathstar,
            self.small_cargo_ship, self.large_cargo_ship, self.colony_ship,
            self.recycler, self.espionage_probe, self.solar_satellite
        ]

    def build(self):
        Clock.schedule_interval(self.update, 0.1)
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


if __name__ == "__main__":
    GameApp().run()
