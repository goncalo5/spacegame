# resources
RESOURCES = ['metal', 'crystal']
# Metal
# initials
# distance=TOTAL, velocity=por segundo=D_TOTAL, aceleracao=rate por segundo=D2_TOTAL
METAL = {'TOTAL': 1000, 'PER_S': 1}
# rate de quanto aumenta o metal ganho
METAL['RATE_PER_S'] = 1.5  # exponencial  RATE__METAL ^ nivel

# buildings
BUILDINGS = {'metal_mine': {'cost': 10, 'rate_cost': 1.5, 'time': 5, 'rate_t': 2,
                            'per_s': 1, 'rate_per_s': 1.5},
             'robots factory': {'cost': 10, 'rate_cost': 2, 'time': 5, 'rate_t': 2}}

#METAL_MINE = {'name': BUILDINGS[0],
#              'cost': 10, 'rate_cost': 1.5, 'time': 5, 'rate_t': 2}
# efeitos: METAL[PER_S] *= METAL[RATE]


#ROBOT_FAC = {'name': BUILDINGS[1],
#             'cost': 10, 'rate_cost': 2, 'time': 5, 'rate_t': 2}

# efeitos BUILDINGS[TIME] /= 2
RATE_FB = 2

# times
TIME2UPDATE_DB = 10
TIME2REFRESH = 3