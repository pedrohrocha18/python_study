# Orientação a objetos: paradigma de programação (estilo)
# Classes = modelos que vão representar itens do mundo real dentro do software
# Objetos = ocorrências dessas classes, são as classes carregadas na memória

# atributos(variáveis, propriedades da class) e métodos(funcionalidades, ações)


class Veiculo:
    def movimentar(self):
        print("Sou um veículo e me desloco.")

    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__num_registro = None

    # Setter
    def set_num_registro(self, registro):
        self.__num_registro = registro

    # Getter
    def get_fab_modelo(self):
        print("Modelo:", self.__modelo, " / Fabricante:", self.__fabricante)

    def get_num_registro(self):
        print("Registro:", self.__num_registro)


class Carro(Veiculo):
    def movimentar(self):
        print("Sou um carro turbinado.")


class Moto(Veiculo):
    def movimentar(self):
        print("Sou uma moto!")


class Aviao(Veiculo):
    def movimentar(self):
        print("Sou um avião!")

    def __init__(self, fabricante, modelo, categoria):
        self.__cat = categoria
        super().__init__(fabricante, modelo)

    def get_categoria(self):
        print("Categoria:", self.__cat)


if __name__ == "__main__":
    # meu_carro = Veiculo("Volkswagem", "Nivus")
    # meu_carro.movimentar()
    # meu_carro.get_fab_modelo()
    # meu_carro.set_num_registro(9781518)
    # meu_carro.get_num_registro()

    # meu_outro_carro = Carro("Volkswagem", "Jetta")
    # meu_outro_carro.movimentar()
    # meu_outro_carro.get_fab_modelo()

    # seu_carro = Carro("Audi", "A4")
    # seu_carro.movimentar()
    # seu_carro.get_fab_modelo()

    # sua_moto = Moto("Kawasaki", "ZX10")
    # sua_moto.movimentar()
    # sua_moto.get_fab_modelo()

    seu_aviao = Aviao("Boeing", "747", "Comercial")
    seu_aviao.movimentar()
    seu_aviao.get_fab_modelo()
    seu_aviao.get_categoria()
