from abc import ABC, abstractclassmethod

def linha():
    print("=+=+"*69)

class Funcionario(ABC):
    @abstractclassmethod

    def __init__(self, nome, cpf, numero, endereco, salario):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.endereco = endereco
        self.salario = salario

    #MÉTODO GET
    def get_nome(self):
        return self.nome

    def get_cpf(self):
        return self.cpf

    def get_numero(self):
        return self.numero

    def get_endereco(self):
        return self.endereco

    def get_salario(self):
        return self.salario

    #MÉTODO SET
    def set_nome(self, novo_nome):
        self.novo_nome = novo_nome

    def set_cpf(self, novo_cpf):
        self.novo_cpf = novo_cpf

    def set_numero(self, novo_numero):
        self.novo_numero = novo_numero

    def set_endereco(self, novo_endereco):
        self.novo_endereco = novo_endereco

    def set_salario(self, novo_salario):
        self.novo_salario = novo_salario

    @abstractclassmethod
    def compute_salario(cls):
        pass


class Empregado(Funcionario):
    def __init__(self, nome, cpf, numero, endereco, salario, decimo_terceiro):
        super().__init__(nome, cpf, numero, endereco, salario)
        self.decimo_terceiro = decimo_terceiro

    def get_decimo_terceiro(self):
        return self.decimo_terceiro

    def set_decimo_terceiro(self, extra):
        self.extra = extra

    def compute_salario(self):
        salario_total = self.decimo_terceiro + 200
        return salario_total

    def mostrar_dados(self):
        print(f"\nNome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Número: {self.numero}")
        print(f"Endereço: {self.endereco}")
        print(f"Salário: R${self.salario:.2f}")
        print(f"Décimo Terceiro: {self.decimo_terceiro}")

if __name__ == "__main__":
    funcionario1 = Empregado("Leanderson",785612341896, 912345678, "Rolândia 69 rua 4", 2500,1250,)
    funcionario2 = Empregado("Gildásio", 12345678910, 915594847, "Asa SUl", 45000,24500)
    funcionario3 = Empregado("Nelson", 98765432103, 998765432, "Rua Nobre Claudio Rodrigues Pinto", 19000,9500)

    linha()
    funcionario1.mostrar_dados()
    linha()
    funcionario2.mostrar_dados()
    linha()
    funcionario3.mostrar_dados()
    linha()
