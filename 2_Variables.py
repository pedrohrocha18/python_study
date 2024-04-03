media = 0
n1 = n2 = n3 = n4 = 0.0
(
    nome,
    idade,
) = (
    "Pedro",
    29,
)
estado = True


# função type() retorna o tipo do dado

print(type(media))
print(type(n2))
print(type(nome))
print(type(estado))
print(type(1 + 2j))

# função isinstance() retorna verdadeiro ou falso de acordo com tipo passado

a = 10
b = "sol"

# print(isinstance(a, int)) # true
# print(isinstance(b, bool)) #false
print(isinstance(b, (int, bool)))  # false false


# 57:34