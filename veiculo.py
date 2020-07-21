#classe com letra maiuscula
class Veiculo():
#metodo dentro do veiculo metodo chamado init, sempre tem o argumento self
    def __init__(self, cor, marca, tanque, nome):
        self.cor = cor
        self.marca = marca
        self.tanque = tanque
        self.nome = nome

    def abastecer(self, litros):
        self.tanque += litros