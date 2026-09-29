def mostrar_menu():
   print("1 - Cadastrar livro")
   print("2 - Listar livros")
   print("0 - Sair")
mostrar_menu()

def apresentar_livro(titulo, autor):
   print("Título:", titulo)
   print("Autor:", autor)
apresentar_livro("Dom Casmurro", "Machado de Assis")

def calcular_total(preco, quantidade):
   return preco * quantidade
valor = calcular_total(25, 3)
print(valor)