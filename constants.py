# resources
RESOURCES = {'metal': {'total': 1000, 'per_s': 5, 'rate_per_s': 2},
             'crystal': {'total': 500, 'per_s': 1, 'rate_per_s': 1.5}}

# buildings
BUILDINGS = {'metal_mine': {'cost': 10, 'rate_cost': 1.5, 'time': 3, 'rate_time': 1.5,
                             'type': 'mine'},
             'metal_wharehouse': {'cost': 10, 'rate_cost': 2, 'time': 3, 'rate_time': 1.5,
                                  'type': 'storage', 'capacity': 1500, 'rate_capacity': 1.5},
             'robot_factory': {'cost': 10, 'rate_cost': 2, 'time': 3, 'rate_time': 1.5,
                               'type': 'factory', 'factor': 2, 'rate_factor': 2}}

UNIVERSE = {'planet': {'fields': 100, 'rate_field': 1.5}}

SPACESHIPS = {'light_fighter', 'heavy_fighter', 'cruiser', 'battleship',
              'battlecruiser', 'bomber', 'destroyer', 'deathstar'
              'small_cargo', 'large_cargo', 'colony_ship',
              'recycler', 'espionage_probe', 'solar_satellite'}

DEFESENSES = {'rocket_launcher', 'light_laser', 'heavy_laser',
              'gauss_cannon', 'ion_cannon', 'plasma_turret',
              'small_shield_dome', 'large_shield_dome',
              'anti_ballistic_missiles', 'interplanetary_missiles'}
# times
TIME2UPDATE_DB = 10
TIME2REFRESH = 3
