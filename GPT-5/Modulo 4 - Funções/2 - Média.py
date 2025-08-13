def media(func):
    return sum(func)/len(func)

lista = [12,5,89,65,22,4]

print(f"Media: {media(lista):.2f}")