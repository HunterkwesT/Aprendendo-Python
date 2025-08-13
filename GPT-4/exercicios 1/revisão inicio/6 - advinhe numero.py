import random

numero_aleatorio = random.randint(1,100)

while True:
    tentativa = int(input())
    if tentativa == numero_aleatorio:
        print("Acertou!")
        break
    elif tentativa > numero_aleatorio:
        print("tente um numero menor!")
    else:
        print("tente um numero maior!")