biblioteca=[]
while True:

    print("\n===== BIBLIOTECA =====")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Pesquisar livro")
    print("4 - Excluir livro")
    print("5 - Sair")

    opcao = input("Digite uma opção: ")

    if opcao == "1":

        titulo = input("Digite o título: ")
        autor = input("Digite o autor: ")

        livros.append([titulo, autor])
        biblioteca.append(livros)
        print("Livro cadastrado!")

    elif opcao == "2":

        print("\n--- LIVROS CADASTRADOS ---")

        for l in livros:
            print("Título:", l[0])
            print("Autor:", l[1])

    elif opcao == "3":

        pesquisa = input("Digite o título que deseja pesquisar: ")
        if pesquisa == "":
            print("Não se pode deixar vazio")

        else:
            encontrado = False
            for livro in biblioteca:
                if l[0] == pesquisa:
                    print("Livro encontrado!")
                    print("Título:", l[0])
                    print("Autor:", l[1])

                encontrado = True
        

        

    elif opcao == "4":

        pesquisa = input("Digite o título que deseja excluir: ")

        for contador in livros:
            if contador[0] == pesquisa:
                livros.remove(contador)
                print("Livro excluído!")

    elif opcao == "5":

        print("Programa encerrado.")
        break

    else:

        print("Opção inválida!")