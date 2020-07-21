#o objeto tem caracteristicas e funções e métodos
#importando pro main
#dentro do arquivo veiculo, importa a classe Veiculo
from veiculo import Veiculo
from carro import Carro
#tem que passar os 3 argumentos, (cor, marca, tanque)
#criado caminhao
#print(caminhao) mostrar que é objeto
# mostrar que tem o tipo veiculo print(type(caminhao))
caminhao = Veiculo('branco','ford', 50, 'F-14000')
print('>>> CADASTRO DE CAMINHÃO <<<')

print('cor do veículo:', caminhao.cor)
print('marca:', caminhao.marca)
print('tanque atual:', caminhao.tanque)
print('nome:', caminhao.nome)
print('')

caminhao.abastecer(40)
print('Você abasteceu + 40L no:', caminhao.nome)
print('tanque atual:', caminhao.tanque)
print('')

carro = Carro('preto','volkswagen', 30, 'T-Cross')
print('>>> CADASTRO DE  CARRO <<<')
print('cor do veiculo:', carro.cor)
print('marca:', carro.marca)
print('tanque atual:', carro.tanque)
print('nome:', carro.nome)

print('')

carro.abastecer(10)
print('Você abasteceu + 10L no:', carro.nome)
print('tanque atual:', carro.tanque)
print('')

carro.abastecer(20)
print('')
print('tanque atual:', carro.tanque)













