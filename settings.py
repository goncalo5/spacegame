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
}