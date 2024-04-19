import random

print("Gerar 5 números aleatórios entre 1 e 10:\n")
for i in range(5):
    num = random.randint(1, 11)
    print("Numero gerado:", num)

####
valor1 = random.random()
print("Valor 1:", round(valor1 * 10, 2))

####
valor2 = random.uniform(1, 25)
print("Valor 2:", round(valor2, 2))

####################
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
n = random.choice(numbers)
print("Drawn Number:", n)

####################
s = random.sample(numbers, 2)
print(s)
####################
print("Lista original", numbers)

print("Embaralhar a lista e exibi-la:")

ne = random.shuffle(numbers)

print(numbers)

#3:25:20