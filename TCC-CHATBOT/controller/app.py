from flask import Flask, render_template, request
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



from auth_controller import auth_bp  # Blueprint com as rotas de login
from model.chat import gerar_resposta  # Função de resposta do chatbot

app = Flask(__name__)
app.register_blueprint(auth_bp)  # Agora o Blueprint está registrado corretamente

# Rota principal da tela inicia
@app.route("/")
def index():
    return render_template("chatbot.html")

# Rota para processar a pergunta do usuário
@app.route("/resposta", methods=["POST"])
def resposta():
    pergunta = request.form["pergunta"]
    resposta = gerar_resposta(pergunta)


@app.route("/login", methods=["GET", "POST"])

def login():
    if request.method == "POST":
     email = request.form["email"] 
     rm = request.form["rm"]
     senha = request.form["senha"]
     
     
     if email == "admin2@gmail.com" and senha == "22" and rm == "11":
         return render_template("chatbot.html")
    
     else:
         return render_template("PaginaLogin.html", error="Usuário ou senha inválidos")
    

# Executar o app
if __name__ == "__main__":
    app.run(debug=True)
