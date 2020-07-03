import hashlib
from random import randint as rdn
import json
#Aprova eu aí men, to precisando de emprego :(

class Gerador:
    def __init__(self):
        self.nomes = []
        self.qtdFamilias = 0

    def gerarHash(self, semente):
        return hashlib.sha1(semente.encode('utf-8')).hexdigest()

    def gerarFamilia(self):
        idFamilia = self.gerarHash(f"familia{self.qtdFamilias}")
        self.qtdFamilias += 1
        qtdMembros = rdn(0,5) #máximo de 7 pessoas na família
        id1 = self.gerarHash(f"pessoa{0}")
        id2 = self.gerarHash(f"pessoa{1}")
        pessoas = []
        pessoas.append({"id": id1,"nome": self.nomes[rdn(0,99)],"tipo": "Pretendente", "dataDeNascimento": self.gerarDataDeIdade(rdn(25,55))})
        pessoas.append({"id": id2,"nome": self.nomes[rdn(0,99)],"tipo": "Cônjugue", "dataDeNascimento": self.gerarDataDeIdade(rdn(25,55))})
        for i in range(qtdMembros):
            pessoas.append({"id": self.gerarHash(f"pessoa{i+2}"),"nome": self.nomes[rdn(0,99)],"tipo": "Dependente", "dataDeNascimento": self.gerarDataDeIdade(rdn(0,23))})

        rendas = []
        rendas.append({"pessoaId": id1, "valor": rdn(500,1500)})
        rendas.append({"pessoaId": id2, "valor": rdn(500,1500)})
        return {"id": idFamilia, "pessoas": pessoas, "rendas": rendas, "status": rdn(0,3)}

    def gerarDataDeIdade(self, idade):
        ano = 2020-idade
        return f"{ano}-{rdn(1,12)}-{rdn(1,31)}"

    def carregarNomes(self):
        arquivo = open("listaDeNomes.txt","r")
        for linha in arquivo.readlines():
            self.nomes.append(linha[:-1])


if __name__ == "__main__":
    gen = Gerador()
    gen.carregarNomes()
    arquivo = open("dados.json","w")
    for i in range(1000):
        arquivo.write(f"{json.dumps(gen.gerarFamilia(), ensure_ascii=False)}\n")
    arquivo.close()