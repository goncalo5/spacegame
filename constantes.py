# recursos
RECURSOS = ['metal', 'cristal']
# Metal
# iniciais
# distancia=TOTAL, velocidade=por segundo=D_TOTAL, aceleracao=taxa por segundo=D2_TOTAL
METAL = {'TOTAL': 1000, 'POR_S': 1}
# taxa de quanto aumenta o metal ganho
METAL['TAXA_POR_S'] = 1.5  # exponencial  TAXA__METAL ^ nivel

# Edificios
EDIFICIOS = ['mina de metal', 'fabrica de robots']

MINA_METAL = {'nome': EDIFICIOS[0],
              'custo': 10, 'taxa_custo': 1.5, 'tempo': 5, 'taxa_t': 2}
# efeitos: METAL[POR_S] *= METAL[TAXA]


FAB_ROBOT = {'nome': EDIFICIOS[1],
             'custo': 10, 'taxa_custo': 2, 'tempo': 5, 'taxa_t': 2}

# efeitos EDIFICIOS[TEMPO] /= 2
TAXA_FB = 2