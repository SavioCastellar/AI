# a
nums = [i for i in range(1,1001) if i % 8 == 0]
print(nums)

# b
#nums = [i for i in range(1,1001) if '6']
#print(nums)

# c
sentence = "Practice Problems to Drill List Comprehension in Your Head."
print("O número de espaços é: ",sentence.count(" "))

# d
sentence = "Practice Problems to Drill List Comprehension in Your Head."
sentence = sentence.replace("a","")
sentence = sentence.replace("e","")
sentence = sentence.replace("i","")
sentence = sentence.replace("o","")
sentence = sentence.replace("u","")
print(sentence)

# e
sentence = "Practice Problems to Drill List Comprehension in Your Head."
separado = sentence.split()
lista = []
i = 0
if len(separado[i]) < 5:
    lista.append(separado[i])
    i += 1
print(lista)  