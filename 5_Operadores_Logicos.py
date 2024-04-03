# and - as duas condições precisam ser verdadeiras
# or - uma das condições precisam ser verdadeira
# not - transforma a entrada para o inverso ex: false em true


a = 5
b = c = 10
d = 18

#      f          v      =  f
x = a == b and b == c
print("Resultado de 'and' uma condição falsa: ", x)

#      v           v       =  v
y = b == c and a * 2 == b
print("Resultado de 'and' duas condições verdadeiras: ", y)

#      f           v       =  v
r = a == b or c // a == 2
print("Resultado de 'or' uma das condições verdadeira: ", r)

#      f        f        =  f
l = a == b or c == d
print("Resultado de 'or' duas condições falsas: ", l)

#         f     =  v 
m = not a == b
print("Resultado de not sendo condição inversa de false: ", m)

#          v    = f
n = not b == c
print("Resultado de not sendo condição inversa de true: ", n)