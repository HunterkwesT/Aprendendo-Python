with open("2 - nome,idade.txt", "w") as arquivo:
    for i in range(3):
        nome = input(f"nome da pessoa {i+1}: ")

        while True:
            try:
                idade = int(input("idade: "))
                break
            except:
                print("idade invalida")
                
        arquivo.write(f"{nome};{idade}\n")

with open("2 - nome,idade.txt", "r") as arquivo:
    for a, b in enumerate(arquivo,start=1):
        nome, idade = b.strip().split(";")
        print(f"Pessoa {a}: {nome} tem {idade} anos")