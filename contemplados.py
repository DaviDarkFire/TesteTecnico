
class FamiliaContemplada:
    def __init__(self, idFamilia, criteriosAtend, pontosTot, dataSelec):
        self.idFamilia = idFamilia
        self.criteriosAtend = criteriosAtend
        self.pontosTot = pontosTot
        self.dataSelec = dataSelec

class Contemplados:
    def __init__(self):
        self.familiasContempladas = []

    def adicionarFamilia(self, familiaContemplada):
        self.familiasContempladas.append(familiaContemplada)

if __name__ == "__main__":
    contemp = Contemplados()
    familia = FamiliaContemplada(1,3,10,"2020-07-03")
    contemp.adicionarFamilia(familia)
    print(contemp.familiasContempladas[0].dataSelec)