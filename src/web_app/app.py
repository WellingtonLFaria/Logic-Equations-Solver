from solver import *
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

expressoes = []

@app.route("/", methods=['GET', 'POST'])
def index():
    global expressoes
    if request.method == 'POST':
        botao = int(request.form['botao'])
        if botao == 0:
            expressao = request.form['expressoes']
            expressoes.append(expressao)
        elif botao == 2:
            try:
                indice = int(request.form['indice'])
                expressoes.pop(indice)
            except:
                return "Índice inválido"
        else:
            tamanho = int(request.form['tamanho'])
            valores_corretos = encontrar_valores_corretos(expressoes, tamanho)
            return jsonify(valores_corretos)
    return render_template('calculadora.html', expressoes=expressoes)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)