from datetime import date

class Pessoa:
    def __init__(self, id, nome, tipo, dataNasc):
        self.id  = id
        self.nome = nome
        self.tipo = tipo
        self.dataNasc = dataNasc
        self.idade = self.conseguirIdade()

    def conseguirIdade(self):
        anoNasc  = self.dataNasc.split('-')[0] #separando o ano da data recebida
        anoAtual = str(date.today()).split('-')[0]
        return int(anoAtual) - int(anoNasc) #converto do formato string para inteiro, subtraio e retorno

if __name__ == "__main__":
    pess = Pessoa(123,"Joana","Dependente","2005-04-28")
    print(pess.idade)