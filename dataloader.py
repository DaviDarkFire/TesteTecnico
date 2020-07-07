from pessoa import Pessoa
from familia import Familia
import json

'''
    Classe responsável por carregar os Dados do arquivo "dados.json". Resolvi
    colocar uma verificação de elegibilidade dos objetos "família", se esta
    não for elegível nem a carregamos. Talvez essa não seja uma boa prática, mas
    foi a solução encontrada pra resolver a falta de memória ocasionada por dados
    muito grandes.
'''

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

            if(familia.elegivel): #se a familia não for elegível nem adiciono ela na lista
                familias.append(familia)
                carregados += 1

        return familias

    def criaListaObjPessoa(self, listaDicionarioPessoa): #convertendo os registros de dicionário para objeto
        pessoas = []

        for dicionario in listaDicionarioPessoa:
             pess = Pessoa(dicionario['id'], dicionario['nome'], dicionario['tipo'],
                           dicionario['dataDeNascimento'])
             pessoas.append(pess)

        return pessoas

