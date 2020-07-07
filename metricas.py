'''
    Classe responsável por implementar as métricas de seleção das famílias
'''
class Metricas:

    @classmethod
    def elegerFamilias(self, listaFamilias):
        listaFamilias.sort(key=lambda x: x.pontos, reverse=True)
        return listaFamilias

    @classmethod
    def consegueElegibilidade(self, status):
        if (status == 0): #status igual a 0 é o único elegível pra conseguir as casas
            return 1
        return 0 #toda possiblilidade que não seja zero significa não elegível

