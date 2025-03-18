class Pessoa:
    def __init__(self, nome, cidade, idade = 18):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def get_idade(self):
            return self.idade
    def set_idade(self, nova_idade):
        if nova_idade >= 0:
            self.idade = nova_idade
        else:
            print("A idade não pode ser negativa.")
    def get_cidade(self):
        return self.cidade
    def set_cidade(self, nova_cidade):
        self.cidade = nova_cidade
    def fazer_aniversario(self):
        self.idade += 1
    def __str__(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}\nCidade: {self.cidade}"
if __name__ == "__main__":
    pessoa1 = Pessoa("João", "São Paulo", 30)
    pessoa2 = Pessoa("Matheus", "Brasília")
    pessoa3 = Pessoa("Maria", "Londres")
    print("Informações iniciais da pessoa:")
    print(pessoa1)
    print(pessoa2)
    print(pessoa3)
    pessoa1.set_cidade("Rio de Janeiro")
    pessoa1.fazer_aniversario()
    print("\nInformações após as alterações:")
    print(pessoa1)
    pessoa2.set_cidade("Minas gerais")
    pessoa2.fazer_aniversario()
    print(pessoa2)
    pessoa3.fazer_aniversario()
    print(pessoa3)