import json

with open("Modulo 6 - exercicio 4.json", "r", encoding="utf-8") as arquivo:
    lista_dict = json.load(arquivo)

    nome = input("Nome: ")

    encontrado = False

    for dicionario in lista_dict:
        if dicionario["nome"] == nome:
            print(f"{dicionario["nome"]} - {dicionario["idade"]}")
            encontrado = True
            break
    
    if not encontrado:
        print("Não tem!")