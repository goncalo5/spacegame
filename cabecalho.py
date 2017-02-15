from Tkinter import *
from constantes import *


class Cabecalho(object):
    def __init__(self, i, linha_i, coluna_i):
        self.i = i
        self.l = linha_i  # linha superior do cabecalho
        self.c = coluna_i  # coluna inicial do cabecalho
        Label(self.i, text='Edificio').grid(row=self.l, column=self.c, rowspan=2)
        Label(self.i, text='Nivel').grid(row=self.l, column=self.c + 1, rowspan=2)

        #  Coluna inicial dos Custos
        self.c_custos = 2
        Label(self.i, text='Custo para evoluir'). \
            grid(row=self.l, column=self.c_custos, columnspan=len(RECURSOS))
        for n, r in enumerate(RECURSOS):
            # custos
            Label(self.i, text=r).grid(row=self.l + 1, column=self.c_custos + n)
        # coluna dos tempos das construcoes
        self.c_t = self.c_custos + len(RECURSOS)
        Label(self.i, text='Tempo'). \
            grid(row=self.l, column=self.c_t, rowspan=2)
        # coluna das evolucoes
        self.c_evol = self.c_t + 1
        Label(self.i, text='Evolucoes').\
            grid(row=self.l, column=self.c_evol, rowspan=2)

