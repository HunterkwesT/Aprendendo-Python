nomes = []

for i in range(5):
    nomes.append(input(f"Nome {i+1}: "))

unicos = set(nomes)

print(f"Nomes unicos: {unicos}")