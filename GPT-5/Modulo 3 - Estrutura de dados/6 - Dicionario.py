turma = []

aluno = {
    "nome": "ale",
    "nota": 10
}
turma.append(aluno)

aluno = {
    "nome": "tete",
    "nota": 5.6
}
turma.append(aluno)

for i in turma:
    print(f"{i["nome"]} - {i["nota"]:.1f}")

soma = 0
for i in turma:
    soma += i["nota"]

print(f"media: {soma/len(turma):.1f}")