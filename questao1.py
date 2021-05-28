# Strings
# Exercício 1
A = "Um elefante incomoda muita gente"
print(A)

# Exercício 2
frase = input("Frase:")
frase = frase.replace(" ","")
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
media = (sum(Notas.values()))/(len(Notas.values()))

# Estruturas de Decisão
# Exercício 1
nota1 = float(input("Valor da primeira nota: "))
nota2 = float(input("Valor da segunda nota: "))
media = (nota1+nota2)/2
if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")
print(media)

# Exercício 2
nota1 = float(input("Valor da primeira nota: "))
nota2 = float(input("Valor da segunda nota: "))
media = (nota1+nota2)/2
if media >= 6:
    print("Aprovado")
elif media >= 4 and media < 6:
    print("Exame")
else:
    print("Reprovado")
print(media)

# Estrutura de repetição
# Exercício 1
s = 0
for i in range (3,333,3):
    s = s + i
print(s)

# Exercício 2
total = 0
for i in range (1,11,1):
    nota = float(input("Valor da nota " + str(i) +": "))
    total = total + nota
print("Média = ",total/10)

# Exercício 3
x = int(input("Número: "))
for i in range (1,11):
    print("%2d x %2d = %3d" %(i,x,i*x))

# Funções
# Exercício 1
def linha(x):
    for i in range(x):
        print(end='_')

# Exercício 2
def lista(L):
    s = 0
    for valor in L:
        s = s + 1
        print(s,'-',valor)

# Exercício 3
def media(L):
    s = 0
    for valor in L:
        s = s + valor
    return s/len(L)