# servico_produtos.py
from flask import Flask, jsonify, request

app = Flask(__name__)
produtos = {}

@app.route("/produto", methods=["POST"])
def adicionar_produto():
    dados = request.json
    nome = dados["nome"]
    quantidade = dados["quantidade"]
    preco = dados["preco"]
    if nome in produtos:
        return jsonify({"erro": "Produto já existe"}), 400
    produtos[nome] = {"quantidade": quantidade, "preco": preco}
    return jsonify({"mensagem": "Produto adicionado"}), 201

@app.route("/produto", methods=["GET"])
def listar_produtos():
    return jsonify(produtos), 200

@app.route("/produto/<nome>", methods=["GET"])
def buscar_produto(nome):
    produto = produtos.get(nome)
    if produto:
        return jsonify(produto), 200
    return jsonify({"erro": "Produto não encontrado"}), 404

if __name__ == "__main__":
    app.run(port=5001)
