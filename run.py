from dataloader import Dataloader
from geradorDeDados import Gerador
import json
import time
from metricas import Metricas
from contemplados import Contemplados

'''
    Classe criada pra encapsular todas as outras e contruir uma interface com o
    usuário.
'''

FAMILIAS = 1000 #alterar para a quantidade de famílias que quiser gerar e processar

class Run:

    @classmethod
    def imprimirFamilias(self, familias):
        for familia in familias:
            print("\n")
            print(f"#### ID: {familia.id}")
            print(f"Renda total da família: {familia.rendaTotal}")
            print(f"Total de membros: {len(familia.pessoas)}")
            print(f"Total de pontos: {familia.pontos}")

    @classmethod
    def exibirMenu(self):
        print("Menu:\n 1 - Gerar Dados\n 2 - Exibir Classificação das Famílias\n 3 - Exibir esse Menu\n Ctrl+c - Sair")


if __name__ == "__main__":
    Run.exibirMenu()
    while True:

        try:
            tecla = input('Tecla do Menu e depois Enter:\n')
        except:
            print("\nCtrl+c, saindo.")
            break

        if tecla == '1':
            gen = Gerador()
            gen.gerarDados(FAMILIAS)
            Run.exibirMenu()

        elif tecla == '2':
            dat  = Dataloader("dados.json", FAMILIAS)
            contempladas = dat.abrirArquivo()
            contempladas = Metricas.elegerFamilias(contempladas)
            Run.imprimirFamilias(contempladas)

            cont = Contemplados()
            cont.criarListaContemplados(contempladas)
            cont.exportContemplados()
            Run.exibirMenu()

        elif tecla == '3':
            Run.exibirMenu()