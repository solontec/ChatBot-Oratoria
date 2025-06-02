from flask import Flask, render_template, request
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#todas as importações necessárias

from model.chat import gerar_resposta  # nome certo da função

app = Flask(__name__) 

@app.route("/")
def index():
    return render_template("chatbot.html") #realiza a funçao de acessar o template HTML
# A função index() renderiza o template HTML inicial
# e retorna a página inicial do chatbot.

@app.route("/resposta", methods=["POST"]) #realiza a funçao de acessar o template HTML
def resposta():
    pergunta = request.form["pergunta"] # pega a pergunta do formulário
    resposta = gerar_resposta(pergunta)  # usa o nome certo aqui também
    return render_template("chatbot.html", pergunta=pergunta, resposta=resposta) #retorna a resposta

if __name__ == "__main__":  #executa o app
    app.run(debug=True) 