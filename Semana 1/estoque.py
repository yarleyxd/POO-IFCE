# Questão 1 - Estoque de Produtos

def exibir_menu():
    print("===== ESTOQUE DA LOJA =====")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Atualizar quantidade")
    print("4 - Exibir estoque")
    print("0 - Sair")


def ler_texto(mensagem):
    while True:
        texto = input(mensagem).strip().title()

        if texto:
            return texto

        print("O nome não pode ficar vazio!")


def ler_quantidade(mensagem):
    while True:
        try:
            quantidade = int(input(mensagem))

            if quantidade >= 0:
                return quantidade

            print("A quantidade não pode ser negativa!")

        except ValueError:
            print("Digite um número inteiro válido!")


def adicionar_produto(estoque, nome, quantidade):
    if nome in estoque:
        print("Produto já cadastrado! Utilize a opção de atualizar.")
    else:
        estoque[nome] = quantidade
        print("Produto adicionado com sucesso!")


def remover_produto(estoque, nome):
    if nome in estoque:
        del estoque[nome]
        print("Produto removido com sucesso!")
    else:
        print("Produto não encontrado!")


def atualizar_quantidade(estoque, nome, quantidade):
    if nome in estoque:
        estoque[nome] = quantidade
        print("Quantidade atualizada com sucesso!")
    else:
        print("Produto não encontrado!")


def exibir_estoque(estoque):
    if not estoque:
        print("Estoque vazio")
    else:
        print("===== PRODUTOS EM ESTOQUE =====")

        for nome, quantidade in estoque.items():
            print(f"Produto: {nome} | Quantidade: {quantidade}")


def main():
    estoque = {}

    while True:
        exibir_menu()

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida! Digite um número.")
            continue

        if opcao == 1:
            nome = ler_texto("Nome do produto: ")
            quantidade = ler_quantidade("Quantidade: ")
            adicionar_produto(estoque, nome, quantidade)

        elif opcao == 2:
            nome = ler_texto("Nome do produto que deseja remover: ")
            remover_produto(estoque, nome)

        elif opcao == 3:
            nome = ler_texto("Nome do produto que deseja atualizar: ")
            quantidade = ler_quantidade("Nova quantidade: ")
            atualizar_quantidade(estoque, nome, quantidade)

        elif opcao == 4:
            exibir_estoque(estoque)

        elif opcao == 0:
            print("Programa encerrado!")
            break

        else:
            print("Opção inválida! Escolha uma opção do menu.")


if __name__ == "__main__":
    main()