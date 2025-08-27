def oi(resp = "Visitante"):
    print( f"Olá, {resp}")

nome = input("Quem és tú?\nMim ser: ")

oi() if not nome else oi(nome)