# resources
RESOURCES = {'metal': {'total': 1000, 'per_s': 1, 'rate_per_s': 1.5},
             'crystal': {'total': 500, 'per_s': 1, 'rate_per_s': 1.3}}

# buildings
BUILDINGS = {'metal_mine': {'cost': 10, 'rate_cost': 1.5, 'time': 5, 'rate_time': 2},
             'robot_factory': {'cost': 10, 'rate_cost': 2, 'time': 5, 'rate_time': 2}}


# effects BUILDINGS[TIME] /= 2
RATE_FB = 2

# times
TIME2UPDATE_DB = 10
TIME2REFRESH = 3
