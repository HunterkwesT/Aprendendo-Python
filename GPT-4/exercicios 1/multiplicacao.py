num = int(input("numero: "))

def format(valor):
    if valor < 10:
        valor = '%02d' % valor
        return valor
    else:
        return valor

for i in range(1,11):
    print(f"{format(num)} x {format(i)} = {format(num*i)}")