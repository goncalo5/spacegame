# kivy:
from kivy.app import App
from kivy.event import EventDispatcher
from kivy import properties as kp
from kivy.clock import Clock


class Construction(EventDispatcher):
    _id = kp.StringProperty()
    name = kp.StringProperty()
    time_left_s = kp.NumericProperty()
    time_left = kp.StringProperty()
    metal_cost = kp.StringProperty()
    crystal_cost = kp.StringProperty()
    deuterium_cost = kp.StringProperty()
    time_cost = kp.StringProperty()
    is_cancel = kp.BooleanProperty(False)
    current_selected = kp.ObjectProperty()
    defenses_queue = kp.ListProperty()
    defenses_queue_time = kp.NumericProperty()
    last_defense_time = kp.NumericProperty()
    # display
    have_textinput = kp.BooleanProperty(0)
    have_button = kp.BooleanProperty(0)
    # queue
    have_queue = kp.BooleanProperty(0)
    def __init__(self):
        super().__init__()

    def on_time_left_s(self, *args):
        self.time_left = "%s" % int(self.time_left_s)

    def display_costs(self, construction):
        print("display_costs", construction)
        self.current_selected = construction
        self.name = construction.name
        self._id = construction._id
        self.metal_cost =  "metal: %s" % int(construction.costs.get("metal"))
        self.crystal_cost =  "crystal: %s" % int(construction.costs.get("crystal"))
        self.deuterium_cost =  "deuterium: %s" % int(construction.costs.get("deuterium"))
        self.time_cost =  "time: %s" % int(construction.time)
        self.have_textinput = 1
        self.have_button = 1

    def upgrade(self, queue, input_text):
        print("upgrade Construction", self._id, input_text)
        self.app = App.get_running_app()
        try:
            construction = getattr(self.app, self._id)
        except AttributeError:
            return
        construction.upgrade(queue, input_text)


    def on_defenses_queue(self, *args):
        print("on_defense_queue", args)
        if len(self.defenses_queue) == 0:
            return
        # calc the time:
        print("self.defenses_queue", self.defenses_queue)
        if self.last_defense_time <= 0:
            self.last_defense_time = self.defenses_queue[0][0].time
            Clock.schedule_interval(self.update_first_defense_time_left, 0.1)
        self.defenses_queue_time = 0
        for defense, quantity in self.defenses_queue:
            self.defenses_queue_time += defense.time * quantity
        print("time", self.defenses_queue_time)
        # Clock.schedule_interval(self.update_defense_time_left, 0.1)
        self.defenses_queue_time -=\
            (self.defenses_queue[0][0].time - self.last_defense_time)
    
    def update_first_defense_time_left(self, dt):
        self.last_defense_time -= dt
        if self.last_defense_time <= 0:
            self.defenses_queue[0][0].n += 1
            self.defenses_queue[0][1] -= 1
            if self.defenses_queue[0][1] == 0:
                self.defenses_queue.pop(0)
            elif self.defenses_queue[0][1] > 0:
                self.last_defense_time = self.defenses_queue[0][0].time
                Clock.schedule_interval(self.update_first_defense_time_left, 0.1)

            return False

    def cancel(self):
        self.is_cancel = True

    def clean_display(self):
        self.name = ""
        self.metal_cost = ""
        self.crystal_cost = ""
        self.deuterium_cost = ""
        self.time_cost = ""
        self.have_textinput = 0
        self.have_button = 0