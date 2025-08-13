#Tuplas são listas constantes. Não podem ser alteradas, mas podem ser verificadas
#Caso item unico "lista = (item,)"
#Conversão:
#lista = (1,2)
#lista = list(lista) -> lista = list[1,2]

lista = ("tata","tete","titi","toto","tutu")

for i,j in enumerate(lista,start=1):
    print(f"{i} - {j}")