# resources
METAL = {'NAME': 'metal', 'total': 1000, 'per_s': 5, 'rate_per_s': 2}
CRYSTAL = {'NAME': 'crystal', 'total': 500, 'per_s': 1, 'rate_per_s': 1.5}
DEUTERIUM = {'NAME': 'deuterium', 'total': 500, 'per_s': 1, 'rate_per_s': 1.5}
ENERGY = {'NAME': 'energy', 'total': 500, 'per_s': 0, 'rate_per_s': 1.5}
RESOURCES = [METAL, CRYSTAL, DEUTERIUM, ENERGY]

# buildings
# resources buildings:
METAL_MINE = {'NAME': 'metal_mine', 'KIND': 'mine', 'COST': [10, 0, 0], 'RATE_COST': [1.5, 0, 0],
              'TIME': 3, 'RATE_TIME': 1.5, 'RESOURCE_GAIN': METAL['name'], 'RESOURCE_CONSUME': DEUTERIUM['name']}

CRYSTAL_MINE = {'NAME': 'crystal_mine', 'KIND': 'mine', 'COST': [10, 0, 0], 'RATE_COST': [1.5, 0, 0],
              'TIME': 3, 'RATE_TIME': 1.5, 'RESOURCE_GAIN': CRYSTAL['name'], 'RESOURCE_CONSUME': DEUTERIUM['name']}

DEUTERIUM_SYNTHESIZER = {'NAME': 'deuterium_synthesizer', 'KIND': 'mine', 'COST': [10, 0, 0], 'RATE_COST': [1.5, 0, 0],
              'TIME': 3, 'RATE_TIME': 1.5, 'RESOURCE_GAIN': DEUTERIUM['name'], 'RESOURCE_CONSUME': DEUTERIUM['name']}

SOLAR_PLANT = {'NAME': 'metal_mine', 'KIND': 'mine', 'COST': [10, 0, 0], 'RATE_COST': [1.5, 0, 0],
              'TIME': 3, 'RATE_TIME': 1.5, 'RESOURCE_GAIN': ENERGY['name']}

FUSION_REACTOR, = {'NAME': 'metal_mine', 'KIND': 'mine', 'COST': [10, 0, 0], 'RATE_COST': [1.5, 0, 0],
              'TIME': 3, 'RATE_TIME': 1.5, 'RESOURCE_GAIN': ENERGY['name'], 'RESOURCE_CONSUME': DEUTERIUM['name']}

METAL_STORAGE = {'NAME': 'metal_storage', 'KIND': 'storage', 'COST': [10, 0, 0], 'RATE_COST': [1.5, 0, 0],
              'TIME': 3, 'RATE_TIME': 1.5, RESOURCE: METAL['name'], 'CAPACITY': 1500, 'RATE_CAPACITY': 1.5}

CRYSTAL_STORAGE = {'NAME': 'crystal_storage', 'KIND': 'storage', 'COST': [10, 0, 0], 'RATE_COST': [1.5, 0, 0],
              'TIME': 3, 'RATE_TIME': 1.5, RESOURCE: METAL['name'], 'CAPACITY': 1500, 'RATE_CAPACITY': 1.5}

DEUTERIUM_TANK = {'NAME': 'deuterium_tank', 'KIND': 'storage', 'COST': [10, 0, 0], 'RATE_COST': [1.5, 0, 0],
              'TIME': 3, 'RATE_TIME': 1.5, RESOURCE: METAL['name'], 'CAPACITY': 1500, 'RATE_CAPACITY': 1.5}

ROBOTICS_FACTORY robot_factory': {'cost': 10, 'rate_cost': 2, 'time': 3, 'rate_time': 1.5,
                               'KIND': 'factory', 'factor': 2, 'rate_factor': 2}}

NANITE_FACTORY

SHIPYARD

ALLIANCE_DEPOT

MISSILE_SILO,

RESEARCH_LAB

TERRAFORMER

SPACE_DOCK

BUILDINGS = [METAL_MINE, CRYSTAL_MINE, DEUTERIUM_SYNTHESIZER, SOLAR_PLANT, FUSION_REACTOR,
             METAL_STORAGE, CRYSTAL_STORAGE, DEUTERIUM_TANK,
             ROBOTICS_FACTORY, NANITE_FACTORY, SHIPYARD, ALLIANCE_DEPOT, MISSILE_SILO,
             RESEARCH_LAB, TERRAFORMER, SPACE_DOCK]

UNIVERSE = {'planet': {'fields': 100, 'rate_field': 1.5}}

SPACESHIPS = {'light_fighter': {'name': 'light_fighter',
                                'cost': {'metal': 3000, 'crystal': 1000},
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

DEFENSES = {'rocket_launcher':
                {'cost': {'metal': 3000, 'crystal': 2000},
                 'attack': 50, 'shield': 10},
            'light_laser':
                {'cost': {'metal': 3000, 'crystal': 2000},
                 'attack': 50, 'shield': 10},
            'heavy_laser':
                {'cost': {'metal': 3000, 'crystal': 2000},
                 'attack': 50, 'shield': 10},
            'gauss_cannon':
                {'cost': {'metal': 3000, 'crystal': 2000},
                 'attack': 50, 'shield': 10},
            'ion_cannon':
                {'cost': {'metal': 3000, 'crystal': 2000},
                 'attack': 50, 'shield': 10},
            'plasma_turret':
                {'cost': {'metal': 3000, 'crystal': 2000},
                 'attack': 50, 'shield': 10},
            'small_shield_dome':
                {'cost': {'metal': 3000, 'crystal': 2000},
                 'attack': 50, 'shield': 10},
            'large_shield_dome':
                {'cost': {'metal': 3000, 'crystal': 2000},
                 'attack': 50, 'shield': 10},
            'anti_ballistic_missiles':
                {'cost': {'metal': 3000, 'crystal': 2000},
                 'attack': 50, 'shield': 10},
            'interplanetary_missiles':
                {'cost': {'metal': 3000, 'crystal': 2000},
                 'attack': 50, 'shield': 10}}

MACHINES = dict(SPACESHIPS, **DEFENSES)

N_ROUNDS = 1
DISTANCES = {'GALAXIES': 100, 'PLANETARYSYSTEMS': 10, 'PLANETS': 1}

# Presentation
MENU = ['overview', 'buildings', 'merchant', 'research',
        'hangar', 'defense', 'fleet', 'universe', 'alliance']
