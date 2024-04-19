carros = ("SW4", "Polo", "Hilux", "Uno", "Corolla", "Civic", "Fusca")

i = 0

for carro in carros:
    i += 1
    if carro == "Civic":
        continue
    print(i, carro)
    for carroDois in carros:
        print("Testando:", carroDois)
