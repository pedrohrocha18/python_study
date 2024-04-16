# Exceção é um objeto que representa um erro que ocorreu ao executar o programa
# tratamento de erros
# try except

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

try:
    r = round(n1 / n2, 2)
except ZeroDivisionError:
    print("Não é possível dividir por zero!")
else:
    print("Resultado", r)