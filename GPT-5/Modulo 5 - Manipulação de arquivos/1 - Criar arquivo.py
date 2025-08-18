with open("Modulo 5 - exercicio 1.txt","w") as arquivo:
    for i in range(3):
        arquivo.write(input(f"Nome {i+1}: ")+"\n")