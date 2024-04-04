nome = None

while True:
    print("Digite seu nome ou x para sair do programa: ")
    nome = input()
    if nome == "x" or nome == "X":
        print("Você saiu do programa!")
        break
    print("Seja bem-vindo", nome)
    break
print("Thank you! Bye!")
