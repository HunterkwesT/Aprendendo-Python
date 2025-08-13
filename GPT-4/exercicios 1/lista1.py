lista = []

for i in range(5):
    lista.append(int(input(f"numero a ser armazenado ({i+1})")))

def listar(valor):
    print(f"lista dos numeros contidos na lista: {valor}")

def soma(valor):
    print(f"soma dos valores na lista: {sum(valor)}")

def media(valor):
    soma=sum(valor)
    print(f"media da soma dos valores: {soma/len(valor)}")

listar(lista)
soma(lista)
media(lista)