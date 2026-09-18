biblioteca = [
    [1, "ablubleble", "Clovis", 1960],
    [2, "jucris", "Santoro", 2030]
]

remove_livro =int(input("Quantos livros você quer apagar?"))
for i in range(1,remove_livro+1):
   codigo_busca = input("Qual o código do livro") 
   for l in remove_livro:
     if l[0] == codigo_busca:
        biblioteca.remove(l)
        print("Livro excluído!")
        break

