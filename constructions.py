# kivy:
from kivy.app import App
from kivy.event import EventDispatcher
from kivy import properties as kp
from kivy.clock import Clock


class Construction(EventDispatcher):
    # both:
    name = kp.StringProperty()
    # display:
    time_cost = kp.StringProperty()
    current_selected = kp.ObjectProperty()
    have_textinput = kp.BooleanProperty(0)
    have_button = kp.BooleanProperty(0)
    metal_cost = kp.StringProperty()
    crystal_cost = kp.StringProperty()
    deuterium_cost = kp.StringProperty()
    # queue:
    queue = kp.ListProperty()
    is_cancel = kp.BooleanProperty(False)
    name_in_queue = kp.StringProperty()
    have_queue = kp.BooleanProperty(0)
    time_left_s = kp.NumericProperty()
    queue_time = kp.NumericProperty()

    def __init__(self):
        super().__init__()

    def display_costs(self, construction):
        print("display_costs", construction)
        self.current_selected = construction
        self.name = construction.name
        self.metal_cost =  "metal: %s" % int(construction.costs.get("metal"))
        self.crystal_cost =  "crystal: %s" % int(construction.costs.get("crystal"))
        self.deuterium_cost =  "deuterium: %s" % int(construction.costs.get("deuterium"))
        self.time_cost =  "time: %s" % int(construction.time)
        self.have_textinput = 1
        self.have_button = 1

    def upgrade(self, construction, construction_queue, quantity=1):
        print("upgrade", self.name)
        self.construction = self.current_selected = construction
        self.construction_queue = construction_queue
        self.app = App.get_running_app()
        try:
            self.quantity = int(quantity)
        except ValueError:
            print("ValueError please input an integer")
            return
        if not self.app.check_if_can_pay(self.construction.costs, self.quantity):
            print("cant pay")
            return
        self.app.pay_the_resources(self.construction.costs, self.quantity)
        self.show_construction_queue()
        self.app.construction.name = self.name
        self.app.construction.queue.append([self.construction, int(quantity)])

    def show_construction_queue(self):
        print("show_construction_queue")
        self.construction_queue.size_hint_y = 0.1
        self.app.construction.have_queue = 1
        self.name_in_queue = self.construction.name

    def hide_construction_queue(self):
        print("hide_construction_queue")
        self.construction_queue.size_hint_y = None
        self.construction_queue.height = 0
        self.app.construction.have_queue = 0

    def on_queue(self, *args):
        print("on_queue", args)
        if len(self.queue) <= 0:
            self.hide_construction_queue()
            return
        # calc the time:
        print("self.queue", self.queue)
        if self.time_left_s <= 0:
            self.time_left_s = self.queue[0][0].time
            Clock.schedule_interval(self.update_time_left, 0.1)
    
    def update_time_left(self, dt):
        print("update_time_left")
        if self.app.construction.is_cancel:
            self.app.return_the_resources(self.construction.costs)
            self.hide_construction_queue()
            self.app.construction.is_cancel = False
            self.queue.pop(0)
            self.time_left_s = 0
            return False
        self.time_left_s -= dt
        if self.time_left_s <= 0:
            self.queue[0][0].upgraded()
            self.queue[0][1] -= 1
            if self.queue[0][1] == 0:
                self.queue.pop(0)
            elif self.queue[0][1] > 0:
                self.time_left_s = self.queue[0][0].time
                Clock.schedule_interval(self.update_time_left, 0.1)

            return False

    def on_time_left_s(self, *args):
        self.queue_time = 0
        for construction, quantity in self.queue:
            self.queue_time += construction.time * quantity
        self.queue_time -=\
            (self.queue[0][0].time - self.time_left_s)

    def cancel(self):
        print("cancel")
        self.is_cancel = True

    def clean_display(self):
        self.name = ""
        self.metal_cost = ""
        self.crystal_cost = ""
        self.deuterium_cost = ""
        self.time_cost = ""
        self.have_textinput = 0
        self.have_button = 0