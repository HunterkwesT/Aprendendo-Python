try:
    divisor = abs(int(input(f"insira um numero: ")))
    resultado = 100 / divisor

    try:
        with open("dados.txt", "r") as text:
            print(text.read())      

    except FileNotFoundError:
        print("Arquivo não encontratdo!")  

except ValueError:
    print("Valor invalido!")

except ZeroDivisionError:
    print("Valor zero não aceito!")

else:
    print(f"Resultado: {resultado}")

finally:
    print("Processo encerrado")