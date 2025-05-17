# Importa a classe ABC (Abstract Base Class) e o decorador abstractmethod do módulo abc
from abc import ABC, abstractmethod


# Define uma função que imprime uma linha decorativa
def linha():
    print("+=+=" * 69)


# Classe abstrata que representa um carro genérico
class Carro(ABC):
    # Atributo de classe que armazena o preço base para todas as instâncias
    preco_base = 100

    # Método de classe para obter o preço base
    @classmethod
    def get_preco_base(cls):
        return cls.preco_base

    # Método de classe para alterar o preço base
    @classmethod
    def set_preco_base(cls, novo_valor):
        cls.preco_base = novo_valor

    # Método inicializador que recebe o modelo do carro
    def __init__(self, modelo):
        self.modelo = modelo  # Atributo de instância para o modelo

    # Método para obter o modelo do carro
    def get_modelo(self):
        return self.modelo

    # Método para alterar o modelo do carro
    def set_modelo(self, modelo):
        self.modelo = modelo

    # Método abstrato que deve ser implementado pelas subclasses
    @abstractmethod
    def preco_diaria(self):
        pass  # A implementação será feita nas classes filhas


# Classe concreta que representa um carro econômico
class Economico(Carro):
    def __init__(self, modelo):
        super().__init__(modelo)  # Chama o inicializador da classe pai

    # Implementação do método abstrato - calcula preço com acréscimo de 5%
    def preco_diaria(self):
        valor = Carro.get_preco_base() * 1.05
        return valor


# Classe concreta que representa um carro intermediário
class Intermediario(Carro):
    def __init__(self, modelo):
        super().__init__(modelo)  # Chama o inicializador da classe pai

    # Implementação do método abstrato - calcula preço com acréscimo de 10%
    def preco_diaria(self):
        return Carro.get_preco_base() * 1.1


# Bloco que será executado quando o script for rodado diretamente
if __name__ == "__main__":
    linha()  # Imprime linha decorativa

    # Mostra o preço base de locação
    print(f"\nPreço base de locação: R${Carro.get_preco_base()},00\n")
    linha()  # Imprime linha decorativa

    # Cria uma instância de carro econômico
    economico = Economico("Uno")
    # Mostra o modelo do carro econômico
    print(f"\nO carro: {economico.get_modelo()}\n")
    linha()  # Imprime linha decorativa

    # Mostra novamente o preço base
    print(f"\nPreço básico: R${Carro.get_preco_base()},00\n")