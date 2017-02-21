import time
import database
import constants


class Resource(object):
    def __init__(self, name):
        self.name = name

        # Null variables
        self.total = self.per_s = None

        # constants
        self.per_s0 = self.per_s = constants.RESOURCES[self.name]['per_s']
        self.rate_per_s = constants.RESOURCES[self.name]['rate_per_s']

        # initial methods
        self.see_total_in_db()

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
