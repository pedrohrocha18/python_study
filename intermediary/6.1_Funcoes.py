def soma(x, y, z):
    return x + y + z


if __name__ == "__main__":
    a = int(input("Digite um número: "))
    b = int(input("Agora, digite outro número: "))
    c = int(input("Agora.. só mais um número: "))

    print("O resultado da soma entre os números", a, b, c, "é:", int(soma(a, b, c)))
