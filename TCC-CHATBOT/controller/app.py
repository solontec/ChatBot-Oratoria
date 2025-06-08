# controller/app.py
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
import sys
import os

# Add the project root to sys.path
# This helps Python find 'model' and 'controller' as top-level packages
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import from the correct locations
from model.chat import gerar_resposta
from controller.auth_controller import auth_bp # Import blueprint from its location

app = Flask(__name__)
app.config['SECRET_KEY'] = 'uma_chave_secreta_muito_longa_e_aleatoria_para_producao_1234567890' # CHANGE THIS!
app.register_blueprint(auth_bp)

@app.route("/")
def index():
    # You might want this to be your login page or a general landing page
    return render_template("chatbot/chatbot.html")

@app.route("/resposta", methods=["POST"])
def resposta():
    pergunta = request.form["pergunta"]
    resposta_chatbot = gerar_resposta(pergunta)
    return render_template("chatbot/chatbot.html" , pergunta=pergunta, resposta=resposta_chatbot)



if __name__ == "__main__":
    app.run(debug=True)