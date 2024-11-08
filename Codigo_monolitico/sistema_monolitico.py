# sistema_monolitico.py

class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, nome, quantidade, preco):
        if nome in self.produtos:
            print("Produto já existe!")
            return
        self.produtos[nome] = {"quantidade": quantidade, "preco": preco}
        print(f"Produto '{nome}' adicionado.")

    def listar_produtos(self):
        if not self.produtos:
            print("Estoque vazio.")
            return
        for nome, info in self.produtos.items():
            print(f"Nome: {nome}, Quantidade: {info['quantidade']}, Preço: {info['preco']}")

    def buscar_produto(self, nome):
        produto = self.produtos.get(nome)
        if produto:
            print(f"Produto encontrado - Nome: {nome}, Quantidade: {produto['quantidade']}, Preço: {produto['preco']}")
        else:
            print("Produto não encontrado.")

    def atualizar_quantidade(self, nome, nova_quantidade):
        if nome in self.produtos:
            self.produtos[nome]["quantidade"] = nova_quantidade
            print(f"Quantidade do produto '{nome}' atualizada.")
        else:
            print("Produto não encontrado.")

    def remover_produto(self, nome):
        if nome in self.produtos:
            del self.produtos[nome]
            print(f"Produto '{nome}' removido.")
        else:
            print("Produto não encontrado.")

# Exemplo de uso
estoque = Estoque()
estoque.adicionar_produto("Teclado", 10, 50.0)
estoque.listar_produtos()
estoque.buscar_produto("Teclado")
estoque.atualizar_quantidade("Teclado", 15)
estoque.remover_produto("Teclado")
estoque.listar_produtos()
