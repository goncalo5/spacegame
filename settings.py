RESOURCES = {
    "metal": {
        "init": 100,
        "per_s0": 1,
        "cap0": 120
    },
    "crystal": {
        "init": 100,
        "per_s0": 1,
        "cap0": 120
    },
    "deuterium": {
        "init": 100,
        "per_s0": 1,
        "cap0": 120
    }
}

BUILDINGS = {
    "metal_mine": {
        "name": "Metal Mine",
        "cost0": {
            "metal": 20,
            "crystal": 15,
            "deuterium": 5
        },
        "cost_rate": 1.5,
        "time0": 2,
        "time_rate": 1.5,
        "metal_rate": 2
    },
    "crystal_mine": {
        "name": "Crystal Mine",
        "cost0": {
            "metal": 20,
            "crystal": 15,
            "deuterium": 5
        },
        "cost_rate": 1.5,
        "time0": 2,
        "time_rate": 1.5,
        "crystal_rate": 2
    },
    "deuterium_mine": {
        "name": "Deuterium Mine",
        "cost0": {
            "metal": 20,
            "crystal": 15,
            "deuterium": 5
        },
        "cost_rate": 1.5,
        "time0": 2,
        "time_rate": 1.5,
        "deuterium_rate": 2
    },
    "metal_storage": {
        "name": "Metal Storage",
        "cost0": {
            "metal": 50,
            "crystal": 0,
            "deuterium": 0
        },
        "cost_rate": 2,
        "time0": 3,
        "time_rate": 2,
        "metal_rate": 2
    },
    "crystal_storage": {
        "name": "Crystal Storage",
        "cost0": {
            "metal": 50,
            "crystal": 25,
            "deuterium": 0
        },
        "cost_rate": 2,
        "time0": 3,
        "time_rate": 2,
        "crystal_rate": 2
    },
    "deuterium_storage": {
        "name": "Deuterium Storage",
        "cost0": {
            "metal": 50,
            "crystal": 50,
            "deuterium": 0
        },
        "cost_rate": 2,
        "time0": 3,
        "time_rate": 2,
        "deuterium_rate": 2
    },
}