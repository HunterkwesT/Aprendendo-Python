lista = {1,5,8,6,4}

print(f"{lista}\n")

for i in range(2):
    lista.add(int(input(f"Numero {i+1}: ")))

print(f"\n{lista}\n")

lista.discard(int(input("Numero a ser removido: ")))

print(f"\n{lista}\n")
