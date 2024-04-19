# É um bloco de cód que executa uma determinada tarefa
# Podemos utilizar várias vezes dentro do programa
# Até mesmo importar 'modulo' em outros programas
# Modularização "reaproveitamento de código"

# def mensagem():
#     print("Bem-vindo aos estudos de Python")
#     print("Próximo passo é aprender FastAPI")

# mensagem()


def somaNumeros(x, y):
    print("A soma de", x, "e", y, "é igual a:", x + y)


somaNumeros(2, 4)


def mult(x, y):
    return x * y


a = 2
b = 3
c = mult(a, b)

print(a, b, c)
print("Primeiro exemplo--------------------------------------")


def div(j, k):
    if k != 0:
        return j / k
    else:
        return "Impossível dividir por 0"


if __name__ == "__main__":
    a = int(input("Digite um número: "))
    b = int(input("Digite outro número: "))

    r = div(a, b)

    print(r)
    
print("Segundo exemplo--------------------------------------")



def quadrado(val):
    quadrados = []
    for x in val:
        quadrados.append(x**2)
    return quadrados


if __name__ == "__main__":
    valores = [2, 5, 10, 20, 40]
    resultados = quadrado(valores)
    for g in resultados:
        print(g)
        
print("Terceiro exemplo--------------------------------------")



# 5:25:14