# resources
METAL = {'index': 0, 'name': 'metal', 'total': 1000}
CRYSTAL = {'index': 1, 'name': 'crystal', 'total': 500}
DEUTERIUM = {'index': 2, 'name': 'deuterium', 'total': 0}
ENERGY = {'index': 3, 'name': 'energy', 'total': 0}
RESOURCES = [METAL, CRYSTAL, DEUTERIUM, ENERGY]

# buildings
# resources buildings:
METAL_MINE = {
    'name': 'metal_mine', 'kind': 'resource_building', 'time': 3, 'rate_time': 1.5,
    'cost': [10, 0, 0, 0], 'rate_cost': [1.5, 0, 0, 0],
    'earned_resources': {'total0': [0, 0, 0, 0], 'total1': [0, 0, 0, -5], 'rate_total': [0, 0, 0, 1.5],
                      'per_s0': [2, 0, 0, 0], 'per_s1': [10, 0, 0, 0], 'rate_per_s': [2, 0, 0, 0]}
}
CRYSTAL_MINE = {
    'name': 'crystal_mine', 'kind': 'resource_building', 'time': 3, 'rate_time': 1.5,
    'cost': [10, 0, 0, 0], 'rate_cost': [1.5, 0, 0, 0],
    'earned_resources': {'total0': [0, 0, 0, 0], 'total1': [0, 0, 0, -5], 'rate_total': [0, 0, 0, 1.5],
                      'per_s0': [0, 1, 0, 0], 'per_s1': [0, 5, 0, 0], 'rate_per_s': [0, 2, 0, 0]}
}
DEUTERIUM_SYNTHESIZER = {
    'name': 'deuterium_synthesizer', 'kind': 'resource_building', 'time': 3, 'rate_time': 1.5,
    'cost': [10, 0, 0, 0], 'rate_cost': [1.5, 0, 0, 0],
    'earned_resources': {'total0': [0, 0, 0, 0], 'total1': [0, 0, 0, -5], 'rate_total': [0, 0, 0, 1.5],
                      'per_s0': [0, 0, 0, 0], 'per_s1': [0, 0, 1.5, 0], 'rate_per_s': [0, 0, 2, 0]}
}
SOLAR_PLANT = {
    'name': 'Solar Plant', 'kind': 'resource_building', 'time': 3, 'rate_time': 1.5,
    'cost': [10, 0, 0, 0], 'rate_cost': [1.5, 0, 0, 0],
    'earned_resources': {'total0': [0, 0, 0, 0], 'total1': [0, 0, 0, 50], 'rate_total': [0, 0, 0, 1.5],
                      'per_s0': [0, 0, 0, 0], 'per_s1': [0, 0, 0, 0], 'rate_per_s': [0, 0, 0, 0]}
}
FUSION_REACTOR = {
    'name': 'Fusion Reactor', 'kind': 'resource_building', 'time': 3, 'rate_time': 1.5,
    'cost': [10, 0, 0, 0], 'rate_cost': [1.5, 0, 0, 0],
    'earned_resources': {'total0': [0, 0, 0, 0], 'total1': [0, 0, 0, 150], 'rate_total': [0, 0, 0, 1.5],
                      'per_s0': [0, 0, 0, 0], 'per_s1': [0, 0, -1.5, 0], 'rate_per_s': [0, 0, 2, 0]}
}
# Storage
METAL_STORAGE = {
    'name': 'metal_storage', 'kind': 'storage', 'time': 3, 'rate_time': 1.5,
    'cost': [10, 0, 0, 0], 'rate_cost': [1.5, 0, 0, 0],
    'resource_storage': {'total': [0, 0, 0, 50], 'rate_total': [0, 0, 0, 1.5]}
}
CRYSTAL_STORAGE = {
    'name': 'crystal_storage', 'kind': 'storage', 'time': 3, 'rate_time': 1.5,
    'cost': [10, 0, 0, 0], 'rate_cost': [1.5, 0, 0, 0],
    'resource_storage': {'total': [0, 0, 0, 50], 'rate_total': [0, 0, 0, 1.5]}
}
DEUTERIUM_TANK = {
    'name': 'deuterium_tank', 'kind': 'storage', 'time': 3, 'rate_time': 1.5,
    'cost': [10, 0, 0, 0], 'rate_cost': [1.5, 0, 0, 0],
    'resource_storage': {'total': [0, 0, 0, 50], 'rate_total': [0, 0, 0, 1.5]}
}
# Factories (Reduces construction time)
ROBOTICS_FACTORY = {
    'name': 'robot_factory',  'kind': 'factory', 'time': 3, 'rate_time': 1.5,
    'cost': [10, 0, 0, 0], 'rate_cost': [1.5, 0, 0, 0],
    'factor': 2, 'rate_factor': 2
}
NANITE_FACTORY = {
    'name': 'Nanite Factory', 'kind': 'factory', 'time': 3, 'rate_time': 1.5,
    'cost': [10, 0, 0, 0], 'rate_cost': [1.5, 0, 0, 0],
    'factor': 2, 'rate_factor': 2
}
SHIPYARD = {
    'name': 'Shipyard', 'kind': 'factory', 'time': 3, 'rate_time': 1.5,
    'cost': [10, 0, 0, 0], 'rate_cost': [1.5, 0, 0, 0],
    'factor': 2, 'rate_factor': 2
}
# Others Buildings
ALLIANCE_DEPOT = {
    'name': 'Alliance Depot', 'kind': 'other', 'time': 3, 'rate_time': 1.5,
    'cost': [10, 0, 0, 0], 'rate_cost': [1.5, 0, 0, 0]
}
MISSILE_SILO = {
    'name': 'Missile Silo', 'kind': 'other', 'time': 3, 'rate_time': 1.5,
    'cost': [10, 0, 0, 0], 'rate_cost': [1.5, 0, 0, 0]
}
RESEARCH_LAB = {
    'name': 'Research Lab', 'kind': 'other', 'time': 3, 'rate_time': 1.5,
    'cost': [10, 0, 0, 0], 'rate_cost': [1.5, 0, 0, 0]
}
TERRAFORMER = {
    'name': 'Terraformer', 'kind': 'other', 'time': 3, 'rate_time': 1.5,
    'cost': [10, 0, 0, 0], 'rate_cost': [1.5, 0, 0, 0]
}
SPACE_DOCK = {
    'name': 'Space Dock', 'kind': 'other', 'time': 3, 'rate_time': 1.5,
    'cost': [10, 0, 0, 0], 'rate_cost': [1.5, 0, 0, 0]
}
RESOURCE_BUILDING = [METAL_MINE, CRYSTAL_MINE, DEUTERIUM_SYNTHESIZER, SOLAR_PLANT, FUSION_REACTOR]
STORAGES = [METAL_STORAGE, CRYSTAL_STORAGE, DEUTERIUM_TANK]
FACTORIES = [ROBOTICS_FACTORY, NANITE_FACTORY, SHIPYARD]
OTHERS = [ALLIANCE_DEPOT, MISSILE_SILO, RESEARCH_LAB, TERRAFORMER, SPACE_DOCK]
BUILDINGS = RESOURCE_BUILDING + STORAGES + FACTORIES + OTHERS

