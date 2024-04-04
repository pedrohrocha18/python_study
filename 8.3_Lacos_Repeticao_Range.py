# exemplo 01

# for num in range(1,11):
#     print(num)

# ------------------------

# exemplo 02

# name = input("Digite seu nome: ")

# for x in range (1, 11):
#     print(x + 1, name)


# ------------------------

# exemplo 03

# for x in range(100, 0, -10):
#     print(x)

# ------------------------

# exemplo 04

carros = ('SW4', 'Polo', 'Hilux', 'Uno', 'Corolla', 'Civic', 'Fusca')

for carro in carros:
    if carro == 'Corolla': 
        break
    print(carro) 
    

# nesse caso o CONTINUE faz com que o if seja ignorado
# o BREAK faz a parada do laço, não deixa executar o restante.