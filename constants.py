# resources
RESOURCES = {'metal': {'total': 1000, 'per_s': 1, 'rate_per_s': 2},
             'crystal': {'total': 500, 'per_s': 1, 'rate_per_s': 1.5}}

# buildings
BUILDINGS = {'metal_mine': {'cost': 10, 'rate_cost': 1.5, 'time': 5, 'rate_time': 1.5},
             'robot_factory': {'cost': 10, 'rate_cost': 2, 'time': 5, 'rate_time': 1.5}}


# effects BUILDINGS[TIME] /= 2
RATE_FB = 2

# times
TIME2UPDATE_DB = 10
TIME2REFRESH = 3
