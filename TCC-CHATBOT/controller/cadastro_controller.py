from models.conexao import conectar # Importa a função conectar do módulo conexao com a conexão ao banco de dados

def cadastrar_usuario(email, rm, senha): ## Função para cadastrar um usuário no banco de dados
    conexao = conectar()
    cursor = conexao.cursor()
    
    try: # Tenta executar o bloco de código abaixo e  Verifica se o usuário já existe
        # Verifica se o usuário já existe
        
        
        sql = "INSERT INTO usuarios (email, rm, senha) VALUES (?, ?, ?)" #  consulta sql para inserir um novo usuário
        valores = (email, rm, senha)  # valores a serem inseridos na consulta sql todos armazenados em name e id no html
        cursor.execute(sql, valores)  # executa a consulta sql com os valores enviados
        conexao.commit()  # Confirma a alteração no  no banco de dados
        return True    # Retorna True se o cadastro der tudo correto
    
    except  Exception as e:
        print(f"Erro ao cadastrar usuário: {e}")
        return False # se der erro ele vai retornar falso, caso usuario ja exista ou outro erro no banco de dados
    
    finally: # Fecha a  conexão com o banco de dados
        cursor.close()
        conexao.close()