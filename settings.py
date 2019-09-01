RESOURCES = {
    "metal": {
        "init": 5000,
        "per_s0": 1,
        "cap0": 10000
    },
    "crystal": {
        "init": 5000,
        "per_s0": 1,
        "cap0": 10000
    },
    "deuterium": {
        "init": 5000,
        "per_s0": 1,
        "cap0": 10000
    }
}

BUILDINGS = {
    "metal_mine": {
        "name": "Metal Mine",
        "costs0": {
            "metal": 20,
            "crystal": 15,
            "deuterium": 5
        },
        "costs_rate": 1.5,
        "time0": 3,
        "time_rate": 1.5,
        "metal_rate": 2
    },
    "crystal_mine": {
        "name": "Crystal Mine",
        "costs0": {
            "metal": 20,
            "crystal": 15,
            "deuterium": 5
        },
        "costs_rate": 1.5,
        "time0": 2,
        "time_rate": 1.5,
        "crystal_rate": 2
    },
    "deuterium_mine": {
        "name": "Deuterium Mine",
        "costs0": {
            "metal": 20,
            "crystal": 15,
            "deuterium": 5
        },
        "costs_rate": 1.5,
        "time0": 2,
        "time_rate": 1.5,
        "deuterium_rate": 2
    },
    "metal_storage": {
        "name": "Metal Storage",
        "costs0": {
            "metal": 50,
            "crystal": 0,
            "deuterium": 0
        },
        "costs_rate": 2,
        "time0": 3,
        "time_rate": 2,
        "metal_rate": 2
    },
    "crystal_storage": {
        "name": "Crystal Storage",
        "costs0": {
            "metal": 50,
            "crystal": 25,
            "deuterium": 0
        },
        "costs_rate": 2,
        "time0": 3,
        "time_rate": 2,
        "crystal_rate": 2
    },
    "deuterium_storage": {
        "name": "Deuterium Storage",
        "costs0": {
            "metal": 50,
            "crystal": 50,
            "deuterium": 0
        },
        "costs_rate": 2,
        "time0": 3,
        "time_rate": 2,
        "deuterium_rate": 2
    },
    "robotics_factory":{
        "name": "Robotics Factory",
        "costs0": {
            "metal": 50,
            "crystal": 50,
            "deuterium": 0
        },
        "costs_rate": 2,
        "time0": 3,
        "time_rate": 2,
        "building_time_factor0": 0.5
    },
    "shipyard":{
        "name": "Shipyard",
        "costs0": {
            "metal": 50,
            "crystal": 50,
            "deuterium": 0
        },
        "costs_rate": 2,
        "time0": 3,
        "time_rate": 2,
        "building_time_factor0": 0.5
    },
    "nanite_factory":{
        "name": "Nanite Factory",
        "costs0": {
            "metal": 50,
            "crystal": 50,
            "deuterium": 0
        },
        "costs_rate": 2,
        "time0": 3,
        "time_rate": 2,
        "building_time_factor0": 0.5
    },
    "research_lab":{
        "name": "Research Lab",
        "costs0": {
            "metal": 50,
            "crystal": 50,
            "deuterium": 0
        },
        "costs_rate": 2,
        "time0": 3,
        "time_rate": 2,
        "reasearch_time_factor0": 0.5
    },
    "terraformer":{
        "name": "Terraformer",
        "costs0": {
            "metal": 50,
            "crystal": 50,
            "deuterium": 0
        },
        "costs_rate": 2,
        "time0": 3,
        "time_rate": 2,
        "fields_added_per_level": 5
    },
}

DEFENSES = {
    "rocketlauncher": {
        "name": "Rocketlauncher",
        "costs": {
            "metal": 2000,
            "crystal": 0,
            "deuterium": 0
        },
        "time": 10,
        "hull": 200,
        "shield": 20,
        "weapon": 80
    },
    "light_laser": {
        "name": "Light Laser",
        "costs": {
            "metal": 1500,
            "crystal": 500,
            "deuterium": 0
        },
        "time": 10,
        "hull": 200,
        "shield": 25,
        "weapon": 100
    },
    "heavy_laser": {
        "name": "Heavy Laser",
        "costs": {
            "metal": 6000,
            "crystal": 2000,
            "deuterium": 0
        },
        "time": 10,
        "hull": 800,
        "shield": 100,
        "weapon": 250
    },
    "ion_cannon": {
        "name": "Ion Cannon",
        "costs": {
            "metal": 2000,
            "crystal": 6000,
            "deuterium": 0
        },
        "time": 10,
        "hull": 800,
        "shield": 500,
        "weapon": 150
    },
    "gauss_cannon": {
        "name": "Gauss Cannon",
        "costs": {
            "metal": 20000,
            "crystal": 15000,
            "deuterium": 2000
        },
        "time": 10,
        "hull": 3500,
        "shield": 200,
        "weapon": 1100
    },
    "plasma_turret": {
        "name": "Plasma Turret",
        "costs": {
            "metal": 50000,
            "crystal": 50000,
            "deuterium": 30000
        },
        "time": 10,
        "hull": 10000,
        "shield": 300,
        "weapon": 3000
    },
    "small_shield_dome": {
        "name": "Small Shield Dome",
        "costs": {
            "metal": 10000,
            "crystal": 10000,
            "deuterium": 0
        },
        "time": 10,
        "hull": 2000,
        "shield": 2000,
        "weapon": 1
    },
    "large_shield_dome": {
        "name": "Large Shield Dome",
        "costs": {
            "metal": 50000,
            "crystal": 50000,
            "deuterium": 0
        },
        "time": 10,
        "hull": 10000,
        "shield": 10000,
        "weapon": 80
    },
}