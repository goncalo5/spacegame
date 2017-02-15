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

MINA_METAL = {'NOME': EDIFICIOS[0],
              'CUSTO': 10, 'TAXA_CUSTO': 1.5, 'TEMPO': 5, 'TAXA_T': 2}
# efeitos: METAL[POR_S] *= METAL[TAXA]


FAB_ROBOT = {'NOME': EDIFICIOS[1],
             'CUSTO': 10, 'TAXA_CUSTO': 2, 'TEMPO': 5, 'TAXA_T': 2}

# efeitos EDIFICIOS[TEMPO] /= 2
TAXA_FB = 2