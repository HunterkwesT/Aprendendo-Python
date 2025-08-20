import json

pessoa = {}
pessoa["nome"] = input("Nome: ").strip()
pessoa["idade"] = abs(int(input("Idade: ")))

try:
    with open("Modulo 6 - exercicio 3.json", "r", encoding="utf-8") as arquivo:
        item = json.load(arquivo)

        with open("Modulo 6 - exercicio 3.json", "w", encoding="utf-8") as arquivo:
            item.append(pessoa)
            item = sorted(item, key=lambda p: p["nome"])
            json.dump(item, arquivo, ensure_ascii=False, indent=2)

except FileNotFoundError:
    lista = []
    lista.append(pessoa)

    with open("Modulo 6 - exercicio 3.json", "w", encoding="utf-8") as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False, indent=2)