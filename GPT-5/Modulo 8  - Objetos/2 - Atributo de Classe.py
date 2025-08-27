class Carro:
    quantidade = 0
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        Carro.quantidade += 1
    
    def detalhes(self):
        print(f"Carro: <{self.marca}> <{self.modelo}>")

lista = []

while True:
    confere = input("Carro ou Vazio para fim: ")
    if not confere:
        print("\n Saiu")
        break
    else:
        marca = confere
        modelo = input("Modelo: ")
        
        lista.append(Carro(marca, modelo))

for carro in lista:
    carro.detalhes()

print(f"\n{Carro.quantidade} carros cadastrados")