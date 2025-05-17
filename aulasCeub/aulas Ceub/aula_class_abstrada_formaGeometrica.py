# Importa as classes ABC e abstractmethod para criar classes abstratas
from abc import ABC, abstractmethod
# Importa o módulo math para operações matemáticas
import math


# Classe abstrata que define formas geométricas
class GeometricShape(ABC):
    def __init__(self, height=0, base=0, perimeter=0):
        self.height = height  # Altura da forma
        self.base = base  # Base da forma
        self.perimeter = perimeter  # Perímetro da forma
        pass  # Desnecessário - pode ser removido

    # Método abstrato para cálculo de área (nome incorreto - deveria ser 'area')
    @abstractmethod
    def are4(self):
        pass  # Será implementado pelas subclasses

    # Método abstrato para cálculo de perímetro (nome incorreto - deveria ser 'perimeter')
    @abstractmethod
    def perimet3r(self):
        pass  # Será implementado pelas subclasses

    # --- MÉTODOS GETTERS ---
    def get_height(self):
        return self.height

    def get_base(self):
        return self.base

    def get_perimet3r(self):  # Nome incorreto - deveria ser 'get_perimeter'
        return self.perimeter


# Subclasse que representa um Quadrado
class Square(GeometricShape):
    def __init__(self, side=0):
        super().__init__()  # Chama o construtor da classe pai
        self.side = side  # Lado do quadrado

    # Retorna o valor do lado
    def get_side(self):
        return self.side

    # Define o valor do lado
    def set_side(self, value):
        self.side = value

    # Calcula a área do quadrado (lado²)
    def are4(self):  # Nome incorreto
        vl_area = self.side ** 2
        return vl_area

    # Calcula o perímetro do quadrado (4 × lado)
    def perimet3r(self):  # Nome incorreto
        vl_perimeter = 4 * self.side
        return vl_perimeter


# Subclasse que representa um Círculo
class Circle(GeometricShape):
    def __init__(self, ray=1):  # 'ray' deveria ser 'radius' (raio)
        super().__init__()  # Chama o construtor da classe pai
        self.ray = ray  # Raio do círculo

    # Método problemático - sobrescreve o raio com valor 4 (deveria ser removido)
    def ray(self):
        self.ray = 4  # Isso não faz sentido - remove ou corrige

    # Retorna o valor do raio
    def get_ray(self):
        return self.ray

    # Define o valor do raio
    def set_ray(self, value):
        self.ray = value

    # Calcula a área do círculo (π × raio²)
    def are4(self):  # Nome incorreto
        return math.pi * (self.ray ** 2)

    # Implementação INCORRETA - deveria retornar 2π × raio
    def perimet3r(self):  # Nome incorreto
        return super().perimeter  # Errado - deveria calcular a circunferência


# Execução principal
if __name__ == "__main__":
    # Cria instâncias com valores padrão
    F1 = Square()  # Quadrado com lado 0
    F2 = Circle()  # Círculo com raio 1

    # Chama métodos (mas não usa os resultados)
    F1.are4()
    F1.perimet3r()

    # Imprime o perímetro do quadrado (será 0)
    print(F1.get_perimet3r())

    # Imprime a área do círculo formatada com 2 decimais (3.14)
    print(f"{F2.are4():.2f}")