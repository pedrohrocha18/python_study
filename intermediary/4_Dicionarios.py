# permite armazenar dados em PARES, chaves e valor
# são similares aos arrays


carro = {"brand": "volkswagem", "model": "nivus", "year": 2024, "0km": True}

# print("marca:", carro["brand"], "modelo:", carro["model"])

# atualiza uma entrada (precisa existir dentro do array, senão ele vai criar um novo elemento)

# carro["brand"] = "Toyota"
# carro["model"] = "Vovorolla"
# saída: {'brand': 'Toyota', 'model': 'Vovorolla', 'year': 2024, '0km': True}


# adicionar uma entrada (não pode existir no array, se não ele atualiza)

# carro["type"] = "SUV"
# saída: {'brand': 'volkswagem', 'model': 'nivus', 'year': 2024, '0km': True, 'type': 'SUV'}


# exclusão de item
# del carro["brand"]

# apagar todos os dados
# carro.clear()

# retorna dict_items (itens)
# print(carro.items())
# saída: dict_items([('brand', 'volkswagem'), ('model', 'nivus'), ('year', 2024), ('0km', True)])

# retorna as chaves dos elementos
# print(carro.keys())
# saída: dict_keys(['brand', 'model', 'year', '0km'])

# retorna os values
# print(carro.values())
# saída: dict_values(['volkswagem', 'nivus', 2024, True])

for x, y in carro.items():
    print(x, ":", y)
