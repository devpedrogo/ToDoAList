import sqlite3

DB_FILE = 'banco.db'

def connect_db():
    conn = sqlite3.connect(DB_FILE)
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            prioridade INTEGER NOT NULL,
            concluida INTEGER NOT NULL,
            data_criacao TEXT NOT NULL
        );
        """
    )

    conn.commit()
    print("Tabela criada com sucesso!")
    conn.close()