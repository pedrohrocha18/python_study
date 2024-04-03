l1 = str(input("Digite uma letra: "))
l2 = str(input("Digite outra letra: "))

x = l1 == l2
print(l1, "e", l2, "são iguais?", x)

x = l1 != l2
print(l1, "e", l2, "são diferentes?", x)

x = l1 > l2
print(l1, "é maior que", l2, "?", x)

x = l1 < l2
print(l1, "é menor que", l2, "?", x)

x = l1 >= l2
print("teste " + str(x))
