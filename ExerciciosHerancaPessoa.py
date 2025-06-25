# Classe base que representa uma pessoa genérica
class Pessoa:
    # Método construtor que inicializa os atributos básicos
    def __init__(self, nome=str, idade=int):
        self.nome = nome      # Atributo para armazenar o nome da pessoa
        self.idade = idade    # Atributo para armazenar a idade da pessoa

    # Método para exibir informações básicas da pessoa
    def apresentar(self):
        print(f"Meu nome é {self.nome} e tenho {self.idade} anos!")


# Classe que representa um Aluno, herdando de Pessoa
class Aluno(Pessoa):
    # Método construtor que adiciona matrícula além dos atributos herdados
    def __init__(self, nome=str, idade=int, matricula=str):
        super().__init__(nome, idade)  # Chama o construtor da classe pai
        self.matricula = matricula    # Atributo específico do Aluno

    # Sobrescreve o método apresentar para incluir a matrícula
    def apresentar(self):
        super().apresentar()         # Chama o método da classe pai
        print(f"Sou aluno e minha matrícula é {self.matricula}")  # Info específica


# Classe que representa um Professor, herdando de Pessoa
class Professor(Pessoa):
    # Método construtor que adiciona disciplina além dos atributos herdados
    def __init__(self, nome=str, idade=int, disciplina=str):
        super().__init__(nome, idade)  # Chama o construtor da classe pai
        self.disciplina = disciplina  # Atributo específico do Professor

    # Sobrescreve o método apresentar para incluir a disciplina
    def apresentar(self):
        super().apresentar()          # Chama o método da classe pai
        print(f"Sou professor de {self.disciplina}")  # Info específica


# Bloco principal que executa quando o arquivo é rodado diretamente
if __name__ == "__main__":
    # Cria uma instância de Aluno com seus atributos
    aluno = Aluno("João Pedro", 14, "456123")
    
    # Cria uma instância de Professor com seus atributos
    professor = Professor("Aurelio", 37, "Matemática")

    # Chama o método apresentar() de cada objeto
    aluno.apresentar()        # Vai mostrar info do aluno + matrícula
    professor.apresentar()    # Vai mostrar info do professor + disciplina
