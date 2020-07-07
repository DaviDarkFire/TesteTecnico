'''
    Classe responsável por armazenar os atributos de familia e alguns
    métodos relacionados, como cálculo de idade baseado na data de nascimento,
    verificação da maioridade dos dependentes, cálculo da renda total da família
    e cálculo dos seus pontos.
'''
from metricas import Metricas
class Familia:
    def __init__(self, id, pessoas, rendas, status):
        self.id = id
        self.pessoas = pessoas
        self.rendas = rendas
        self.status = status
        self.pontos = 0 #indica os pontos da família
        self.elegivel = Metricas.conseguirElegibilidade(self.status) #indica se a família é elegível para participar: 0 não elegível, 1 elegível
        self.rendaTotal = self.calcRenda()
        self.qtdCriteriosAtendidos = 3 #colocar o máximo e decrementar caso algum não seja atendido

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
        else:
            self.qtdCriteriosAtendidos -= 1

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
        elif qtdDependente < 3 and qtdDependente >= 1:
            pontos += 2
        else:
            self.qtdCriteriosAtendidos -= 1

        return pontos
