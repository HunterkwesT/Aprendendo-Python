def opera(a, b):
    def soma():
        return a+b
    def subtract():
        return a-b
    def multi():
        return a*b
    def div():
        return a/b
    
    return soma(), subtract(), multi(), div()
num1 = int(input(f"Numero 1: "))
num2 = int(input(f"Numero 2: "))

soma, sub, mult, div = opera(num1, num2)

print(f"Soma: {soma}\nSubtração: {sub}\nMultiplicação: {mult}\nDivisão: {div:.2f}")