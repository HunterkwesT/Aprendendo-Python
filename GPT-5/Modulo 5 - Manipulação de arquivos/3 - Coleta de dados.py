nome = input("Nome: ")
idade = input("Idade: ")

with open("Modulo 5 - exercicio 3.txt","w") as arquivo:
    arquivo.write(nome+";"+idade)

with open("Modulo 5 - exercicio 3.txt","r") as arquivo:
    for linha in arquivo:
        lenome,leidade = linha.strip().split(";")
        print(f"{lenome} tem {leidade} anos.")