# tupla é bem parecida com listas, porém, com algumas particularidades
# não podemos alterar o conteúdo da tupla (imutável)
# operações não disponpiveis em tuplas: .sort(), .append()
# .reverse(), .pop()...

cars = ("SW4", "Hillux", "Corolla")
cars2 = ("Polo", "Virtus", "Amarok")

garagem = cars + cars2

for car in garagem:
    print("Carro disponível:", car)
    
    