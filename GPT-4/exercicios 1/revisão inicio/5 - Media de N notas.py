qnt_notas = int(input("quantas notas seram tratadas: "))
notas = []

for i in range(qnt_notas):
    notas.append(int(input(f"nota {i+1}: ")))

print(sum(notas) / len(notas))

