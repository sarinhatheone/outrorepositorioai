nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade do aluno: "))
curso = input("Digite o curso: ")
nota = float(input("Digite a nota do aluno: "))

if nota >= 6.0:
    aprovacao = "Aprovado"
else:
    aprovacao = "Reprovado"

print("\n===== CADASTRO DO ALUNO =====")
print("Nome:", nome)
print("Idade:", idade)
print("Curso:", curso)
print("Nota:", nota)
print("Situação:", aprovacao)