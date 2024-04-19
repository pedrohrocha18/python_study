# def div(j, k):
#     if k != 0:
#         return j / k
#     else:
#         print("Não é possível dividir por 0.")


# if __name__ == "__main__":
#     a = int(input("Digite um número: "))
#     b = int(input("Digite outro número: "))

# print("A divisão entre", a, "e", b, "é igual a:", int(div(a, b)))


def quadrado(valores):
    quadrados = []
    for x in valores:
        quadrados.append(x**2)
    return quadrados


if __name__ == "__main__":
    valores = [2, 5, 7, 9, 10, 12]
    resultados = quadrado(valores)
    for ze in resultados:
        print(ze)