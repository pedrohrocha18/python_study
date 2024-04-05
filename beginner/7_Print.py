# nome = input("Digite seu nome:")

# forma 1
brand = "Volkswagem"
model = "Nivus"

print("First example of print:", brand, model)

# forma 2
name = "Pedro"
age = 29

print(
    "Seccond example of print: His name is {0} and he have {1} years old.".format(
        name, age
    )
)

# forma 3
name = "Zezim"
age = "80"

print(f"Meu nome é {name} e eu tenho {age} anos de idade")


# forma 3 exemplo 2
a = 20
b = 30

print(f"A soma de {a} e {b} é: {a + b}")


# forma 3 exemplo 3 :.2f (arredonda as casas decimais) caso dê erro basta usar \ antes do caractere esp

value = 128.78562
print(f"O valor é '{value:.2f}'")

# forma 3 exemplo 4 caractere de escape

nome = "Pedrox"
idade = 29

print(f"Nome: {nome}\tIdade: {idade} ")

# 2:10:43