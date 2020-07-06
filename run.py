from dataloader import Dataloader
from geradorDeDados import Gerador
import json
import time

class Run:

    def carregarDados(self, qtdFamilias):
        dat  = Dataloader("dados.json", qtdFamilias)
        return dat.abrirArquivo()

    def gerarEstatisticas(self):
        return

    def gerarDados(self, qtdFamilias):
        gen = Gerador()
        gen.carregarNomes()
        arquivo = open("dados.json","w")
        flag = 0

        arquivo.write("[")
        for i in range(qtdFamilias):
            if flag:
                arquivo.write(",")
            flag = 1
            arquivo.write(f"{json.dumps(gen.gerarFamilia(), ensure_ascii=False)}\n")
        arquivo.write("]")
        arquivo.close()

    def exibirMenu(self):
        print("Menu:\n 1 - Gerar Dados\n 2 - Exibir Classificação das Famílias\n 3 - Gerar Estatísticas dos Dados\n 4 - Exibir esse Menu\n 5 - Sair")

    def exibirPontuacoes(self, listaFamilias):
        listaFamilias.sort(key=lambda x: x.pontos, reverse=True)
        for i in listaFamilias:
            print(i.pontos)
        return 0

if __name__ == "__main__":
    run = Run()
    while True:
        try:
            tecla = input('Tecla do Menu e depois Enter:\n')
        except:
            print("\nCtrl+c, saindo.")
            break
        if tecla == '1':
            run.gerarDados(1000000)
        if tecla == '2':
            aux = time.time()
            run.exibirPontuacoes(run.carregarDados(1000000))
            print(time.time()-aux)
            #print(run.exibirPontuacoes(run.carregarDados(100)))
            #print(run.carregarDados(300))
        if tecla == '3':
            print("Em construção")
        if tecla == '4':
            print("Em construção")
        if tecla == '5':
            print("Em construção")
            break