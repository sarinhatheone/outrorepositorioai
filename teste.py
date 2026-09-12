print("=================================")
print(" A BIBLIOTECA VIRTUAL")
print("=================================")
print("1 - Cadastrar Livros")
print("2 - Cadastrar Alunos")
print("3 - Realizar Empréstimo")
print("4 - Sair")

opcao = input("Escolha uma opção: ")

if opcao == "1":
    print("Você escolheu Cadastrar Livros. \n================================")

if opcao == "1":

    quantidade_livros = int(input("Quantos livros deseja cadastrar? "))

    for i in range(quantidade_livros):

        print(f"\n----- LIVRO {i + 1} -----")

        codigo = int(input("Código: "))

        titulo = input("Título: ")
        if titulo == "":
            print("O título não pode ficar vazio.")
            continue

        autor = input("Autor: ")
        if autor == "":
            print("O autor não pode ficar vazio.")
            continue

        ano = int(input("Ano: "))
        if ano <= 0 or ano > 2026:
            print("Ano inválido.")
            continue

        quantidade = int(input("Quantidade: "))
        if quantidade <= 0:
            print("A quantidade deve ser maior que zero.")
            continue

        print("Livro cadastrado com sucesso!")


elif opcao == "2":
    print("Você escolheu Cadastrar Alunos.")

elif opcao == "3":
    print("Você escolheu Realizar Empréstimo.")

elif opcao == "4":
    print("Saindo do sistema...")

else:
    print("Opção inválida!")
   
