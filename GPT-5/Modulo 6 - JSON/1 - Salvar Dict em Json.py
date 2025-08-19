import json

dados = {}

dados["nome"] = input("Nome: ").strip()
dados["idade"] = abs(int(input("Idade: ")))
dados["cidade"] = input("Cidade: ").strip()
 
with open("Modulo 6 - exercicio 1.json","w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=2)

with open("Modulo 6 - exercicio 1.json", "r", encoding="utf-8") as arquivo:
    lidos = json.load(arquivo)

print(f"Nome: {lidos["nome"]}, Idade: {lidos["idade"]} anos, Cidade: {lidos["cidade"]}")