class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}"

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, nome, telefone, email):
        novo_contato = Contato(nome, telefone, email)
        self.contatos.append(novo_contato)
        print(f"Contato {nome} adicionado com sucesso!")

    def listar_contatos(self):
        if not self.contatos:
            print("Nenhum contato na agenda.")
        else:
            for contato in self.contatos:
                print(contato)

    def procurar_contato(self, nome):
        for contato in self.contatos:
            if contato.nome.lower() == nome.lower():
                print(contato)
                return
        print(f"Contato {nome} não encontrado.")

def menu():
    agenda = Agenda()
    while True:
        print("\n--- Menu ---")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Procurar contato")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            agenda.adicionar_contato(nome, telefone, email)
        elif opcao == '2':
            agenda.listar_contatos()
        elif opcao == '3':
            nome = input("Digite o nome do contato: ")
            agenda.procurar_contato(nome)
        elif opcao == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
