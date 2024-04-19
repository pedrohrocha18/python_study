# Função Map
# permite aplicar uma outra função a cada elemento
# map(função, objeto)


# num = [1, 2, 3, 4, 5, 6]

# dobro = list(map(lambda y: y * 2, num))

# print(dobro)


names = ["Pedro", "Adrielle", "Amor", "Eterno"]

maiuscula = list(map(str.upper, names))

print(maiuscula)