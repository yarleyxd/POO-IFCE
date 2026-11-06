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
    alunos[0].adicionar_nota(8.5)
    alunos[0].adicionar_nota(7.0)

    alunos[0].registrar_falta()
    alunos[0].registrar_falta()

    if not alunos[0].adicionar_nota(11):
        print("Nota inválida: use um valor entre 0 e 10.")

    if not alunos[0].adicionar_nota(-2):
        print("Nota inválida: use um valor entre 0 e 10.")

if len(alunos) >= 2:
    alunos[1].adicionar_nota(5.5)

    for i in range(6):
        alunos[1].registrar_falta()

    if not alunos[1].set_matricula(""):
        print("Matrícula inválida: não pode ser vazia.")

for aluno in alunos:
    print(aluno)

    if aluno.verificar_aprovacao(40):
        print("Situação: aprovado")
    else:
        print("Situação: reprovado")

maior_media = None

for aluno in alunos:
    if maior_media is None or aluno.calcular_media() > maior_media.calcular_media():
        maior_media = aluno

if maior_media is not None:
    print(f"Maior média: {maior_media.nome} ({maior_media.calcular_media():.2f})")
else:
    print("Nenhum aluno cadastrado.")