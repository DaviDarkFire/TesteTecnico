
class Familia:
    def __init__(self, id, pessoas, rendas, status):
        self.id = id
        self.pessoas = pessoas
        self.rendas = rendas
        self.status = status
        self.pontos = 0 #indica os pontos da família
        self.elegivel = self.consegueElegibilidade() #indica se a família é elegível para participar: 0 não elegível, 1 elegível
        self.rendaTotal = self.calcRenda()

        if(self.elegivel): #não preciso gastar recurso computacional se a família não for elegível
            self.pontos = self.calcPontos()

    def pretendenteIdade(self):
        for pessoa in self.pessoas:
            if pessoa.tipo == "Pretendente":
                return pessoa.idade
        return 0

    def contaDependente(self):
        cont = 0
        for pessoa in self.pessoas:
            if pessoa.tipo == "Dependente" and pessoa.idade < 18:
                cont += 1
        return cont

    def calcRenda(self):
        soma = 0
        for renda in self.rendas:
            soma += renda['valor']
        return soma

    def calcPontos(self):
        pontos = 0
        if self.rendaTotal <= 900:
            pontos += 5
        elif self.rendaTotal > 900 and self.rendaTotal <= 1500:
            pontos += 3
        elif self.rendaTotal > 1500 and self.rendaTotal <= 2000:
            pontos += 1

        idade = self.pretendenteIdade()
        if idade >= 45:
            pontos += 3
        elif idade < 45 and idade >= 30:
            pontos += 2
        elif idade < 30:
            pontos += 1

        qtdDependente = self.contaDependente()
        if qtdDependente >= 3:
            pontos += 3
        elif qtdDependente < 3:
            pontos += 2

        return pontos
    def consegueElegibilidade(self):
        if (self.status == 0): #status igual a 0 é o único elegível pra conseguir as casas
            return 1
        return 0 #toda possiblilidade que não seja zero significa não elegível

if __name__ == "__main__":
    print("em construção")