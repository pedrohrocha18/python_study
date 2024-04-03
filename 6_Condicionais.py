nota1 = nota2 = 0
media = 0.0

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print("Aprovado. Sua média foi:", media)
    print("Parabéns!")
elif media >= 5:
    print("Recuperação. Sua média foi:", media)
else:
    print("Reprovado. Sua média foi:", media)


# 1:52
