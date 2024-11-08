# servico_estoque.py
from flask import Flask, jsonify, request

app = Flask(__name__)
produtos = {}  # Este dicionário simula o banco de dados compartilhado.

@app.route("/estoque/<nome>", methods=["PUT"])
def atualizar_quantidade(nome):
    if nome not in produtos:
        return jsonify({"erro": "Produto não encontrado"}), 404
    dados = request.json
    produtos[nome]["quantidade"] = dados["quantidade"]
    return jsonify({"mensagem": "Quantidade atualizada"}), 200

@app.route("/estoque/<nome>", methods=["DELETE"])
def remover_produto(nome):
    if nome in produtos:
        del produtos[nome]
        return jsonify({"mensagem": "Produto removido"}), 200
    return jsonify({"erro": "Produto não encontrado"}), 404

if __name__ == "__main__":
    app.run(port=5002)