UNIVERSE = {'n_galaxies': 9, 'planet': {'fields': 100, 'rate_field': 1.5}}
DISTANCES = {'GALAXIES': 100, 'PLANETARY_SYSTEMS': 10, 'PLANETS': 1}

# Trader
TRADER = {'ratios': {'metal': 1, 'crystal': 2, 'deuterium': 3},
          'profit': 0.1}

# Spaceships
GRAVITATION = {'name': 'Gravitation', 'power': 0}
COMBUSTION = {'name': 'Combustion', 'power': 1}
IMPULSION = {'name': 'Impulsion', 'power': 1}
HYPERSPACE = {'name': 'Hyperspace', 'power': 1}
ENGINES = [COMBUSTION, IMPULSION, HYPERSPACE]

LIGHT_FIGHTER = {
    'name': 'light_fighter', 'time': 3, 'rate_time': 1.5, 'cost': [3000, 1000, 0, 0],
    'attack': 50, 'shield': 10, 'speed': 12500, 'cargo_capacity': 50,
    'fuel_usage': 20, 'engine': COMBUSTION}
HEAVY_FIGHTER = {
    'name': 'Heavy Fighter', 'time': 3, 'rate_time': 1.5, 'cost': [6000, 4000, 0, 0],
    'attack': 50, 'shield': 10, 'speed': 12500, 'cargo_capacity': 50, 'fuel_usage': 20, 'engine': COMBUSTION}
