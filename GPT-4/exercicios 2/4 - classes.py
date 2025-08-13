class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print(f"{self.nome}, {self.idade} anos1")
    
    def maior_idade(self):
        return self.idade >= 18
    
    def __str__(self):
        return f"{self.nome}, {self.idade} anos2"

cadastro = []

for i in range(3):
    print(f"Pessoa {i+1}")
    nome = input(f"Nome:")
    idade = int(input(f"Idade: "))
    cadastro.append(Pessoa(nome,idade))

for i in cadastro:
    if i.maior_idade():
        print(f"{i} | Maior de idade!")
    else:
        print(f"{i} | Menor de idade!")

