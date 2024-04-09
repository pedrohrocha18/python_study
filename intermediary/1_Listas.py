# Lista é uma sequência de valores armazenados na memória

minhas_notas_primeiro_semestre = [2.4, 5.9, 8.0, 10, 12]
minhas_notas_segundo_semestre = [5, 8.9, 5.5, 6, 7]

lista = minhas_notas_primeiro_semestre + minhas_notas_segundo_semestre

# length
print("Len:", len(lista))

# sem reverse ordem crescente  /// reverse ordem decrescente
print("Sorted:", sorted(lista, reverse=True))

# somar os elementos do array
print("Sum", sum(lista))

# min(vlr min) e max (vlr max)
print("Valor min", min(lista))
print("Valor max", max(lista))
