

from database.conexao import get_db

def cadastrar_usuario(email, rm, senha_plain):
    conn = None
    cursor = None
    try:
        conn = get_db()
        cursor = conn.cursor()

        sql = "INSERT INTO usuarios (email, rm, senha) VALUES (%s, %s, %s)"
        values = (email, rm, senha_plain)

        cursor.execute(sql, values)
        conn.commit()
        print(f"Usuário {email} cadastrado com sucesso!")
        return True
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"Erro ao cadastrar usuário: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
