# a) Pessoa
class Pessoa:

    def __init__(self, nome, genero, idade):
        self.nome = nome
        self.genero = genero
        self.idade = idade
    
    def __str__(self):
        return self.nome + ' ' + self.genero + ' ' + self.idade

savio = Pessoa('Sávio','Masculino', '21')
print(savio)

# b) Calculadora Simples
class CalculadoraSimples:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def somar(self):
        return self.a + self.b
    
    def subtrair(self):
        return self.a - self.b
    
    def multiplicar(self):
        return self.a * self.b

    def dividir(self):
        return self.a / self.b

valores = CalculadoraSimples(12,8)
print(valores.somar())
print(valores.subtrair())
print(valores.multiplicar())
print(valores.dividir())

# c) Calculadora
class Calculadora:

    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        return a / b

# d) Pedido
#???