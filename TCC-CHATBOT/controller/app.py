from flask import Flask, render_template, request
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.chat import gerar_resposta  # nome certo da função

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/resposta", methods=["POST"])
def resposta():
    pergunta = request.form["pergunta"]
    resposta = gerar_resposta(pergunta)  # usa o nome certo aqui também
    return render_template("index.html", pergunta=pergunta, resposta=resposta)

if __name__ == "__main__":
    app.run(debug=True)