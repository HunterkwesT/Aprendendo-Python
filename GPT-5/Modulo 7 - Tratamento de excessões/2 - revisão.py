pessoa = {
    "nome": "Alexandre",
    "idade": 28
}

numeros = [10, 20, 30]

try:
    id_chave = input("Chave: ")
    p = pessoa[f"{id_chave}"]

    id_lista = int(input("Lista: "))
    l = numeros[id_lista]

except KeyError:
    print("Chave não encontrada")

except IndexError:
    print(f"A chave {id_chave} tem valor {p}")
    print("Essa posição não existe na lista")

except ValueError:
    print(f"A chave {id_chave} tem valor {p}")
    print("Indice não aceito")

else:
    print(f"A chave {id_chave} tem valor {p}")
    print(f"O numero na posição {id_lista} é {l}")
    print("Tudo ocorreu bem!")

finally:
    print("encerrado")