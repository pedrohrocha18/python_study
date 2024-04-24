notas_primeiro_semestre = [2.4, 5.9, 8.0, 10, 12]
notas_segundo_semestre = [5, 8.9, 5.5, 6, 7]

lista = notas_primeiro_semestre + notas_segundo_semestre

#append acrescenta um valor no final do array
lista.append(9000)

#pop remove o último elemento do array
#passando o parâmetro ele remove o elemento da posição passada
lista.pop(3)

#insert insere o valor na posição escolhida
#posição / valor
lista.insert(0, 999)

#in mostra se possui o determinado valor dentro do array
print(10002 in lista)
