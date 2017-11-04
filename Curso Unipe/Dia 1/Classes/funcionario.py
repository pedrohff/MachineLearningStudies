from pessoa import Pessoa


class Funcionario(Pessoa):
    def __init__(self, nome, cpf, matricula, salarioBase):
        Pessoa.__init__(self, nome=nome, cpf=cpf)
        self.matricula = matricula
        self.salarioBase = salarioBase

    def reajustar(self):
        self.salarioBase *= 1.09