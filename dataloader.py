from pessoa import Pessoa
from familia import Familia
import json

class Dataloader:
    def __init__(self, caminhoJson, qtdFamiliasCarregar):
        self.caminhoJson = caminhoJson
        self.qtdFamiliasCarregar = qtdFamiliasCarregar

    def abrirArquivo(self):
        with open(self.caminhoJson, 'r') as f:
            arquivo = json.load(f)
        carregados = 0
        familias = []

        for registro in arquivo:
            if carregados == self.qtdFamiliasCarregar:
                break
            pessoas = self.criaListaObjPessoa(registro['pessoas'])
            familia = Familia(registro['id'], pessoas, registro['rendas'], registro['status'])
            familias.append(familia)
            carregados += 1

        return familias

    def criaListaObjPessoa(self, listaDicionarioPessoa): #convertendo os registro de dicionário para objeto
        pessoas = []

        for dicionario in listaDicionarioPessoa:
             pess = Pessoa(dicionario['id'], dicionario['nome'], dicionario['tipo'],
                           dicionario['dataDeNascimento'])
             pessoas.append(pess)

        return pessoas

if __name__ == "__main__":
    dat  = Dataloader("dados.json", 500)
    familias = dat.abrirArquivo()
    for f in familias:
        print(f"{f.id}: {f.pontos} \n")