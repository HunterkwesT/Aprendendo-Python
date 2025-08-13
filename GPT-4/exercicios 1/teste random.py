import random

numero_secreto = random.randint(1, 10)
tentativa = 0

while True:
    palpite = int(input("Tente adivinhar o número entre 1 e 10: "))
    tentativa += 1
    
    if palpite == numero_secreto:
        print("🎉 Parabéns! Você acertou!")
        break
    elif palpite < numero_secreto:
        print("🔼 Muito baixo. Tente um número maior.")
    else:
        print("🔽 Muito alto. Tente um número menor.")

print(f"numero de tentativas: {tentativa}")
