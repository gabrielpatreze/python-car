#herdar caracteristicas do veiculo
from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, cor, marca, tanque, nome):
        Veiculo.__init__(self, cor, marca, tanque, nome)

    def abastecer(self, litros):
        if self.tanque + litros >= 50:
            print('>> Você tentou abastecer', litros, 'litros <<')
            print('')
            print('>> Limite do tanque é 50L, não irá abastecer mais <<')

        else:
            self.tanque += litros

#carro esta limitado a 50 litros, caminhão esta ilimitado