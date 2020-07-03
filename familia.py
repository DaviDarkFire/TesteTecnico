
class Familia:
    def __init__(self, id, pessoas, rendas, status):
        self.id = id
        self.pessoas = pessoas[:] #como pessoas e rendas são listas, a cópia por padrão é por referência
        self.rendas = rendas[:] #[:] indica cópia de valores ao invés de referência
        self.status = status
        self.pontos = 0
        self.elegivel = 0 #indica se a família é elegível para participar
        #0 não elegível, 1 elegível
