from datetime import date
import json
'''
    Classe responsável por tratar e exportar os atributos da familia que
    foi contemplada
'''

class FamiliaContemplada:
    def __init__(self, idFamilia, criteriosAtend, pontosTot, dataSelec):
        self.idFamilia = idFamilia
        self.criteriosAtend = criteriosAtend
        self.pontosTot = pontosTot
        self.dataSelec = dataSelec

class Contemplados:
    def __init__(self):
        self.familiasContempladas = []

    def criarListaContemplados(self, familias):
        dataSelec = date.today().strftime("%Y-%b-%d")
        for fam in familias:
            familia = FamiliaContemplada(fam.id, fam.qtdCriteriosAtendidos, fam.pontos, dataSelec)
            self.familiasContempladas.append(familia)

    def exportContemplados(self):
        saida = open("contemplados.json","w")
        flag = 0
        saida.write("[")
        for familia in self.familiasContempladas:
            if flag:
                saida.write(",")
            flag = 1
            saida.write("\n")
            saida.write(json.dumps({"id": familia.idFamilia,"qtdCriterios": familia.criteriosAtend, "pontos": familia.pontosTot, "data": familia.dataSelec}, ensure_ascii=False))
        saida.write("]")
        saida.close()


