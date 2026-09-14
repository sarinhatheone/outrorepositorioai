print("\n================================= \n BIBLIOTECA VIRTUAL \n=================================")
print("1 - Cadastrar Livros \n2 - Cadastrar Alunos \n3 - Realizar Empréstimo \n4 - Sair")

opcao = input("Escolha uma opção: ")

if opcao == "1":
    print("================================\nVocê escolheu cadastrar livros")

    quanti_livros = int(input("Quantos livros deseja cadastrar? "))

    for q in range(quanti_livros):
        print(f"\n----- LIVRO {q + 1} -----")

        codigo = int(input("Código: "))

        titulo = input("Título: ")
        if titulo == "":
            print("O título não pode ficar vazio")

        autor = input("Autor: ")
        if autor == "":
            print("O autor não pode ficar vazio")

        ano = int(input("Ano: "))
        if ano <= 0:
            print("Ano inválido")     

        quantidade = int(input("Quantidade: "))
        if quantidade <= 0:
            print("A quantidade deve ser maior que zero")   

        print("Livro cadastrado com sucesso!")

elif opcao == "2":
    print("================================\nVocê escolheu Cadastrar Alunos")
    aluno_quanti = int(input("Quantos alunos deseja cadastrar? "))

    for aq in range(aluno_quanti):
        print(f"\n----- ALUNO {aq + 1} -----")

        matricula = int(input("Matrícula: "))
        if matricula <= 0:
            print("Matrícula inválida")

        nome = input("Nome do aluno: ")
        if nome == "":
            print("O nome não pode ficar vazio")

        turma = input("Turma: ")
        if turma == "":
            print("A turma não pode ficar vazia")

        print("Aluno cadastrado com sucesso!")


elif opcao == "3":
    print("================================\nVocê escolheu Realizar Empréstimo")
    codigo = int(input("Digite o código do livro: "))
    matricula = int(input("Digite a matrícula do aluno: "))

    quantidade_emp = (int(input("\n================================\nDigite a quantidade de livros para o empréstimo: ")))
    if quantidade_emp <= 0:
        print("\nA quantidade deve ser maior que zero")

    for e in range(quantidade_emp):
        print(f"\n----- EMPRÉSTIMO {e + 1} -----")
        print(f"\nCódigo do livro: {codigo}")
        print(f"Matrícula do aluno: {matricula}")
        print(f"Quantidade de livros disponível: {quantidade_emp}")

        print("\n================================\nEmpréstimo realizado com sucesso!")

    
elif opcao == "4":
    print("\nSaindo do sistema...")
    

else:
    print("Opção inválida!")

   
