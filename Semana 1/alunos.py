# Questão 2 - Cadastro de Alunos e Notas

def exibir_menu():
    print("===== CADASTRO DE ALUNOS =====")
    print("1 - Adicionar aluno")
    print("2 - Atualizar notas")
    print("3 - Remover aluno")
    print("4 - Exibir alunos e notas")
    print("5 - Exibir médias")
    print("0 - Sair")


def ler_texto(mensagem):
    while True:
        nome = input(mensagem).strip().title()

        if nome:
            return nome

        print("O nome não pode ficar vazio!")


def ler_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem).replace(",", "."))

            if 0 <= nota <= 10:
                return nota

            print("A nota deve estar entre 0 e 10!")

        except ValueError:
            print("Digite uma nota válida!")


def ler_quatro_notas():
    notas = []

    for i in range(1, 5):
        nota = ler_nota(f"Digite a nota N{i}: ")
        notas.append(nota)

    return notas


def adicionar_aluno(alunos, nome, notas):
    if nome in alunos:
        print("Aluno já cadastrado! Utilize a opção de atualizar notas.")
    else:
        alunos[nome] = notas
        print("Aluno cadastrado com sucesso!")


def atualizar_notas(alunos, nome, notas):
    if nome in alunos:
        alunos[nome] = notas
        print("Notas atualizadas com sucesso!")
    else:
        print("Aluno não encontrado!")


def remover_aluno(alunos, nome):
    if nome in alunos:
        del alunos[nome]
        print("Aluno removido com sucesso!")
    else:
        print("Aluno não encontrado!")


def calcular_media(notas):
    return sum(notas) / len(notas)


def exibir_alunos(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado")
        return

    print("===== ALUNOS E NOTAS =====")

    for nome, notas in alunos.items():
        print(f"Aluno: {nome}")
        print(f"N1: {notas[0]:.2f}")
        print(f"N2: {notas[1]:.2f}")
        print(f"N3: {notas[2]:.2f}")
        print(f"N4: {notas[3]:.2f}")


def exibir_medias(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado")
        return

    print("===== MÉDIAS DOS ALUNOS =====")

    for nome, notas in alunos.items():
        media = calcular_media(notas)
        print(f"Aluno: {nome} | Média: {media:.2f}")


def main():
    alunos = {
        "Ana": [8.5, 7.0, 9.2, 6.8],
        "Carlos": [5.5, 6.0, 7.5, 8.0],
        "Mariana": [9.0, 8.5, 10.0, 9.8],
        "Lucas": [6.5, 7.2, 5.8, 6.9],
        "Fernanda": [7.8, 8.2, 7.0, 8.5]
    }

    while True:
        exibir_menu()

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida! Digite um número.")
            continue

        if opcao == 1:
            nome = ler_texto("Nome do aluno: ")
            notas = ler_quatro_notas()
            adicionar_aluno(alunos, nome, notas)

        elif opcao == 2:
            nome = ler_texto("Nome do aluno que deseja atualizar: ")
            notas = ler_quatro_notas()
            atualizar_notas(alunos, nome, notas)

        elif opcao == 3:
            nome = ler_texto("Nome do aluno que deseja remover: ")
            remover_aluno(alunos, nome)

        elif opcao == 4:
            exibir_alunos(alunos)

        elif opcao == 5:
            exibir_medias(alunos)

        elif opcao == 0:
            print("Programa encerrado!")
            break

        else:
            print("Opção inválida! Escolha uma opção do menu.")


if __name__ == "__main__":
    main()