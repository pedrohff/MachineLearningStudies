from pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome, cpf, codigo, credito):
        Pessoa.__init__(self,nome=nome,cpf=cpf)
        self.codigo = codigo
        self.credito = credito

    def aumentar(self):
        self.credito *= 1.3

