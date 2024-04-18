# Função Filter
# filtra elementos de uma sequência
# filter(função, sequência)

# Exemplo 01

# def numeros_pares(n):
#     return n % 2 == 0

# listNumbers = [2, 3, 4, 5, 10, 12, 15, 17, 19, 22, 28]

# num_par = list(filter(numeros_pares, listNumbers))

# print(num_par)


# Exemplo 02

listNumbers = [2, 3, 4, 5, 10, 12, 15, 17, 19, 22, 28]

num_impar = list(filter(lambda x: x % 2 != 0, listNumbers))

print(num_impar)
