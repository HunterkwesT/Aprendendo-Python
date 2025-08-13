from datetime import date

ano = date.today().year

nome = input("nome: ");
idade = int(input("idade: "));
ano_nascimento = ano-idade;
print(f"voce nasceu em {ano_nascimento}");