# coleções não ordenadas de valores únicos
# não é possível modificar, mas, é possível adicionar

smartphones = {"iphone", "samsung", "xiaomi", "morotola", "nokia"}

print("iphone" in smartphones)

# for cel in smartphones:
#     print(cel.upper())

smartphones_2 = ["iphone", "samsung", "xiaomi", "morotola", "xiaomi"]

print(smartphones_2)

smart_set = set(smartphones_2)

print(smart_set)

listaDeFrutas = {"Uva", "Banana", "Manga", "Cajú", "Pinha"}
frutas = {"Banana", "Uva", "Laranja"}

print(listaDeFrutas.union(frutas))  # unir dois arrays
#       ou listaDeFrutas | frutas

print(listaDeFrutas & frutas)  # compara e retorna resultados iguais
#       ou listaDeFrutasx.intersection(frutas)

print(listaDeFrutas.symmetric_difference(frutas))  # é a diferença entre os conjuntos
#       ou  listaDeFrutas ^ frutas

listaDeFrutas.add("Cajamanga") # adicionar

listaDeFrutas.remove("Cajú")

print(listaDeFrutas)
