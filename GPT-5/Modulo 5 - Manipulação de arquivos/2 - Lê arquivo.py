with open("Modulo 5 - exercicio 1.txt","r") as arquivo:
    for i,linha in enumerate(arquivo, start=1):
        print(f"{i} - {linha.strip()}")