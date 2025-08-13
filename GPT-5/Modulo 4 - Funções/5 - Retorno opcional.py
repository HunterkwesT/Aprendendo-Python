def oi(resp = "Visitante"):
    print( f"Olá, {resp}")

nome = input("Quem és tú?\nMim ser: ")

if not nome:
    oi()
else:
    oi(nome)

oi() if not nome else oi(nome)