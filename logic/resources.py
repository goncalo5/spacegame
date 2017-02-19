import time
import database
import constants


class Resource(object):
    def __init__(self, name):
        self.name = name

        # Null variables
        self.total = None
        self.per_s = None

        # initial methods
        self.see_total_in_db()
        self.calculate_per_s()

    # calculators
    def calculate_per_s(self):
        self.per_s = 1

    # Data Base
    # GET
    def see_total_in_db(self):
        self.total = database.RESOURCES[self.name]

    # PUT
    def save_total_in_db(self):
        database.BUILDINGS[self.name]['total'] = self.total

    def updating_total_in_db(self):
        self.save_total_in_db()
        time.sleep(constants.TIME2UPDATE_DB)
        self.updating_total_in_db()
