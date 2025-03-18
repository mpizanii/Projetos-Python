class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.vendas = []
    
    def adicionar_venda(self, venda):
      if isinstance(venda, Venda):
        self.vendas.append(venda)
    
    def total_vendas(self):
      total = 0
      for venda in self.vendas:
        valor = venda.valor
        total +=  valor
        
      return total

def main():
    categorias = []

    for i in range(2):
        nome_categoria = input("")
        categoria = Categoria(nome_categoria)

        for j in range(2): 
            entrada_venda = input("")
            produto, quantidade, valor = entrada_venda.split(',')
            quantidade = int(quantidade.strip())
            valor = float(valor.strip())

            venda = Venda(produto.strip(), quantidade, valor)
            categoria.adicionar_venda(venda)

        categorias.append(categoria)
    
    for categoria in categorias:
        total = categoria.total_vendas()
        print(f"Venda em {categoria.nome}: {total}")

if __name__ == "__main__":
    main()