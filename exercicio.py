class Pessoa:
    def __init__(self, nome, idade, endereco, CPF):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.CPF = CPF

    def exibirDados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Endereço: {self.endereco}, CPF: {self.CPF}")

class Aluno(Pessoa):
    def __init__(self, nome, idade, endereco, CPF, matricula, curso):
        super().__init__(nome, idade, endereco, CPF) #é usado para evitar que eu tenha que repetir código, no caso eu teria que reescrever 4 linhas de código 
        #no caso, self.nome = nome
       # self.idade = idade
       # self.endereco = endereco
       # self.CPF = CPF
        #self.matricula = matricula
       # self.curso = curso

    def exibirDados(self):
        super().exibirDados() 
        print(f"Matrícula: {self.matricula}, Curso: {self.curso}")

class Professor(Pessoa):
    def __init__(self, nome, idade, endereco, CPF, salario, disciplina):
        super().__init__(nome, idade, endereco, CPF)
        self.salario = salario
        self.disciplina = disciplina

    def exibirDados(self):
        super().exibirDados()
        print(f"Salário: R$ {self.salario:.2f}, Disciplina: {self.disciplina}")

    def receberAumento(self, valor):
        self.salario += valor

class Responsavel(Pessoa):
    def __init__(self, nome, idade, endereco, CPF, dependente, telefone):
        super().__init__(nome, idade, endereco, CPF)
        self.dependente = dependente
        self.telefone = telefone

    def exibirDados(self):
        super().exibirDados() 
        print(f"Dependente: {self.dependente}, Contato: {self.telefone}")

class Main:
    aluno1 = Aluno("Davi", 17, "Rua A, 3", "555.555.555-55", "A2024", "Desenvolvimento de Sistemas")
    prof1 = Professor("Celso", 46, "Rua Tal, 100", "111.111.111-11", 7560.0, "Python")
    resp1 = Responsavel("Alberto", 37, "Rua Tal, 100", "000.000.000-01", "Davi", "(11) 99999-0000")

    aluno1.exibirDados()
    print("-" * 30)
    prof1.exibirDados()
    prof1.receberAumento(500)
    prof1.exibirDados()
    print("-" * 30)
    resp1.exibirDados()
