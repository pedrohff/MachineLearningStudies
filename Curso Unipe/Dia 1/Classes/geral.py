from cliente import *
from funcionario import *

aa = Cliente(codigo=15, credito=15.0, cpf='0384803', nome='Pedro')

print(aa.nome)

aa.aumentar()
print(aa.credito)

bb = Funcionario(cpf='081828283847', nome='Henrique', matricula='151034140', salarioBase=500.00)
bb.reajustar()
print(bb.salarioBase)


