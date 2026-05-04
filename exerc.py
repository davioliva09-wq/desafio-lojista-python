class Gafanhoto:
    def __init__(self):
        self.idade = 12
        self.nome = "brunino"

    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f"{self.nome} é gafanhoto e tem {self.idade} anos"


g1 = Gafanhoto()
g1.nome = "Rodomilsom"
g1.idade = 89
g1.aniversario()
print(g1.mensagem())




g2 = Gafanhoto()

g2.nome = "well"
g2.idade = 9
g2.aniversario()
print(g2.mensagem())