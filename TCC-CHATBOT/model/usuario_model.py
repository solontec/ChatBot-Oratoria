import sqlite3
import bcrypt

# neste arquivo é realizado a conexão com o banco de dados e as funções de cadastro e login do usuário

#realizado por SQLlite3, que é um banco leve e local, com bycript para hash na senha

def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

# na linha acima a conexao do banco é realizada, puxando o database.db que vai conter as informações do usuário

def setup_database():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                rm INTEGER UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                senha BLOB NOT NULL
            )
        ''')
        
        # Cria a tabela de usuários acima, lembrando que é LOCAL e não precisa de servidor, o banco é leve e rápido
        conn.commit()
        
        

def cadastrar_usuario(email, rm,  password): # Função para cadastrar um usuário no banco de dados
    rm = rm.strip()  # Remove espaços em branco no início e no final independente do que for digitado
    
    
    
    if not rm or not email or not password: # verifica se os campos foram todos
        return False # se algum campo estiver vazio, retorna falso e vai dar um erro
    
    
    
    try: # caso dê certinho ele faz a verificação da senha em bycript e insere no banco de dados em hash
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())  # Gera o hash da senha usando bcrypt 
        with get_db_connection() as conn:
            conn.execute("INSERT INTO usuarios (rm, email, senha) VALUES (?, ?, ?)", (rm, email, hashed)) # Insere o novo usuário no banco de dados rm email e senha criptgrafada
        return True # retorna True se o cadastro for sucesso
    
    except sqlite3.IntegrityError: #caso nao de certo para dar o insert no banco ele da um erro !
        return False 
    
    
    
def login_check(rm, email, password): # Função para verificar se o usuário existe e a senha está correta
    
    with get_db_connection() as conn: # Abre a conexão com o banco de dados novamente 
        user = conn.execute("SELECT id, senha FROM usuarios WHERE rm = ? AND email = ?", (rm, email)).fetchone() # Busca o usuário pelo RM e email  retornando o ID e a senha criptografada
        
        
    if user and bcrypt.checkpw(password.encode(), user['senha']):   # Verifica se o usuário foi encontrado e se a senha fornecida corresponde ao hash armazenado, que foi criado na função cadastrar_usuario
        # Se a senha estiver correta, retorna o ID do usuário 
        
        
        return user['id'] 
    return None
