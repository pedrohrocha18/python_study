frase = "Python é bom. Só que JavaScript é melhor! haha"

vogais = ["a", "e", "i", "o", "u", "é", "ó"]


lista_de_vogais = [vo for vo in frase if vo in vogais]

print(len(lista_de_vogais))