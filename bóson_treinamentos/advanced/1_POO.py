# Orientação a objetos: paradigma de programação (estilo)
# Classes = modelos que vão representar itens do mundo real dentro do software
# Objetos = ocorrências dessas classes, são as classes carregadas na memória

# atributos(variáveis) e métodos(ações,funções)

class Veiculo:
    def movimentar(self):
        print("Sou um veículo e me desloco!")
    
    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__num_registro = None
        
if __name__ == "__main__":
    my_car = Veiculo("Volkswagem", "Nivus")
    my_car.movimentar()
    print(my_car.fabricante)
    print(my_car.modelo)