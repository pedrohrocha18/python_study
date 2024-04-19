# Funções Lambda 'anônimas'
# funções que não possuem nome, podem ser criadas e usadas no mesmo momento
# lambda argumentos: expressão

# Primeiro exemplo

quadrado = lambda x: x**2

for i in range(1, 11):
    print("O quadrado de", i, "é:", quadrado(i))

# Segundo exemplo

par = lambda y: y % 2 == 0
print(par(3))


# Terceiro exemplo

numbers = lambda h,g: h >= 2 and g >=2

print(numbers(2, 4))