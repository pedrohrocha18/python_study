from math import sqrt

class NumeroNegativoError(Exception):
    def __init__(self):
        pass

if __name__ == "__main__":
    while True:
        try:
            num = int(input("Digite um número POSITIVO: "))
            if num < 0:
                raise NumeroNegativoError
        except NumeroNegativoError:
            print("Foi digitado um número negativo")
        else:
            print("A raiz quadrada de", num, "é:", sqrt(num))
            break
        
print("Fim do cálculo!")
