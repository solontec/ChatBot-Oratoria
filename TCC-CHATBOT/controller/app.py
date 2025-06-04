from flask import Flask, render_template, request, jsonify # Adicionado jsonify
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from auth_controller import auth_bp 
from model.chat import gerar_resposta 

app = Flask(__name__)
app.register_blueprint(auth_bp) 

@app.route("/")
def index():
    return render_template("PaginaLogin.html")

@app.route("/resposta", methods=["POST"])
def resposta():
    pergunta = request.form["pergunta"]
    resposta_chatbot = gerar_resposta(pergunta) # Alterado nome para evitar conflito
    return render_template("chatbot.html", pergunta=pergunta, resposta=resposta_chatbot) #retorna a resposta


if __name__ == "__main__":
    app.run(debug=True)