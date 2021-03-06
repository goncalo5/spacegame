from functools import partial
# kivy:
from kivy.app import App
from kivy.event import EventDispatcher
from kivy import properties as kp
from kivy.clock import Clock


class Construction(EventDispatcher):
    # display:
    name = kp.StringProperty()
    time_cost = kp.StringProperty()
    current_selected = kp.ObjectProperty()
    have_textinput = kp.BooleanProperty(0)
    have_button = kp.BooleanProperty(0)
    metal_cost = kp.StringProperty()
    crystal_cost = kp.StringProperty()
    deuterium_cost = kp.StringProperty()
    # queue:
    all_queues = kp.ListProperty(
        ["buildings", "researches", "units"]
    )
    current_queue = kp.StringProperty("buildings")
    queue = kp.DictProperty({
        "buildings": [],
        "researches": [],
        "units": []
    })
    is_cancel = kp.DictProperty({
        "buildings": False,
        "researches": False,
        "units": False
    })
    name_in_queue = kp.DictProperty({
        "buildings": "",
        "researches": "",
        "units": ""
    })
    have_queue = kp.DictProperty({
        "buildings": 0,
        "researches": 0,
        "units": 0
    })
    time_left_s = kp.DictProperty({
        "buildings": 0,
        "researches": 0,
        "units": 0
    })
    queue_time = kp.DictProperty({
        "buildings": 0,
        "researches": 0,
        "units": 0
    })
    construction_queue = kp.DictProperty({
        "buildings": [],
        "researches": [],
        "units": []
    })

    def __init__(self):
        super().__init__()
        Clock.schedule_once(self.get_app, 0)

    def get_app(self, dt):
        self.app = App.get_running_app()

    def change_screen(self, queue_name, construction_queue):
        print("change_screen", queue_name, construction_queue)
        self.current_queue = queue_name
        if construction_queue not in self.construction_queue[queue_name]:
            self.construction_queue[queue_name].append(construction_queue)
        print("self.construction_queue", self.construction_queue)
        self.update_if_have_queue()

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

    def check_if_it_have_the_necessary_requirements(self, construction):
        print("check_if_it_have_the_necessary_requirements")
        if not construction.requirements:
            return True
        for requirement_name, requirement_level in construction.requirements:
            print(requirement_name, requirement_level)
            requirement = getattr(self.app, requirement_name)
            print(requirement.level, requirement_level)
            if requirement_level > requirement.level:
                print("False")
                return False
        print("True", construction.requirements)
        return True

    def upgrade(self, construction, construction_queue, quantity=1):
        print("upgrade", self.name)
        self.construction = self.current_selected = construction
        if not self.check_if_it_have_the_necessary_requirements(construction):
            return
        try:
            self.quantity = int(quantity)
        except ValueError:
            print("ValueError please input an integer")
            return
        if not self.app.check_if_can_pay(self.construction.costs, self.quantity):
            print("cant pay")
            return
        self.app.pay_the_resources(self.construction.costs, self.quantity)
        self.app.construction.name = self.name
        queue_name = self.construction.queue
        queue = self.queue[queue_name]
        to_add = [self.construction, int(quantity)]
        queue.append(to_add)
        self.on_queue(queue_name)

    def update_if_have_queue(self):
        print("update_if_have_queue", self.all_queues)
        for queue_name in self.all_queues:
            print(queue_name)
            if self.queue[queue_name]:
                self.app.construction.have_queue[queue_name] = 1
                self.show_construction_queue(queue_name)
            else:
                self.app.construction.have_queue[queue_name] = 0
                self.hide_construction_queue(queue_name)
        print(self.have_queue)

    def show_construction_queue(self, queue_name):
        print("show_construction_queue", queue_name)
        if not self.construction_queue[queue_name]:
            return
        if not self.queue[queue_name]:
            return
        print("self.construction_queue", self.construction_queue)
        for construction_queue in self.construction_queue[queue_name]:
            construction_queue.size_hint_y = 0.1
        self.name_in_queue[queue_name] = self.queue[queue_name][0][0].name
        print("end show_construction_queue")

    def hide_construction_queue(self, queue_name):
        print("hide_construction_queue")
        if not self.construction_queue[queue_name]:
            return
        for construction_queue in self.construction_queue[queue_name]:
            construction_queue.size_hint_y = None
            construction_queue.height = 0

    def on_queue(self, *args):
        print("on_queue", args)
        queue_name = args[0]
        self.update_if_have_queue()
        if len(self.queue[queue_name]) == 0:
            return
        # calc the time:
        print("self.queue", self.queue[queue_name])
        if self.time_left_s[queue_name] <= 0:
            self.time_left_s[queue_name] = self.queue[queue_name][0][0].time
            Clock.schedule_interval(partial(self.update_time_left, queue_name), 0.1)
    
    def update_time_left(self, queue_name, dt):
        # print("update_time_left", queue_name, dt)
        if self.app.construction.is_cancel[queue_name]:
            self.app.return_the_resources(self.construction.costs)
            self.app.construction.is_cancel[queue_name] = False
            self.time_left_s[queue_name] = 0
            self.queue[queue_name].pop(0)
            self.on_queue(queue_name)
            return False
        self.time_left_s[queue_name] -= dt
        if self.time_left_s[queue_name] <= 0:
            self.queue[queue_name][0][0].upgraded()
            self.queue[queue_name][0][1] -= 1
            if self.queue[queue_name][0][1] == 0:
                self.queue[queue_name].pop(0)
                self.on_queue(queue_name)
            elif self.queue[queue_name][0][1] > 0:
                self.time_left_s[queue_name] = self.queue[queue_name][0][0].time
                Clock.schedule_interval(partial(self.update_time_left, queue_name), 0.1)
            return False

    def on_time_left_s(self, *args):
        # print("on_time_left_s")
        for queue_name in ["buildings", "researches", "units"]:
            if self.queue[queue_name] == []:
                continue
            self.queue_time[queue_name] = 0
            for construction, quantity in self.queue[queue_name]:
                self.queue_time[queue_name] += construction.time * quantity
            self.queue_time[queue_name] -=\
                (self.queue[queue_name][0][0].time - self.time_left_s[queue_name])

    def cancel(self, queue_name):
        print("cancel")
        self.is_cancel[queue_name] = True

    def clean_display(self):
        self.name = ""
        self.metal_cost = ""
        self.crystal_cost = ""
        self.deuterium_cost = ""
        self.time_cost = ""
        self.have_textinput = 0
        self.have_button = 0