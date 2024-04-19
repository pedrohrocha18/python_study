# é um laço que está dentro de outro laço

for count in range(1,6):
    print('\nRodada:', count)
    for count2 in range (5, 0, -1 ):
        print("valor:", count2)

print("Fim dos laços")