def margem():
    print("\n=============================================================\n")

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def media(self):
        return sum(self.notas) / len(self.notas)
    
    def situacao(self):
        return "Aprovado" if self.media() >= 7 else "Reprovado"
    
    def __str__(self):
        return f"Aluno: {self.nome} | Notas: {self.notas} | Media: {self.media():.2f} | Situação: {self.situacao()}\n"
    

qtd_alunos = int(input(f"Quantos alunos: "))

aluno = []

margem()

for i in range(qtd_alunos):
    nome = input("Nome: ")
    notas = []
    for j in range(3):
        notas.append(float(input(f"Nota {j+1}: ")))    
    aluno.append(Aluno(nome,notas))
    margem()

for i in aluno:
    print(i)