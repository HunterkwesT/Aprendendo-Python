class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print(f"Pessoa: {self.nome}, {idade} anos")

cadastro = []
for i in range(2):
    print(f"Pessoa {i+1}")
    nome = input("Nome: ")
    idade = input("Idade: ")
    cadastro.append(Pessoa(nome,idade))

for i in range(len(cadastro)):
    cadastro[i].apresentar()

for i in cadastro:
    i.apresentar()