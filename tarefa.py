import sqlite3

from database import connect_db
from datetime import datetime

PRIORIDADES = {
    1: "BAIXA",
    2: "MÉDIA",
    3: "ALTA"
}
STATUS = {
    0: "PENDENTE",
    1: "CONCLUÍDA"
}

def adicionar_tarefa(titulo, descricao, prioridade):

    conn = connect_db()

    concluida = 0
    data_criacao = datetime.now().isoformat()

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO tarefas (titulo, descricao, prioridade, concluida, data_criacao)
    VALUES (?, ?, ?, ?, ?);
    """, (titulo, descricao, prioridade, concluida, data_criacao))

    conn.commit()
    print("Tarefa adicionada com sucesso!")

    conn.close()


def formatar_tarefa(tarefa):

    id_tarefa = tarefa[0]
    titulo = tarefa[1]
    prioridade_txt = PRIORIDADES.get(tarefa[3], "Desconhecida")
    status_txt = STATUS.get(tarefa[4], "Desconhecida")

    data_criacao = tarefa[5].split('T')[0]  # Pega apenas a data

    return (
        f"ID: {id_tarefa:<3} | Status: {status_txt:<14} | Prioridade: {prioridade_txt:<6} "
        f"| Criada em: {data_criacao:<10} | Título: {titulo}"
    )

def listar_tarefas():

    conn = connect_db()

    cursor = conn.cursor()

    try:
        cursor.execute("SELECT id, titulo, descricao, prioridade, concluida, data_criacao FROM tarefas ORDER BY data_criacao ASC;")

        tarefas = cursor.fetchall()

        if not tarefas:
            print("\nNenhuma tarefa encontrada.")
            return

        print(f"\n--- Lista de Tarefas ({len(tarefas)} encontradas) ---")
        for tarefa in tarefas:
            print(formatar_tarefa(tarefa))
        print("---------------------------------------")

    except sqlite3.Error as e:
        print(f"ERRO! Não foi possível listar as tarefas: {e}")
    finally:
        conn.close()


def listar_filtro(filtro_prioridade=None, filtro_status=None):
    conn = connect_db()

    cursor = conn.cursor()

    sql_query = "SELECT id, titulo, descricao, prioridade, concluida, data_criacao FROM tarefas "
    condicoes = []
    valores = []

    if filtro_prioridade is not None:
        condicoes.append("prioridade = ?")
        valores.append(filtro_prioridade)

    if filtro_status is not None:
        condicoes.append("concluida = ?")
        valores.append(filtro_status)

    if condicoes:
        sql_query += " WHERE " + " AND ".join(condicoes)

    sql_query += " ORDER BY prioridade DESC, data_criacao ASC;"

    try:
        cursor.execute(sql_query, valores)
        tarefas = cursor.fetchall()

        if not tarefas:
            print("\nNenhuma tarefa encontrada.")
            return

        print(f"\n--- Lista de Tarefas ({len(tarefas)} encontradas) ---")
        for tarefa in tarefas:
            print(formatar_tarefa(tarefa))
        print("---------------------------------------")

    except sqlite3.Error as e:
        print(f"ERRO! Não foi possível listar as tarefas: {e}")
    finally:
        conn.close()

def concluir_tarefa(tarefa_id):

    conn = connect_db()

    cursor = conn.cursor()

    try:
        cursor.execute("""
        UPDATE tarefas
        SET concluida = 1
        WHERE id = ?;
        """, (tarefa_id,))

        conn.commit()

        if cursor.rowcount > 0:
            print(f"\nSUCESSO! Tarefa ID {tarefa_id} marcada como CONCLUÍDA.")
        else:
            print(f"\nAVISO! Nenhuma tarefa encontrada com o ID {tarefa_id}.")

    except sqlite3.Error as e:
        print(f"\nERRO! Não foi possível atualizar a tarefa: {e}")
    finally:
        conn.close()


def excluir_tarefa(tarefa_id):

    conn = connect_db()

    cursor = conn.cursor()

    try:
        cursor.execute("""
        DELETE FROM tarefas
        WHERE id = ?;
        """, (tarefa_id,))

        conn.commit()

        if cursor.rowcount > 0:
            print(f"\nSUCESSO! Tarefa ID {tarefa_id} excluída permanentemente.")
        else:
            print(f"\nAVISO! Nenhuma tarefa encontrada com o ID {tarefa_id} para exclusão.")

    except sqlite3.Error as e:
        print(f"\nERRO! Não foi possível excluir a tarefa: {e}")
    finally:
        conn.close()