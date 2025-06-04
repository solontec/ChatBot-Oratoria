from flask import Blueprint, render_template, request
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    # PRIMEIRO, VERIFICAMOS SE É UMA REQUISIÇÃO POST (ENVIO DO FORMULÁRIO)
    if request.method == "POST":
        email = request.form["email"]
        rm = request.form ["rm"]
        senha = request.form ["senha"]

        # Realiza a verificação das credenciais
        if(email == "dudu2@gmail.com" and senha == "10" and rm == "23078"):
            # Se as credenciais estiverem corretas, renderiza a página do chatbot
            return render_template('chatbot.html') 
        else:
            # Se as credenciais estiverem incorretas, renderiza a página de login com a mensagem de erro
            return render_template("PaginaLogin.html", error="Usuário ou senha incorretos")
    
    # SE NÃO FOR UMA REQUISIÇÃO POST (ou seja, geralmente GET, para o acesso inicial à página)
    # ENTÃO, renderiza a página de login para o usuário preencher o formulário
    return render_template('PaginaLogin.html')
    
    
    
    
    
    
    


