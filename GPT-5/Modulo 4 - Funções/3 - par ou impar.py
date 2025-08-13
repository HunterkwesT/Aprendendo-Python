def verifica(num):
    return "Par" if num % 2 == 0 else "Impar"

num = int(input(f"Numero: "))

print(f"Numero {num} é {verifica(num)}!")