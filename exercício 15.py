salario = float(input("Insira o valor do salário:"))
percentual = float(input("Insira o percentual de reajuste:"))

reajuste = (salario * percentual /100)
novo_salario = (salario + reajuste)

print("o valor do reajuste é:", reajuste)
print("O novo salário é:", novo_salario)