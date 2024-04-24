bandas = []

print("Digite o nome de 5 bandas favoritas.")

for banda in range(5):
    print("Banda:")
    bandas.append(input())
bandas.sort()

print("Bandas escolhidas:")

for banda in bandas:
    print("-", banda)
    
    
# 3:46:31