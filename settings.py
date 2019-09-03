RESOURCES = {
    "metal": {
        "init": 8000,
        "per_s0": 1,
        "cap0": 10000
    },
    "crystal": {
        "init": 8000,
        "per_s0": 1,
        "cap0": 10000
    },
    "deuterium": {
        "init": 8000,
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
    "solar_plant": {
        "name": "Solar Plant",
        "costs0": {
            "metal": 20,
            "crystal": 15,
            "deuterium": 5
        },
        "costs_rate": 1.5,
        "time0": 2,
        "time_rate": 1.5,
        "energy_rate": 2
    },
    "fusion_reactor": {
        "name": "Fusion Reactor",
        "costs0": {
            "metal": 900,
            "crystal": 360,
            "deuterium": 180
        },
        "costs_rate": 1.5,
        "time0": 2,
        "time_rate": 1.5,
        "requirements": [
            ["deuterium_mine", 5],
            ["energy_technology", 3]
        ],
        "energy_rate": 2
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
        "requirements": [
            ["robotics_factory", 2]
        ],
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
    "missile_silo":{
        "name": "Missile Silo",
        "costs0": {
            "metal": 20000,
            "crystal": 20000,
            "deuterium": 1000
        },
        "costs_rate": 2,
        "time0": 3,
        "time_rate": 2,
        "reasearch_time_factor0": 0.5
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
        "requirements": [
            ["robotics_factory", 10],
            ["computer_technology", 10]
        ],
        "building_time_factor0": 0.5
    },
    "terraformer":{
        "name": "Terraformer",
        "costs0": {
            "metal": 50,
            "crystal": 50,
            "deuterium": 0,
            "energy": 1000
        },
        "costs_rate": 2,
        "time0": 3,
        "time_rate": 2,
        "requirements": [
            ["nanite_factory", 1],
            ["energy_technology", 12]
        ],
        "fields_added_per_level": 5
    },
    "space_dock":{
        "name": "Space Dock",
        "costs0": {
            "metal": 200,
            "crystal": 0,
            "deuterium": 50,
            "energy": 50
        },
        "costs_rate": 2,
        "time0": 3,
        "time_rate": 2,
        "requirements": [
            ["nanite_factory", 1],
            ["energy_technology", 12]
        ],
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
        "time": 2,
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

RESEARCHES = {
    "energy_technology": {
        "name": "Energy Technology",
        "requirements": [
            ["research_lab", 1]
        ],
        "costs0": {
            "metal": 0,
            "crystal": 800,
            "deuterium": 400
        },
        "costs_rate": 2,
        "time0": 2,
        "time_rate": 2
    },
    "laser_technology": {
        "name": "Laser Technology",
        "requirements": [
            ["research_lab", 1],
            ["energy_technology", 2],
        ],
        "costs0": {
            "metal": 200,
            "crystal": 100,
            "deuterium": 0
        },
        "costs_rate": 2,
        "time0": 10,
        "time_rate": 2
    },
    "ion_technology": {
        "name": "Ion Technology",
        "requirements": [
            ["research_lab", 4],
            ["energy_technology", 2],
            ["laser_technology", 5],
        ],
        "costs0": {
            "metal": 1000,
            "crystal": 300,
            "deuterium": 100
        },
        "costs_rate": 2,
        "time0": 10,
        "time_rate": 2
    },
    "hyperspace_technology": {
        "name": "Hyperspace Technology",
        "requirements": [
            ["research_lab", 7],
            ["laser_technology", 5],
            ["shielding_technology", 5],
        ],
        "costs0": {
            "metal": 0,
            "crystal": 4000,
            "deuterium": 2000
        },
        "costs_rate": 2,
        "time0": 10,
        "time_rate": 2
    },
    "plasma_technology": {
        "name": "Plasma Technology",
        "requirements": [
            ["research_lab", 4],
            ["energy_technology", 8],
            ["laser_technology", 10],
            ["ion_technology", 5],
        ],
        "costs0": {
            "metal": 2000,
            "crystal": 4000,
            "deuterium": 1000
        },
        "costs_rate": 2,
        "time0": 10,
        "time_rate": 2
    },
    "combustion_drive": {
        "name": "Combustion Drive",
        "requirements": [
            ["research_lab", 1],
            ["energy_technology", 1],
        ],
        "costs0": {
            "metal": 400,
            "crystal": 0,
            "deuterium": 600
        },
        "costs_rate": 2,
        "time0": 10,
        "time_rate": 2
    },
    "impulse_drive": {
        "name": "Impulse Drive",
        "requirements": [
            ["research_lab", 2],
            ["energy_technology", 1],
        ],
        "costs0": {
            "metal": 2000,
            "crystal": 4000,
            "deuterium": 600
        },
        "costs_rate": 2,
        "time0": 10,
        "time_rate": 2
    },
    "hyperspace_drive": {
        "name": "Hyperspace Drive",
        "requirements": [
            ["research_lab", 7],
            ["energy_technology", 5],
            ["hyperspace_technology", 3],
            ["shielding_technology", 6],
        ],
        "costs0": {
            "metal": 10000,
            "crystal": 20000,
            "deuterium": 6000
        },
        "costs_rate": 2,
        "time0": 10,
        "time_rate": 2
    },
    "espionage_technology": {
        "name": "Espionage Technology",
        "requirements": [
            ["research_lab", 4],
            ["energy_technology", 8],
            ["laser_technology", 10],
            ["ion_technology", 5],
        ],
        "costs0": {
            "metal": 200,
            "crystal": 1000,
            "deuterium": 200
        },
        "costs_rate": 2,
        "time0": 10,
        "time_rate": 2
    },
    "computer_technology": {
        "name": "Computer Technology",
        "requirements": [
            ["research_lab", 1],
        ],
        "costs0": {
            "metal": 0,
            "crystal": 400,
            "deuterium": 600
        },
        "costs_rate": 2,
        "time0": 10,
        "time_rate": 2
    },
    "astrophysics": {
        "name": "Astrophysics",
        "requirements": [
            ["research_lab", 3],
            ["energy_technology", 1],
            ["impulse_drive", 3],
            ["espionage_technology", 4],
        ],
        "costs0": {
            "metal": 4000,
            "crystal": 8000,
            "deuterium": 4000
        },
        "costs_rate": 2,
        "time0": 10,
        "time_rate": 2
    },
    "intergalactic_research_network": {
        "name": "Intergalactic Research Network",
        "requirements": [
            ["research_lab", 10],
            ["energy_technology", 5],
            ["hyperspace_technology", 8],
            ["computer_technology", 8],
            ["shielding_technology", 5],
        ],
        "costs0": {
            "metal": 240000,
            "crystal": 400000,
            "deuterium": 160000
        },
        "costs_rate": 2,
        "time0": 10,
        "time_rate": 2
    },
    "graviton_technology": {
        "name": "Graviton Technology",
        "requirements": [
            ["research_lab", 12],
        ],
        "costs0": {
            "metal": 0,
            "crystal": 0,
            "deuterium": 0
        },
        "costs_rate": 2,
        "time0": 10,
        "time_rate": 2
    },
    "armour_technology": {
        "name": "Armour Technology",
        "requirements": [
            ["research_lab", 2],
        ],
        "costs0": {
            "metal": 1000,
            "crystal": 0,
            "deuterium": 0
        },
        "costs_rate": 2,
        "time0": 10,
        "time_rate": 2
    },
    "weapons_technology": {
        "name": "Weapons Technology",
        "requirements": [
            ["research_lab", 4],
        ],
        "costs0": {
            "metal": 800,
            "crystal": 200,
            "deuterium": 0
        },
        "costs_rate": 2,
        "time0": 10,
        "time_rate": 2
    },
    "shielding_technology": {
        "name": "Shielding Technology",
        "requirements": [
            ["research_lab", 6],
            ["energy_technology", 3],
        ],
        "costs0": {
            "metal": 200,
            "crystal": 600,
            "deuterium": 600
        },
        "costs_rate": 2,
        "time0": 10,
        "time_rate": 2
    },
}

SHIPS = {
    "light_fighter": {
        "name": "Light Fighter",
        "costs": {
            "metal": 3000,
            "crystal": 1000,
            "deuterium": 0
        },
        "time": 2,
        "hull": 400,
        "shield": 20,
        "weapon": 80,
        "speed": 12500,
        "fuel_consumption": 20,
        "cargo_capacity": 50
    },
    "heavy_fighter": {
        "name": "Heavy Fighter",
        "costs": {
            "metal": 6000,
            "crystal": 4000,
            "deuterium": 0
        },
        "time": 2,
        "hull": 1000,
        "shield": 25,
        "weapon": 150,
        "speed": 12500,
        "fuel_consumption": 75,
        "cargo_capacity": 100
    },
    "cruiser": {
        "name": "Cruiser",
        "costs": {
            "metal": 20000,
            "crystal": 7000,
            "deuterium": 2000
        },
        "time": 2,
        "hull": 2700,
        "shield": 50,
        "weapon": 400,
        "speed": 15000,
        "fuel_consumption": 300,
        "cargo_capacity": 800
    },
    "battleship": {
        "name": "Battleship",
        "costs": {
            "metal": 45000,
            "crystal": 15000,
            "deuterium": 0
        },
        "time": 2,
        "hull": 6000,
        "shield": 200,
        "weapon": 1000,
        "speed": 10000,
        "fuel_consumption": 500,
        "cargo_capacity": 1500
    },
    "battlecruiser": {
        "name": "Battlecruiser",
        "costs": {
            "metal": 30000,
            "crystal": 40000,
            "deuterium": 15000
        },
        "time": 2,
        "hull": 7000,
        "shield": 400,
        "weapon": 700,
        "speed": 10000,
        "fuel_consumption": 250,
        "cargo_capacity": 750
    },
    "bomber": {
        "name": "Bomber",
        "costs": {
            "metal": 50000,
            "crystal": 25000,
            "deuterium": 15000
        },
        "time": 2,
        "hull": 7500,
        "shield": 500,
        "weapon": 1000,
        "speed": 4000,
        "fuel_consumption": 1000,
        "cargo_capacity": 500
    },
    "destroyer": {
        "name": "Destroyer",
        "costs": {
            "metal": 60000,
            "crystal": 50000,
            "deuterium": 15000
        },
        "time": 2,
        "hull": 11000,
        "shield": 500,
        "weapon": 2000,
        "speed": 5000,
        "fuel_consumption": 1000,
        "cargo_capacity": 2000
    },
    "deathstar": {
        "name": "Deathstar",
        "costs": {
            "metal": 5000000,
            "crystal": 4000000,
            "deuterium": 1000000
        },
        "time": 2,
        "hull": 900000,
        "shield": 50000,
        "weapon": 200000,
        "speed": 100,
        "fuel_consumption": 1,
        "cargo_capacity": 1000000
    },
    "small_cargo_ship": {
        "name": "Small Cargo Ship",
        "costs": {
            "metal": 2000,
            "crystal": 2000,
            "deuterium": 0
        },
        "time": 2,
        "hull": 400,
        "shield": 10,
        "weapon": 5,
        "speed": 5000,
        "fuel_consumption": 10,
        "cargo_capacity": 5000
    },
    "large_cargo_ship": {
        "name": "Large Cargo Ship",
        "costs": {
            "metal": 6000,
            "crystal": 6000,
            "deuterium": 0
        },
        "time": 2,
        "hull": 1200,
        "shield": 25,
        "weapon": 5,
        "speed": 7500,
        "fuel_consumption": 50,
        "cargo_capacity": 25000
    },
    "colony_ship": {
        "name": "Colony Ship",
        "costs": {
            "metal": 10000,
            "crystal": 20000,
            "deuterium": 10000
        },
        "time": 2,
        "hull": 3000,
        "shield": 100,
        "weapon": 50,
        "speed": 2500,
        "fuel_consumption": 1000,
        "cargo_capacity": 7500
    },
    "recycler": {
        "name": "Recycler",
        "costs": {
            "metal": 10000,
            "crystal": 6000,
            "deuterium": 2000
        },
        "time": 2,
        "hull": 1600,
        "shield": 10,
        "weapon": 1,
        "speed": 2000,
        "fuel_consumption": 300,
        "cargo_capacity": 20000
    },
    "espionage_probe": {
        "name": "Espionage Probe",
        "costs": {
            "metal": 0,
            "crystal": 1000,
            "deuterium": 0
        },
        "time": 2,
        "hull": 100,
        "shield": 0.01,
        "weapon": 0.01,
        "speed": 100000000,
        "fuel_consumption": 1,
        "cargo_capacity": 5
    },
    "solar_satellite": {
        "name": "Solar Satellite",
        "costs": {
            "metal": 0,
            "crystal": 2000,
            "deuterium": 500
        },
        "time": 2,
        "hull": 200,
        "shield": 1,
        "weapon": 1,
        "speed": 0,
        "fuel_consumption": 0,
        "cargo_capacity": 0
    },
}