import sys
import os
from flask import Flask, session

#importações para realizar o sistema de autenticação e o chatbot


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Adiciona o diretório pai ao sys.path para importar módulos corretamente

from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from model.usuario_model import setup_database
from model.chat import gerar_resposta
from controller.auth_controller import auth_bp

# acima as importações são feitas para importar os módulos necessários para o funcionamento do chatbot e autenticação


app = Flask(__name__) # Cria uma instância do Flask, que é o aplicativo web
# Configurações do aplicativo Flask abaixo:


app.config['SECRET_KEY'] = 'uma_chave_secreta_muito_longa_e_aleatoria_para_producao_1234567890' # Define uma chave secreta para o aplicativo Flask, que é usada para proteger sessões e cookies
app.register_blueprint(auth_bp) # Registra o blueprint de autenticação, que contém as rotas de cadastro e login

# ✅ Chamar a criação do banco/tabela
setup_database()   # Chama a função setup_database do model.usuario_model para configurar o banco de dados e criar as tabelas necessárias

@app.route("/") # define a rota raiz do sistema 
def index():
    return render_template("chatbot/chatbot.html") # retorna a page do login, que é login.html

@app.route("/resposta", methods=["POST"]) # Define a rota para receber a pergunta do usuario e gerar a resposta do chatbot, porem no mesmo template, a rota muda mas retorna o mesmo html
def resposta():
    pergunta = request.form["pergunta"] # Pega a pergunta enviada pelo usuário através do formulário
    resposta_chatbot = gerar_resposta(pergunta) # Chama a função gerar_resposta do model.chat para obter a resposta do chatbot com base na pergunta do usuário
    return render_template("chatbot/chatbot.html" , pergunta=pergunta, resposta=resposta_chatbot) #



if __name__ == "__main__": #fecha o script e ve se ta tudo ok
    app.run(debug=True)
