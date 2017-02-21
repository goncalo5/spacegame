# resources
RESOURCES = {'metal': {'total': 1000, 'per_s': 5, 'rate_per_s': 2},
             'crystal': {'total': 500, 'per_s': 1, 'rate_per_s': 1.5}}

# buildings
BUILDINGS = {'metal_mine': {'cost': 10, 'rate_cost': 1.5, 'time': 3, 'rate_time': 1.5,
                            'type': 'mine'},
             'metal_storage': {'cost': 10, 'rate_cost': 2, 'time': 3, 'rate_time': 1.5,
                               'type': 'storage', 'capacity': 1500, 'rate_capacity': 1.5},
             'robot_factory': {'cost': 10, 'rate_cost': 2, 'time': 3, 'rate_time': 1.5,
                               'type': 'factory', 'factor': 2, 'rate_factor': 2}}

UNIVERSE = {'planet': {'fields': 100, 'rate_field': 1.5}}

SPACESHIPS = {'light_fighter': {'cost': {'metal': 3000, 'crystal': 1000},
                                'attack': 50, 'shield': 10,
                                'speed': 12500, 'cargo_capacity': 50,
                                'fuel_usage': 20, 'engine': 'combustion'},
              'heavy_fighter': {'cost': {'metal': 6000, 'crystal': 4000},
                                'attack': 50, 'shield': 10,
                                'speed': 12500, 'cargo_capacity': 50, 'fuel_usage': 20, 'engine': 'combustion'},
              'cruiser': {'cost': {'metal': 20000, 'crystal': 7000},
                          'attack': 50, 'shield': 10,
                          'speed': 12500, 'cargo_capacity': 50, 'fuel_usage': 20, 'engine': 'combustion'},
              'battleship': {'cost': {'metal': 45000, 'crystal': 15000},
                             'attack': 50, 'shield': 10,
                             'speed': 12500, 'cargo_capacity': 50, 'fuel_usage': 20, 'engine': 'combustion'},
              'battle_cruiser': {'cost': {'metal': 40000, 'crystal': 30000},
                                 'attack': 50, 'shield': 10,
                                 'speed': 12500, 'cargo_capacity': 50, 'fuel_usage': 20, 'engine': 'combustion'},
              'bomber': {'cost': {'metal': 50000, 'crystal': 25000},
                         'attack': 50, 'shield': 10,
                         'speed': 12500, 'cargo_capacity': 50, 'fuel_usage': 20, 'engine': 'combustion'},
              'destroyer': {'cost': {'metal': 60000, 'crystal': 50000},
                            'attack': 50, 'shield': 10,
                            'speed': 12500, 'cargo_capacity': 50, 'fuel_usage': 20, 'engine': 'combustion'},
              'death_star': {'cost': {'metal': 5*10**6, 'crystal': 4*10**6},
                             'attack': 50, 'shield': 10,
                             'speed': 12500, 'cargo_capacity': 50, 'fuel_usage': 20, 'engine': 'combustion'},
              'small_cargo': {'cost': {'metal': 2000, 'crystal': 2000},
                              'attack': 50, 'shield': 10,
                              'speed': 12500, 'cargo_capacity': 50, 'fuel_usage': 20, 'engine': 'combustion'},
              'large_cargo': {'cost': {'metal': 6000, 'crystal': 6000},
                              'attack': 50, 'shield': 10,
                              'speed': 12500, 'cargo_capacity': 50, 'fuel_usage': 20, 'engine': 'combustion'},
              'colony_ship': {'cost': {'metal': 10000, 'crystal': 20000},
                              'attack': 50, 'shield': 10,
                              'speed': 12500, 'cargo_capacity': 50, 'fuel_usage': 20, 'engine': 'combustion'},
              'recycler': {'cost': {'metal': 10000, 'crystal': 6000},
                           'attack': 50, 'shield': 10,
                           'speed': 12500, 'cargo_capacity': 50, 'fuel_usage': 20, 'engine': 'combustion'},
              'espionage_probe': {'cost': {'metal': 0, 'crystal': 1000},
                                  'attack': 50, 'shield': 10,
                                  'speed': 12500, 'cargo_capacity': 50, 'fuel_usage': 20, 'engine': 'combustion'},
              'solar_satellite': {'cost': {'metal': 3000, 'crystal': 2000},
                                  'attack': 50, 'shield': 10,
                                  'speed': 0, 'cargo_capacity': 0, 'fuel_usage': 0, 'engine': None}}

ENGINE = {'combustion': 100}
DEFENSES = {'rocket_launcher',
            'light_laser',
            'heavy_laser',
            'gauss_cannon',
            'ion_cannon',
            'plasma_turret',
            'small_shield_dome',
            'large_shield_dome',
            'anti_ballistic_missiles',
            'interplanetary_missiles'}
# times
TIME2UPDATE_DB = 10
TIME2REFRESH = 3