CRUISER = {
    'name': 'Cruiser', 'time': 3, 'rate_time': 1.5, 'cost': [20000, 7000, 0, 0],
    'attack': 50, 'shield': 10, 'speed': 12500, 'cargo_capacity': 50, 'fuel_usage': 20, 'engine': COMBUSTION}
BATTLESHIP = {
    'name': 'Battleship', 'time': 3, 'rate_time': 1.5, 'cost': [45000, 15000, 0, 0],
    'attack': 50, 'shield': 10, 'speed': 12500, 'cargo_capacity': 50, 'fuel_usage': 20, 'engine': COMBUSTION}
BATTLE_CRUISER = {
    'name': 'Battle Cruiser', 'time': 3, 'rate_time': 1.5, 'cost': [40000, 30000, 0, 0],
    'attack': 50, 'shield': 10,
    'speed': 12500, 'cargo_capacity': 50, 'fuel_usage': 20, 'engine': COMBUSTION}
BOMBER = {
    'name': 'Bomber', 'time': 3, 'rate_time': 1.5, 'cost': [50000, 25000, 0, 0],
    'attack': 50, 'shield': 10,
    'speed': 12500, 'cargo_capacity': 50, 'fuel_usage': 20, 'engine': COMBUSTION}
DESTROYER = {
    'name': 'destroyer', 'time': 3, 'rate_time': 1.5, 'cost': [60000, 50000, 0, 0],
    'attack': 50, 'shield': 10,
    'speed': 12500, 'cargo_capacity': 50, 'fuel_usage': 20, 'engine': COMBUSTION}
DEATH_STAR = {
    'name': 'Death Star', 'time': 3, 'rate_time': 1.5, 'cost': [5*10**6, 4*10**6, 0, 0],
    'attack': 50, 'shield': 10,
    'speed': 12500, 'cargo_capacity': 50, 'fuel_usage': 20, 'engine': COMBUSTION}
SMALL_CARGO = {
    'name': 'small Cargo', 'time': 3, 'rate_time': 1.5, 'cost': [2000, 2000, 0, 0],
    'attack': 50, 'shield': 10,
    'speed': 12500, 'cargo_capacity': 50, 'fuel_usage': 20, 'engine': COMBUSTION}
LARGE_CARGO = {
    'name': 'Large Cargo', 'time': 3, 'rate_time': 1.5, 'cost': [6000, 6000, 0, 0],
    'attack': 50, 'shield': 10,
    'speed': 12500, 'cargo_capacity': 50, 'fuel_usage': 20, 'engine': COMBUSTION}
COLONY_SHIP = {
    'name': 'Colony Ship', 'time': 3, 'rate_time': 1.5, 'cost': [10000, 20000, 0, 0],
    'attack': 50, 'shield': 10,
    'speed': 12500, 'cargo_capacity': 50, 'fuel_usage': 20, 'engine': COMBUSTION}
RECYCLER = {
    'name': 'Recycler', 'time': 3, 'rate_time': 1.5, 'cost': [10000, 6000, 0, 0],
    'attack': 50, 'shield': 10,
    'speed': 12500, 'cargo_capacity': 50, 'fuel_usage': 20, 'engine': COMBUSTION}
