class Veiculo:
    def __init__(self, marca="Desconhecida", modelo="Desconhecido", ano_fabricacao=0):
        self.marca = marca
        self.modelo = modelo
        self.ano_fabricacao = ano_fabricacao

    def get_marca(self):
        return self.marca
    
    def set_marca(self, marca):
        if marca and marca.strip():
            self.marca = marca
        else:
            print("Marca inválida")

    def get_modelo(self):
        return self.modelo
    
    def set_modelo(self, modelo):
        if modelo and modelo.strip():
            self.modelo = modelo
        else:
            print("Modelo inválido")

    def get_ano_fabricacao(self):
        return self.ano_fabricacao
    
    def set_ano_fabricacao(self, ano_fabricacao):
        if 1900 <= ano_fabricacao <= 2023:
            self.ano_fabricacao = ano_fabricacao
        else:
            print("Ano de fabricação inválido")

    def acelerar(self):
        print("O veículo está acelerando")
        
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano_fabricacao, num_portas, ar_condicionado):
        super().__init__(marca, modelo, ano_fabricacao)
        self.num_portas = num_portas
        self.ar_condicionado = ar_condicionado
    def get_num_portas(self):
        return self.num_portas
    def set_num_portas(self, num_portas):
        if 2 <= num_portas <= 5:
            self.num_portas = num_portas
        else:
            print("Número de portas inválido")
    def get_ar_condicionado(self):
        return self.ar_condicionado
    def set_ar_condicionado(self, ar_condicionado):
        self.ar_condicionado = ar_condicionado
class Moto(Veiculo):
    def __init__(self, marca, modelo, ano_fabricacao, tipo):
        super().__init__(marca, modelo, ano_fabricacao)
        self.tipo = tipo
    def get_tipo(self):
        return self.tipo
    def set_tipo(self, tipo):
        self.tipo = tipo
if __name__ == '__main__':
    veiculo = Veiculo("Toyota", "Corolla", 2022)
    veiculo.acelerar()
    carro1 = Carro("Volkswagen", "Gol", 2020, 4, True)
    carro2 = Carro("Ford", "Fiesta", 2019, 5, False)
    moto1 = Moto("Honda", "CBR 600", 2021, "Esportiva")
    moto2 = Moto("Yamaha", "YZF-R3", 2020, "Naked")
    print(f"Carro 1: {carro1.get_marca()} {carro1.get_modelo()}")
    print(f"Moto 2: {moto2.get_marca()} {moto2.get_modelo()} - {moto2.get_tipo()}")
