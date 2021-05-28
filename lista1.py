# Strings
# Exercício 1
A = "Um elefante incomoda muita gente"
print(A)

# Exercício 2
frase = input("Frase:")
frase = frase.strip()
frase = frase.upper()
print(frase)

# Números
# Exercício 1
x = float(input("Valor de x: "))
y = float(input("Valor de y: "))
z = (x**2+y**2)/(x-y)**2
print(z)

# Exercício 2
salario = float(input("Valor do salário: "))
reajuste = salario*1.35
print("O salário reajustado é: %.2f" %reajuste)

# Listas
# Exercício 1
L = [5, 7, 2, 9, 4, 1, 3]
print("Tamanho da lista: ",len(L))
print("Maior valor da lista: ",max(L))
print("Menor valor da lista: ",min(L))
print("Soma de todos os elementos da lista: ",sum(L))
L.sort()
print("Lista em ordem crescente: ",L)
L.reverse()
print("Lista em ordem decrescente: ",L)

# Exercício 2
L = list(range(3, 50, 3))
print(L)

# Dicionário
# Exercício 1
Lanchonete = {
    "Salgado" : 4.50,
    "Lanche" : 6.50,
    "Suco" : 3.00,
    "Refrigerante" : 3.50,
    "Doce" : 1.00
}
print(Lanchonete)

# Exercício 2
Notas = {
    "Aluno 1" : 6,
    "Aluno 2" : 7,
    "Aluno 3" : 8,
    "Aluno 4" : 9,
    "Aluno 5" : 10,
}