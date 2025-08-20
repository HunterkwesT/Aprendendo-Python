import json

lista = []
for i in range(2):
    pessoa = {}
    pessoa["nome"] = input("Nome: ").strip()
    pessoa["idade"] = abs(int(input("Idade: ")))

    lista.append(pessoa)

lista = sorted(lista, key=lambda pessoa: pessoa["nome"])

with open("Modulo 6 - exercicio 2.json", "w", encoding="utf-8") as arquivo:
    json.dump(lista, arquivo, ensure_ascii=False, indent=2)

with open("Modulo 6 - exercicio 2.json", "r", encoding="utf-8") as arquivo:
    item = json.load(arquivo)
    for pessoa in item:
        print(f"{pessoa["nome"]} tem {pessoa["idade"]} anos")