ESPIONAGE_PROBE = {
    'name': 'Espionage Probe', 'time': 3, 'rate_time': 1.5, 'cost': [0, 1000, 0, 0],
    'attack': 50, 'shield': 10,
    'speed': 12500, 'cargo_capacity': 50, 'fuel_usage': 20, 'engine': COMBUSTION}
SOLAR_SATELLITE = {
    'name': 'Solar Satellite', 'time': 3, 'rate_time': 1.5, 'cost': [3000, 2000, 0, 0],
    'attack': 50, 'shield': 10,
    'speed': 0, 'cargo_capacity': 0, 'fuel_usage': 0, 'engine': GRAVITATION}

SPACESHIPS = [LIGHT_FIGHTER, HEAVY_FIGHTER, CRUISER, BATTLESHIP, BATTLE_CRUISER, BOMBER, DESTROYER, DEATH_STAR,
              SMALL_CARGO, LARGE_CARGO, COLONY_SHIP, RECYCLER, ESPIONAGE_PROBE, SOLAR_SATELLITE]

ROCKET_LAUNCHER = {
    'name': 'rocket_launcher', 'time': 3, 'rate_time': 1.5, 'cost': [3000, 2000, 0, 0],
    'attack': 50, 'shield': 10}
LIGHT_LASER = {
    'name': 'light_laser', 'time': 3, 'rate_time': 1.5, 'cost': [3000, 2000, 0, 0],
    'attack': 50, 'shield': 10}
HEAVY_LASER = {
    'name': 'heavy_laser', 'time': 3, 'rate_time': 1.5, 'cost': [3000, 2000, 0, 0],
    'attack': 50, 'shield': 10}
GAUSS_CANNON = {
    'name': 'gauss_cannon', 'time': 3, 'rate_time': 1.5, 'cost': [3000, 2000, 0, 0],
    'attack': 50, 'shield': 10}
ION_CANNON = {
    'name': 'ion_cannon', 'time': 3, 'rate_time': 1.5, 'cost': [3000, 2000, 0, 0],
    'attack': 50, 'shield': 10}
PLASMA_TURRET = {
    'name': 'plasma_turret', 'time': 3, 'rate_time': 1.5, 'cost': [3000, 2000, 0, 0],
    'attack': 50, 'shield': 10}
SMALL_SHIELD_DOME = {
    'name': 'small_shield_dome', 'time': 3, 'rate_time': 1.5, 'cost': [3000, 2000, 0, 0],
    'attack': 50, 'shield': 10}
LARGE_SHIELD_DOME = {
    'name': 'large_shield_dome', 'time': 3, 'rate_time': 1.5, 'cost': [3000, 2000, 0, 0],
    'attack': 50, 'shield': 10}
ANTI_BALLISTIC_MISSILES = {
    'name': 'anti_ballistic_missiles', 'time': 3, 'rate_time': 1.5, 'cost': [3000, 2000, 0, 0],
    'attack': 50, 'shield': 10}
INTERPLANETARY_MISSILES = {
    'name': 'interplanetary_missiles', 'time': 3, 'rate_time': 1.5, 'cost': [3000, 2000, 0, 0],
    'attack': 50, 'shield': 10}
DEFENSES = [ROCKET_LAUNCHER, LIGHT_LASER, HEAVY_LASER, GAUSS_CANNON, ION_CANNON, PLASMA_TURRET,
            SMALL_SHIELD_DOME, LARGE_SHIELD_DOME, ANTI_BALLISTIC_MISSILES, INTERPLANETARY_MISSILES]

MACHINES = SPACESHIPS + DEFENSES

N_ROUNDS = 1

# Presentation
SCREEN = '800x650'
MENU = ['overview', 'resources', 'buildings', 'market', 'research',
        'hangar', 'defense', 'fleet', 'universe', 'alliance']
