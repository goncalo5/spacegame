from kivy.app import App
from kivy import properties as kp
from kivy.clock import Clock
from kivy.event import EventDispatcher
# uix:
from kivy.uix.screenmanager import ScreenManager
# mine:
from settings import RESOURCES, BUILDINGS


class Building(EventDispatcher):
    def __init__(self, settings):
        super().__init__()
        self.cost0 = settings.get("cost0")
        self.cost_rate = settings.get("cost_rate")


class Game(ScreenManager):
    pass


class GameApp(App):
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

    def build(self):
        Clock.schedule_interval(self.update, 0.1)
        return Game()

    def update(self, dt):
        # update resources:
        self.metal += self.metal_per_s * dt
        

if __name__ == "__main__":
    GameApp().run()
