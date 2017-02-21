import constants
from machines import Defense


class Planet(object):
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.empty = True
        self.star_distance = self.coordinates['planet'] + 1
        self.total_fields = self.star_distance * \
                            constants.UNIVERSE['planet']['rate_field'] + \
                            constants.UNIVERSE['planet']['fields']
        self.fields_left = self.total_fields
        self.fields_occupied = 0
        self.defenses = {}
        for i, defense in enumerate(constants.DEFENSES):
            new = Defense(defense)
            self.defenses[new.name] = new
            self.defenses[new.name].n = 0

        def occupy1field(self):
            self.field_left -= 1
            self.fields_ocupided += 1

        def leave1field(self):
            self.field_left += 1
            self.fields_ocupided -= 1
