class Produto:
    def __init__(self,nome,preço):
        self.nome = nome
        self.preço = preço

    def desconto(self):
        self.preço -= self.preço * 0.1
    
    def __str__(self):
        return f"Produto: {self.nome} - R${self.preço}\n"
    
produto = []

for i in range(3):
    nome = input("Nome: ")
    preço = float(input("Valor: "))
    produto.append(Produto(nome,preço))

for i in produto:
    print(i)
    i.desconto()
    print(i)
