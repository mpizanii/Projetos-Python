import time
class Carro(object):
    def __init__(self, marca, modelo, cor = 'Branco', ano = 2023):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
    def get_marca(self):
        return self.marca
    def set_marca(self):
        self.marca = nova_marca
    def get_modelo(self):
        return self.modelo
    def set_modelo(self):
        self.modelo = novo_modelo
    def get_ano(self):
        return self.ano
    def set_ano(self, ano):
        if isinstance(ano, int) and ano >= 1900:
            self.ano = novo_ano
        else:
            print('Ano inválido!')
    def get_cor(self):
        return self.cor
    def set_cor(self):
        self.cor = nova_cor
    def mostra_dados(self):
        print(f'Marca:{self.marca}.\nModelo:{self.modelo}.\nAno:{self.ano}.\nCor:{self.cor}.'.title())
    def retorna_dados(self):
        dados = (f'O carro {self.marca} {self.modelo} {self.cor} de ano {self.ano}')
        return dados
carro1 = Carro ('BMW', 'M2', 'preto', 2020)
carro2 = Carro ('BMW', '320i', 'vermelho')
carro3 = Carro ('Audi', 'A3')
print(carro1.retorna_dados())
print()
carro1.mostra_dados()
print()
print(carro1.marca)
print(carro1.modelo)
print(carro1.cor)
print(carro1.ano)
time.sleep(5)