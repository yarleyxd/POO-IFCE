from aluno import Aluno

alunos = []

while True:
    nome = input("Nome do aluno (Enter para sair): ")

    if nome == "":
        break

    matricula = input("Matrícula: ")

    aluno = Aluno(nome, matricula)
    alunos.append(aluno)

if len(alunos) >= 1:
    alunos[0].notas.append(8.5)
    alunos[0].notas.append(7.0)
    alunos[0].faltas = 2

if len(alunos) >= 2:
    alunos[1].notas.append(5.5)
    alunos[1].faltas = 6

for aluno in alunos:
    print(f"{aluno.nome} ({aluno.matricula})")
    print(f"Notas: {aluno.notas}")
    print(f"Faltas: {aluno.faltas}")

    if len(aluno.notas) > 0:
        media = sum(aluno.notas) / len(aluno.notas)
        print(f"Média: {media:.2f}")
    else:
        print("Média: sem notas")

mais_faltas = None

for aluno in alunos:
    if mais_faltas is None or aluno.faltas > mais_faltas.faltas:
        mais_faltas = aluno

if mais_faltas is not None:
    print(f"Mais faltas: {mais_faltas.nome} ({mais_faltas.faltas})")
else:
    print("Nenhum aluno cadastrado.")