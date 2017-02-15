# from Tkinter import *
# from constantes import *
from cabecalho import *


class Game(object):
    def __init__(self):
        self.i = Tk()
        self.i.title('Ogame')

        # Recursos Disponiveis
        # cabecalho
        Label(self.i, text='Recurso').grid(row=0, column=0)
        Label(self.i, text='por seg').grid(row=1, column=0)
        Label(self.i, text='Total').grid(row=2, column=0)
        # criar objetos dos recursos
        self.metal = Recursos(RECURSOS[0], METAL['TOTAL'],
                              METAL['POR_S'], METAL['TAXA_POR_S'])
        self.recursos = [self.metal]
        for n, r in enumerate(self.recursos):
            Label(self.i, text=r.nome).grid(row=0, column=1 + n)
            r.l_por_s = Label(self.i, text=r.por_s)
            r.l_por_s.grid(row=1, column=1 + n)
            r.l_total = Label(self.i, text=r.total)
            r.l_total.grid(row=2, column=1 + n)

        # Edicios
        # criar objetos dos edificios
        self.mina_metal = Edificios(self.i, lv=0, evol=False,
                                    falta=MINA_METAL['tempo'],
                                    **MINA_METAL)

        self.fab_robot = Edificios(self.i, lv=0, evol=False,
                                   falta=FAB_ROBOT['tempo'], **FAB_ROBOT)

        # Cabecalho
        cab = Cabecalho(self.i, 3, 0)
        self.edificios = [self.mina_metal, self.fab_robot]
        self.minas = [self.mina_metal]
        for n, e in enumerate(self.edificios):
            l = cab.l + 2 + n
            Label(self.i, text=e.NOME).\
                grid(row=l, column=cab.c)
            # Nivel
            e.l_lv = Label(self.i, text=e.lv)
            e.l_lv.grid(row=l, column=cab.c + 1)
            # Custo para evoluir
            e.l_custo = Label(self.i, text=int(e.custo))
            e.l_custo.grid(row=l, column=cab.c_custos)
            # Tempo para evoluir
            e.l_t = Label(self.i, text=int(e.t))
            e.l_t.grid(row=l, column=cab.c_t)
            # Evoluir
        # criar Botoes
        l = cab.l + 2
        self.mina_metal.b_lv = \
            Button(text='Evoluir mina', command=lambda: self.evoluir(self.mina_metal))
        self.mina_metal.b_lv.grid(row=l, column=cab.c_evol)
        self.fab_robot.b_lv = \
            Button(text='Evoluir fabrica', command=lambda: self.evoluir(self.fab_robot))
        self.fab_robot.b_lv.grid(row=l + 1, column=cab.c_evol)

        self.atualizando_recursos()

        self.i.mainloop()

    def evoluir(self, e):
        if self.metal.total >= e.custo and not e.evol:
            self.metal.total -= e.custo
            self.metal.l_total['text'] = int(self.metal.total)
            e.evol = True
            self.loop_evoluir(e)

    def loop_evoluir(self, e):
        if e.evol:
            e.falta -= 1
            if e.falta <= 0:
                e.lv += 1
                e.custo = e.CUSTO * e.TAXA_CUSTO ** e.lv
                e.t = (e.T * e.TAXA_T ** e.lv) / \
                      (TAXA_FB ** self.fab_robot.lv)
                # Labels
                e.l_lv['text'] = e.lv
                e.l_custo['text'] = int(e.custo)
                e.l_t['text'] = int(e.t)

                e.falta = e.t
                e.evol = False

                # efeitos da evolucao
                if e.NOME == 'mina de metal':
                    self.metal.por_s = \
                        METAL['POR_S'] * METAL['TAXA_POR_S']**self.mina_metal.lv
                    self.metal.l_por_s['text'] = int(self.metal.por_s)
                if e.NOME == 'fabrica de robots':
                    self.atualizar_edificios()
            e.l_t['text'] = int(e.falta)

            self.i.after(1000, lambda: self.loop_evoluir(e))

    def atualizar_recursos(self):
        for r in self.recursos:
            r.total += r.por_s
            r.l_total['text'] = int(r.total)

    def atualizando_recursos(self):
        self.atualizar_recursos()
        self.i.after(1000, self.atualizando_recursos)

    def atualizar_edificios(self):
        for e in self.edificios:
            e.t = e.falta = (e.T * e.TAXA_T ** e.lv) / (TAXA_FB ** self.fab_robot.lv)
            e.l_t['text'] = int(e.t)


class Recursos(object):
    def __init__(self, nome, total, por_s, taxa_por_s):
        self.l_total = self.l_por_s = None
        self.nome = nome
        self.total = total
        self.por_s = por_s
        self.taxa_por_s = taxa_por_s


class Edificios(object):
    def __init__(self, i, lv, falta, evol,
                 nome, custo, taxa_custo, tempo, taxa_t):
        self.i = i
        self.l_lv = self.l_custo = self.l_t = None

        # constantes
        self.NOME = nome
        self.CUSTO = custo
        self.TAXA_CUSTO = taxa_custo
        self.T = tempo
        self.TAXA_T = taxa_t

        # variaveis
        self.lv = lv  # level
        self.custo = self.CUSTO * self.TAXA_CUSTO**self.lv
        self.t = self.T * self.TAXA_T**self.lv
        self.evol = evol
        self.falta = falta


if __name__ == '__main__':
    Game()
