class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, eu sou o {self.nome} e tenho {self.idade} anos")


nome = input("Digite seu nome: ")
try:
    idade = abs(int(input("digite sua idade: ")))
except ValueError:
    print("idade invalida")
else:
    objeto = Pessoa(nome,idade)
    objeto.apresentar()