#Gerenciamento de Sementes.py

import database # Nosso novo arquivo de banco de dados
import csv
import os
from datetime import datetime, date, timedelta
from typing import Optional

# Caminho do arquivo CSV
CSV_FILE = "sementes.csv"
ALERTA_DIAS = 30


# -------------------------
# Funções auxiliares
# -------------------------

#Analisa data de entrada no formato Y-m-d e retorna objeto date ou None
def analise_de_data(text: str) -> Optional[date]:
    try:
        return datetime.strptime(text, "%Y-%m-%d").date()
    except ValueError:
        return None

# Entrada que não pode ser vazia
def entrada_naovazia(prompt: str) -> str:
    while True:
        v = input(prompt).strip()
        if v:
            return v
        print("Entrada vazia — tente novamente.")

# Entrada de inteiro positivo (ou zero)
def inteiro_positivo(prompt: str) -> int:
    while True:
        v = input(prompt).strip()
        try:
            n = int(v)
            if n < 0:
                raise ValueError
            return n
        except ValueError:
            print("Digite um número inteiro não-negativo.")

# Entrada de data (ou vazio)
def entrada_data(prompt: str) -> Optional[date]:
    while True:
        v = input(prompt).strip()
        if v == "":
            return None
        d = analise_de_data(v)
        if d:
            return d
        print("Formato inválido. Use AAAA-MM-DD ou deixe vazio.")


"""# -------------------------
# Funções de persistência (CSV)
# -------------------------
def load_data() -> list[dict]:
    if not os.path.exists(CSV_FILE):
        return []
    with open(CSV_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def save_data(rows: list[dict]):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["id", "nome", "quantidade", "data_validade"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def get_next_id(rows: list[dict]) -> int:
    if not rows:
        return 1
    ids = [int(r["id"]) for r in rows]
    return max(ids) + 1"""


# -------------------------
# Operações principais
# -------------------------

# Adiciona uma nova semente
def adicionar_sementes():
    nome = entrada_naovazia("Nome da semente: ")
    quantidade = inteiro_positivo("Quantidade (unidades): ")
    data_validade = entrada_data("Data de validade (AAAA-MM-DD) (opcional): ")

    # A nova função do database.py faz todo o trabalho!
    database.add_seed_db(nome, quantidade, data_validade)


# NOVA VERSÃO:

# Lista todas as sementes
def lista_sementes():
    rows = database.list_seeds_db() # Busca os dados direto do Oracle!
    if not rows:
        print("Nenhuma semente cadastrada.")
        return

    # O resto da função continua igual, pois nossa list_seeds_db já retorna o formato que ela espera
    print(f"\n{'ID':<5} {'NOME':<30} {'QTD':<8} {'VALIDADE':<12} {'STATUS'}")
    hoje = date.today()
    # ... (o resto do código do 'for' não muda)
    for r in rows:
        dv_str = r["data_validade"] or "-"
        status = ""
        if r["data_validade"]:
            dv = analise_de_data(r["data_validade"])
            if dv:
                delta = (dv - hoje).days
                if delta < 0:
                    status = "VENCIDO"
                elif delta <= ALERTA_DIAS:
                    status = f"ATENÇÃO ({delta}d)"
        print(f"{r['id']:<5} {r['nome']:<30} {r['quantidade']:<8} {dv_str:<12} {status}")


# (Substitua as funções correspondentes no seu arquivo principal)

