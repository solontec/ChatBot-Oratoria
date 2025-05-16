import google.generativeai as genai
import os
import sqlite3
from dotenv import load_dotenv



# ... outras funções ...

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("API KEY da Gemini não encontrada. Verifique o arquivo .env.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("models/gemini-1.5-flash")

chat = model.start_chat(history=[
    {
        "role": "user",
        "parts": ["Você é um cara legal que vai conversar sobre oratória, apresentações e ajudar os alunos, e não vai comentar sobre sexo, drogas, agressão, qualquer coisa ruim você não pode responder pois é um sistema educacional!"]
    }
])

temas_permitidos = ["oratória", "apresentação", "falar em público", "comunicação"]
palavras_proibidas = ["violência", "política", "arma", "sexo", "drogas"]

def pergunta_permitida(texto):
    return True

def resposta_segura(texto):
    return not any(p in texto.lower() for p in palavras_proibidas)

def gerar_resposta(pergunta):
    if pergunta_permitida(pergunta) and resposta_segura(pergunta):
        try:
            resposta = chat.send_message(pergunta)
            return resposta.text
        except Exception as e:
            return f"❌ Erro ao gerar resposta: {e}"
    else:
        return "❌ Desculpe, só posso responder perguntas relacionadas à oratória e apresentações."

