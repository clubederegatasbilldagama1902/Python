def linha():
    print("+=+="*69)

class Produto():
    def __init__(self, nome: str, preco: float, quantidade: int, categoria: str):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.categoria = categoria

    def get_nome(self):
        return self.nome

    def set_nome(self, nome: str):
        self.nome = nome

    def get_preco(self):
        return self.preco

    def set_preco(self, preco: float):
        if preco >= 0:
            self.preco = preco
        else:
            print("Erro: O preço não pode ser negativo!.")

    def get_quantidade(self):
        return self.quantidade

    def set_quantidade(self, quantidade: int):
        self.quantidade = quantidade

    def get_categoria(self):
        return self.categoria

    def set_categoria(self, categoria: str):
        self.categoria = categoria

    def mostra_dados_atributos(self):
        print(f"\nNome: {self.nome}")
        print(f"Preço: R$ {self.preco:.2f}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Categoria: {self.categoria}\n")

    def mostra_dados_metodos(self):
        print(f"\nNome: {self.get_nome()}")
        print(f"Preço: R$ {self.get_preco():.2f}")
        print(f"Quantidade: {self.get_quantidade()}")
        print(f"Categoria: {self.get_categoria()}\n")

    def retorna_dados(self):
        return {
            "nome": self.nome,
            "preco": self.preco,
            "quantidade": self.quantidade,
            "categoria": self.categoria
        }

    def aumentar_quantidade(self, valor: int):
        if valor > 0:
            self.quantidade += valor
        else:
            print("Erro: O valor de aumento deve ser positivo.")

if __name__ == "__main__":

    produto1 = Produto("Camisa", 59.99, 100, "Vestuário")
    produto2 = Produto("Batedeira", 55.00, 50, "Eletrodoméstico")
    produto3 = Produto("Calculadora", 25.00, 200, "Eletrônicos")

    print("\nDados diretamente dos atributos:\n")
    linha()
    produto1.mostra_dados_atributos()
    linha()
    produto2.mostra_dados_atributos()
    linha()
    produto3.mostra_dados_atributos()
    linha()

    print("\nDados utilizando os métodos get:\n")
    linha()
    produto1.mostra_dados_metodos()
    linha()
    produto2.mostra_dados_metodos()
    linha()
    produto3.mostra_dados_metodos()
    linha()
    print("\nAumentando a quantidade do produto 1 em 20 unidades:\n")
    produto1.aumentar_quantidade(20)
    linha()
    produto1.mostra_dados_atributos()
    linha()
    print("\nTentando definir um preço negativo:")
    produto1.set_preco(-100)

    print("\nDados retornados do produto 1:")
    dados_produto1 = produto1.retorna_dados()
    print(dados_produto1)
