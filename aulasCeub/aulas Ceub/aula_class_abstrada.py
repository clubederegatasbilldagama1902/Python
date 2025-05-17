# Importa ABC (classe base abstrata) e abstractclassmethod para criar métodos abstratos
from abc import ABC, abstractclassmethod

# Função auxiliar para imprimir uma linha decorativa
def linha():
    print("=+=+"*69)

# Classe abstrata que define a estrutura base de um Funcionário
class Funcionario(ABC):
    @abstractclassmethod  # Decorador para método abstrato de classe
    
    # Método construtor que inicializa os atributos básicos
    def __init__(self, nome, cpf, numero, endereco, salario):
        self.nome = nome        # Nome do funcionário
        self.cpf = cpf          # CPF (deveria ser string)
        self.numero = numero    # Número de telefone
        self.endereco = endereco # Endereço completo
        self.salario = salario  # Salário base

    # --- MÉTODOS GETTERS ---
    # Retorna o nome do funcionário
    def get_nome(self):
        return self.nome

    # Retorna o CPF
    def get_cpf(self):
        return self.cpf

    # Retorna o número de telefone
    def get_numero(self):
        return self.numero

    # Retorna o endereço
    def get_endereco(self):
        return self.endereco

    # Retorna o salário
    def get_salario(self):
        return self.salario

    # --- MÉTODOS SETTERS ---
    # Atualiza o nome (COM ERRO - cria novo atributo ao invés de modificar)
    def set_nome(self, novo_nome):
        self.novo_nome = novo_nome  # ERRADO: deveria ser self.nome = novo_nome

    # Atualiza o CPF (COM ERRO - mesmo problema)
    def set_cpf(self, novo_cpf):
        self.novo_cpf = novo_cpf

    # Atualiza o número (COM ERRO)
    def set_numero(self, novo_numero):
        self.novo_numero = novo_numero

    # Atualiza o endereço (COM ERRO)
    def set_endereco(self, novo_endereco):
        self.novo_endereco = novo_endereco

    # Atualiza o salário (COM ERRO)
    def set_salario(self, novo_salario):
        self.novo_salario = novo_salario

    # Método abstrato que deve ser implementado pelas subclasses
    @abstractclassmethod
    def compute_salario(cls):
        pass

# Classe concreta que implementa um Empregado (tipo específico de Funcionário)
class Empregado(Funcionario):
    def __init__(self, nome, cpf, numero, endereco, salario, decimo_terceiro):
        super().__init__(nome, cpf, numero, endereco, salario)
        self.decimo_terceiro = decimo_terceiro  # Valor do 13º salário

    # Retorna o valor do décimo terceiro
    def get_decimo_terceiro(self):
        return self.decimo_terceiro

    # Atualiza o décimo terceiro (COM ERRO - mesmo problema dos setters)
    def set_decimo_terceiro(self, extra):
        self.extra = extra  # ERRADO: deveria ser self.decimo_terceiro = extra

    # Calcula o salário total (lógica questionável)
    def compute_salario(self):
        salario_total = self.decimo_terceiro + 200  # Por que +200?
        return salario_total

    # Exibe todos os dados do funcionário formatados
    def mostrar_dados(self):
        print(f"\nNome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Número: {self.numero}")
        print(f"Endereço: {self.endereco}")
        print(f"Salário: R${self.salario:.2f}")  # Formata com 2 casas decimais
        print(f"Décimo Terceiro: {self.decimo_terceiro}")

# Bloco principal que executa quando o arquivo é rodado diretamente
if __name__ == "__main__":
    # Cria 3 instâncias de Empregado com dados diferentes
    funcionario1 = Empregado("Leanderson",785612341896, 912345678, "Rolândia 69 rua 4", 2500,1250)
    funcionario2 = Empregado("Gildásio", 12345678910, 915594847, "Asa SUl", 45000,24500)
    funcionario3 = Empregado("Nelson", 98765432103, 998765432, "Rua Nobre Claudio Rodrigues Pinto", 19000,9500)

    # Exibe os dados de cada funcionário separados por linhas
    linha()
    funcionario1.mostrar_dados()
    linha()
    funcionario2.mostrar_dados()
    linha()
    funcionario3.mostrar_dados()
    linha()
