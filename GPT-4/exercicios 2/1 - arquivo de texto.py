with open("1 - nomes.txt", "w") as arquivo:
    for i in range(3):
        arquivo.write(input(f"nome {i+1}: ")+"\n")

with open("1 - nomes.txt", "r") as arquivo:
    for a,b in enumerate(arquivo, start=1):
        print(f"{a}: {b.strip()}")