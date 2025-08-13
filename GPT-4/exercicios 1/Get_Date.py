from datetime import date

ano = date.today().year
dia = date.today().day
mes = date.today().month

def format(valor):
    if valor < 10:
        valor = '%02d' % valor
        return valor
    else:
        return valor

print(f"{format(dia)}/{format(mes)}/{ano}")