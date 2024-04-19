cars = ("SW4", "Hillux", "Corolla")
cars2 = ("Polo", "Virtus", "Amarok")

comboio = list(cars + cars2)  # transforma a tupla em lista
comboio.append("Strada")
comboio[1] = "Carrim"

print("Agora a tupla virou lista.", comboio)

############################

carsT = ["Polo", "Virtus", "Amarok", "SW4", "Hillux", "Corolla"]

cares = tuple(carsT) # transforma a lista em tupla

print("Agora a lista virou tupla.", sorted(cares))



#4:00:05