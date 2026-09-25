livros = []

while True:

    print("\n===== BIBLIOTECA =====")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Pesquisar livro")
    print("4 - Excluir livro")
    print("5 - Sair")
    print("6 - Mostrar quantidade de livros",)

    opcao = input("Digite uma opção: ")

    if opcao == "1":

        titulo = input("Digite o título: ")
        autor = input("Digite o autor: ")
        

        livros.append([titulo, autor])

        print("Livro cadastrado!")

    elif opcao == "2":

        print("\n--- LIVROS CADASTRADOS ---")

        for contador in livros:
            print("Título:", contador[0])
            print("Autor:", contador[1])
           

    elif opcao == "3":

        pesquisa = input("Digite o título que deseja pesquisar: ")

        encontrado = False

        for contador in livros:
            if contador[0] == pesquisa:
                print("Livro encontrado!")
                print("Título:", contador[0])
                print("Autor:", contador[1])
                encontrado = True
        
        if  not encontrado:
            print("Livro não encontrado")
    #coloquei o not para se o livro não fosse encontrado desse isso dai que o senhor sabe o que é professor
    

    elif opcao == "4":

        pesquisa = input("Digite o título que deseja excluir: ")
        sem_retorno = False

        for contador in livros:
            if contador[0] == pesquisa:
                livros.remove(contador)
                print("Livro excluído!")
                sem_retorno = True

        if not sem_retorno:
            print("Nenhum livro correspondente")
    #a fórmula deu certo enyão eu vou repetir simbora

    elif opcao == "5":

        print("Programa encerrado.")
        break

    elif opcao == "6":
         print("Quantidade de livros", len(livros))

        



    else:

        print("Opção inválida!")