import oracledb
import os
from datetime import date

# --- Configuração da Conexão ---
# É uma boa prática usar variáveis de ambiente para não deixar usuário e senha no código.
# Configure-as no seu sistema ou substitua os valores diretamente para testar.
user = os.getenv("DB_USER", "rm566672")
password = os.getenv("DB_PASSWORD", "061004")
dsn = os.getenv("DB_DSN", "oracle.fiap.com.br:1521/ORCL") # Ex: "localhost/XEPDB1" ou o TNS Name

def get_connection():
    """Cria e retorna uma conexão com o banco de dados Oracle."""
    try:
        conn = oracledb.connect(user=user, password=password, dsn=dsn)
        return conn
    except oracledb.DatabaseError as e:
        print(f"Erro ao conectar ao Oracle: {e}")
        return None

# --- Funções de CRUD ---

def list_seeds_db():
    """Busca todas as sementes do banco de dados."""
    conn = get_connection()
    if not conn:
        return []
    
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT ID_SEMENTE, NOME, QUANTIDADE, DT_VALIDADE FROM TBL_SEMENTES ORDER BY ID_SEMENTE")
        rows = cursor.fetchall()
        
        # Converte a lista de tuplas para uma lista de dicionários, como era antes
        seeds = []
        for row in rows:
            # Lida com a data de validade que pode ser None (nula)
            validade = row[3].strftime('%Y-%m-%d') if row[3] else ""
            seeds.append({
                "id": str(row[0]),
                "nome": row[1],
                "quantidade": str(row[2]),
                "data_validade": validade
            })
        return seeds
    finally:
        cursor.close()
        conn.close()


def add_seed_db(nome: str, quantidade: int, data_validade: date | None):
    """Adiciona uma nova semente no banco de dados."""
    conn = get_connection()
    if not conn:
        return
        
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO TBL_SEMENTES (NOME, QUANTIDADE, DT_VALIDADE) VALUES (:1, :2, :3)"
        cursor.execute(sql, [nome, quantidade, data_validade])
        conn.commit()
        print("Semente cadastrada com sucesso no banco de dados!")
    except oracledb.DatabaseError as e:
        print(f"Erro ao inserir semente: {e}")
        conn.rollback() # Desfaz a transação em caso de erro
    finally:
        cursor.close()
        conn.close()

# Você irá criar aqui as funções para editar (update) e excluir (delete) depois...

# (continuação do arquivo database.py...)

def edit_seed_db(seed_id: int, nome: str, quantidade: str, data_validade: date | None):
    """Atualiza uma semente existente no banco de dados."""
    conn = get_connection()
    if not conn:
        return False
    
    cursor = conn.cursor()
    try:
        sql = """
            UPDATE TBL_SEMENTES 
            SET NOME = :1, QUANTIDADE = :2, DT_VALIDADE = :3
            WHERE ID_SEMENTE = :4
        """
        cursor.execute(sql, [nome, int(quantidade), data_validade, seed_id])
        conn.commit()
        # rowcount > 0 significa que a linha foi encontrada e atualizada
        return cursor.rowcount > 0 
    except oracledb.DatabaseError as e:
        print(f"Erro ao atualizar semente: {e}")
        conn.rollback()
        return False
    finally:
        cursor.close()
        conn.close()


def delete_seed_db(seed_id: int):
    """Exclui uma semente do banco de dados pelo seu ID."""
    conn = get_connection()
    if not conn:
        return False

    cursor = conn.cursor()
    try:
        sql = "DELETE FROM TBL_SEMENTES WHERE ID_SEMENTE = :1"
        cursor.execute(sql, [seed_id])
        conn.commit()
        return cursor.rowcount > 0
    except oracledb.DatabaseError as e:
        print(f"Erro ao excluir semente: {e}")
        conn.rollback()
        return False
    finally:
        cursor.close()
        conn.close()
        

def search_seeds_db(termo: str):
    """Busca sementes por nome no banco de dados."""
    conn = get_connection()
    if not conn:
        return []

    cursor = conn.cursor()
    try:
        # Usamos LOWER para busca case-insensitive e % para buscar em qualquer parte do nome
        sql = "SELECT ID_SEMENTE, NOME, QUANTIDADE, DT_VALIDADE FROM TBL_SEMENTES WHERE LOWER(NOME) LIKE :termo ORDER BY NOME"
        # O termo de busca precisa estar entre '%'
        search_term = f"%{termo.lower()}%"
        cursor.execute(sql, termo=search_term)
        
        rows = cursor.fetchall()
        seeds = []
        for row in rows:
            validade = row[3].strftime('%Y-%m-%d') if row[3] else ""
            seeds.append({
                "id": str(row[0]),
                "nome": row[1],
                "quantidade": str(row[2]),
                "data_validade": validade
            })
        return seeds
    finally:
        cursor.close()
        conn.close()

def check_expirations_db(alerta_dias: int):
    """Busca sementes vencidas ou próximas do vencimento."""
    conn = get_connection()
    if not conn:
        return []

    cursor = conn.cursor()
    try:
        # SYSDATE é a data atual no Oracle. O cálculo é feito diretamente no banco.
        sql = """
            SELECT ID_SEMENTE, NOME, QUANTIDADE, DT_VALIDADE
            FROM TBL_SEMENTES
            WHERE DT_VALIDADE IS NOT NULL AND DT_VALIDADE <= SYSDATE + :dias
            ORDER BY DT_VALIDADE
        """
        cursor.execute(sql, dias=alerta_dias)
        
        rows = cursor.fetchall()
        seeds = []
        for row in rows:
            validade = row[3].strftime('%Y-%m-%d') if row[3] else ""
            seeds.append({
                "id": str(row[0]),
                "nome": row[1],
                "quantidade": str(row[2]),
                "data_validade": validade
            })
        return seeds
    finally:
        cursor.close()
        conn.close()