def editar_sementes():
    lista_sementes() # Mostra a lista para o usuário saber qual ID editar
    rows_in_db = database.list_seeds_db()
    if not rows_in_db:
        print("Nenhuma semente para editar.")
        return

    try:
        semente_id = int(input("ID da semente a editar: ").strip())
    except ValueError:
        print("ID inválido.")
        return

    # Encontra a semente original para mostrar os dados atuais
    semente_original = None
    for r in rows_in_db:
        if int(r['id']) == semente_id:
            semente_original = r
            break
            
    if not semente_original:
        print("ID não encontrado.")
        return

    print(f"Editando semente: {semente_original['nome']}")
    novo_nome = input(f"Novo nome (ENTER para manter '{semente_original['nome']}'): ").strip() or semente_original['nome']
    
    nova_qtd_str = input(f"Nova quantidade (ENTER para manter {semente_original['quantidade']}): ").strip()
    if nova_qtd_str == "":
        quantidade = semente_original['quantidade']
    else:
        try:
            # Valida se a nova quantidade é um inteiro não-negativo
            n = int(nova_qtd_str)
            if n < 0: raise ValueError
            quantidade = str(n)
        except ValueError:
            print("Quantidade inválida. Deve ser um número inteiro não-negativo.")
            return

    # Para a data, usamos a função entrada_data que já retorna um objeto date ou None
    nova_data_obj = entrada_data(f"Nova data (AAAA-MM-DD | ENTER para manter '{semente_original['data_validade']}'): ")
    # Se o usuário não digitar nada, precisamos converter a data antiga de string para objeto date
    if nova_data_obj is None:
        data_final = analise_de_data(semente_original['data_validade']) if semente_original['data_validade'] else None
    else:
        data_final = nova_data_obj

    if database.edit_seed_db(semente_id, novo_nome, quantidade, data_final):
        print("Registro atualizado com sucesso.")
    else:
        print("Falha ao atualizar o registro. O ID pode não existir mais.")

# Exclui uma semente
def deletar_semente():
    lista_sementes()# Mostra a lista para o usuário saber qual ID excluir
    if not database.list_seeds_db():
         print("Nenhuma semente para excluir.")
         return

    try:
        semente_id = int(input("ID da semente a excluir: ").strip())
    except ValueError:
        print("ID inválido.")
        return

    confirmar = input(f"Tem certeza que deseja excluir a semente com ID {semente_id}? (s/N): ").lower().strip()
    if confirmar == 's':
        if database.delete_seed_db(semente_id):
            print("Registro excluído com sucesso.")
        else:
            print("ID não encontrado.")
    else:
        print("Operação cancelada.")

# Procura sementes por nome 
def procurar_sementes():
    termo = entrada_naovazia("Termo de busca: ").lower()
    matches = database.search_seeds_db(termo)
    
    if not matches:
        print("Nenhum resultado.")
        return

    print(f"\n{'ID':<5} {'NOME':<30} {'QTD':<8} {'VALIDADE'}")
    for r in matches:
        print(f"{r['id']:<5} {r['nome']:<30} {r['quantidade']:<8} {r['data_validade'] or '-'}")

# Verifica sementes com validade próxima ou vencida
def conferir_validade():
    vencidas = database.check_expirations_db(ALERTA_DIAS)

    if not vencidas:
        print(f"Nenhuma semente com validade próxima (nos próximos {ALERTA_DIAS} dias) ou vencida.")
        return

    print(f"\nSementes com validade próxima (<= {ALERTA_DIAS} dias):")
    hoje = date.today()
    for r in vencidas:
        dv = analise_de_data(r["data_validade"])
        dias = (dv - hoje).days
        status = "VENCIDA" if dias < 0 else f"vence em {dias} dias"
        print(f"[{r['id']}] {r['nome']} — {r['quantidade']} un. — {dv} ({status})")


# -------------------------
# Menu principal
# -------------------------
def print_menu():
    print("""
===== Gestão de Sementes =====
1) Cadastrar nova semente
2) Listar sementes
3) Editar semente
4) Excluir semente
5) Buscar por nome
6) Ver validade próxima/vencida
0) Sair
""")

# Loop principal
def main():
    while True:
        print_menu()
        op = input("Escolha uma opção: ").strip()
        if op == "1":
            adicionar_sementes()
        elif op == "2":
            lista_sementes()
        elif op == "3":
            editar_sementes()
        elif op == "4":
            deletar_semente()
        elif op == "5":
            procurar_sementes()
        elif op == "6":
            conferir_validade()
        elif op == "0":
            print("Saindo... até logo!")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
