import mysql.connector
def criar_tabela():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="aaa",
        password="",
        database="banco_de_dados"
    )
    cursor = conn.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS sua_tabela (
        id INT AUTO_INCREMENT PRIMARY KEY,
        coluna_obrigatoria VARCHAR(255),
        coluna_opcional1 DECIMAL(10,2),
        coluna_opcional2 INT
    )
    """
    cursor.execute(create_table_query)
    cursor.close()
    conn.close()
def inserir_dados():
    conn = mysql.connector.connect(
        host="seu_host",
        user="seu_usuario",
        password="sua_senha",
        database="nome_do_banco"
    )
    cursor = conn.cursor()
    insert_query_1 = """
    INSERT INTO sua_tabela (coluna_obrigatoria, coluna_opcional1, coluna_opcional2)
    VALUES ('valor_obrigatorio_1', 10.50, 20)
    """
    insert_query_2 = """
    INSERT INTO sua_tabela (coluna_obrigatoria, coluna_opcional1, coluna_opcional2)
    VALUES ('valor_obrigatorio_2', 15.75, 30)
    """
    cursor.execute(insert_query_1)
    cursor.execute(insert_query_2)
    conn.commit()
    cursor.close()
    conn.close()
def consultar_registros():
    conn = mysql.connector.connect(
        host="seu_host",
        user="seu_usuario",
        password="sua_senha",
        database="nome_do_banco"
    )
    cursor = conn.cursor()
    select_query = "SELECT * FROM sua_tabela"
    cursor.execute(select_query)
    registros = cursor.fetchall()
    if len(registros) == 0:
        print("Tabela vazia.")
    else:

        for registro in registros:
            print(registro)
    cursor.close()
    conn.close()
criar_tabela()
inserir_dados()
consultar_registros()