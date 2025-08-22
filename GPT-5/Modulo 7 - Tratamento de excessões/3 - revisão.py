valor = "100"
print("Opções: ")
print("1 - Type Error")
print("2 - Attribute Error")
print("3 - Soma corrigida")
opcao = abs(int(input()))
match opcao:
    case 1:
        try:   
            valor = valor + 10
        except TypeError:
            print("Erro")
    case 2:
        try:
            valor.append(5)
        except AttributeError:
            print("Erro")
    case 3:
        try:
            valor = int(valor)
            valor = valor + 10
        except:
            print("erro na conversão")
        else:
            print(f"{valor}")
    case _:
        print("opção invalida")