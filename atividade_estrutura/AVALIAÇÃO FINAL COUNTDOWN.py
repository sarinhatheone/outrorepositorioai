livros = []
alunos = []


def cadastrar_livro():

    codigo = input("Código do livro: ")

    if codigo == "":
        print("Adicione o código")
        return

    codigo = int(codigo)

    titulo = input("Título do livro: ")

    if titulo == "":
        print("O título não pode ficar vazio")
        return

    autor = input("Autor: ")

    if autor == "":
        print("O autor não pode ficar vazio")
        return

    ano = int(input("Ano: "))

    if ano <= 0:
        print("Ano inválido")
        return

    quantidade = int(input("Quantidade: "))

    if quantidade <= 0:
        print("A quantidade deve ser maior que zero")
        return

    livros.append([codigo, titulo, autor, ano, quantidade])

    print("Livro cadastrado com sucesso!")


def cadastrar_livros():

    print("================================")
    print("Você escolheu cadastrar livros")

    quanti_livros = int(input("Quantos livros deseja cadastrar? "))

    for a in range(quanti_livros):

        print(f"\n----- LIVRO {a + 1} -----")

        cadastrar_livro()


def cadastrar_alunos():

    print("================================")
    print("Você escolheu cadastrar alunos")

    aluno_quanti = int(input("Quantos alunos deseja cadastrar? "))

    for a in range(aluno_quanti):

        print(f"\n----- ALUNO {a + 1} -----")

        matricula = input("Matrícula: ")
        nome = input("Nome do aluno: ")
        turma = input("Turma: ")

        alunos.append([matricula, nome, turma])

        print("Aluno cadastrado com sucesso!")


def realizar_emprestimo():

    print("================================")
    print("Você escolheu realizar empréstimo")

    codigo = int(input("Digite o código do livro: "))
    matricula = input("Digite a matrícula do aluno: ")
    quantidade_emp = int(
        input("Digite a quantidade de livros para o empréstimo: ")
    )

    if quantidade_emp <= 0:
        print("A quantidade deve ser maior que zero")
        return

    # Procurar o livro
    livro_encontrado = None

    for livro in livros:

        if livro[0] == codigo:
            livro_encontrado = livro
            break

    if livro_encontrado is None:
        print("Livro não encontrado!")
        return

    # Procurar o aluno
    aluno_encontrado = None

    for aluno in alunos:

        if aluno[0] == matricula:
            aluno_encontrado = aluno
            break

    if aluno_encontrado is None:
        print("Aluno não encontrado!")
        return

    # Verificar quantidade disponível
    if quantidade_emp > livro_encontrado[4]:
        print("Quantidade de livros insuficiente!")
        return

    # Diminuir a quantidade disponível
    livro_encontrado[4] -= quantidade_emp

    print("\n================================")
    print("Empréstimo realizado com sucesso!")
    print(f"Livro: {livro_encontrado[1]}")
    print(f"Aluno: {aluno_encontrado[1]}")
    print(f"Quantidade emprestada: {quantidade_emp}")
    print(f"Quantidade restante: {livro_encontrado[4]}")


def mostrar_alunos():

    print("\n------ ALUNOS CADASTRADOS ------")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    for aluno in alunos:

        print(f"Matrícula: {aluno[0]}")
        print(f"Nome: {aluno[1]}")
        print(f"Turma: {aluno[2]}")
        print("-----------------------------")


def mostrar_livros():

    print("\n------ LIVROS CADASTRADOS ------")

    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
        return

    for livro in livros:

        print(f"Código: {livro[0]}")
        print(f"Título: {livro[1]}")
        print(f"Autor: {livro[2]}")
        print(f"Ano: {livro[3]}")
        print(f"Quantidade: {livro[4]}")
        print("-----------------------------")


# PROGRAMA PRINCIPAL

while True:

    print("\n=================================")
    print("       BIBLIOTECA VIRTUAL")
    print("=================================")
    print("1 - Cadastrar Livros")
    print("2 - Cadastrar Alunos")
    print("3 - Realizar Empréstimo")
    print("4 - Sair")
    print("5 - Mostrar alunos cadastrados")
    print("6 - Mostrar livros cadastrados")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        cadastrar_livros()

    elif opcao == "2":

        cadastrar_alunos()

    elif opcao == "3":

        realizar_emprestimo()

    elif opcao == "4":

        print("Saindo do sistema...")
        break

    elif opcao == "5":

        mostrar_alunos()

    elif opcao == "6":

        mostrar_livros()

    else:

        print("Opção inválida!")