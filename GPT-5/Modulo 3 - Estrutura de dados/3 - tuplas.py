lista = []

for i in range(4):
    lista.append(float(input(f"nota {i+1}: ")))

lista = tuple(lista)

print(f"media: {sum(lista)/len(lista):.2f}")