# controller/auth_controller.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from model.usuario_model import cadastrar_usuario # Import from the correct location

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        email = request.form.get('email') # Use .get() for safer access
        senha = request.form.get('senha')
        rm = request.form.get('rm')

        # Add basic input validation here before calling DB function
        if not email or not senha or not rm:
            flash('Por favor, preencha todos os campos.', 'error')
            return render_template('PaginaCadastro.html')

        sucesso = cadastrar_usuario(email, rm, senha) # Pass the variables

        if sucesso:
            flash('Cadastro realizado com sucesso! Faça login.', 'success')
            return redirect(url_for('auth.login')) # Redirect to the login route in this blueprint
        else:
            flash('Erro ao cadastrar usuário. O RM ou e-mail pode já estar em uso.', 'error')
            return render_template('PaginaCadastro.html')

    # For GET request or if POST fails
    return render_template('PaginaCadastro.html')

@auth_bp.route('/login', methods=['GET', 'POST']) # <--- CRUCIAL: Added route decorator
def login():
    # In a real app, you'd handle login form submission here (POST)
    # For now, it just renders the login page.
    if request.method == 'POST':
        # Process login logic
        pass # Placeholder for login logic

    return render_template('PaginaLogin/PaginaLogin.html') # Render your actual login page