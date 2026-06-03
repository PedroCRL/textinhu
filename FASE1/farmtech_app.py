
"""
FarmTech Solutions - Agricultura Digital 
Culturas: Café (área circular) e soja (área retangular)

Requisitos:
- Vetores (listas) para armazenar dados
- Cálculo de área por cultura (figuras geométricas distintas)
- Cálculo de manejo de insumos (por metro de rua e por hectare)
- Menu com: entrada, saída, atualização, deleção, exportação e sair
- Estruturas de repetição e decisão
"""
import math
import csv
import os
from typing import List, Dict

# Estrutura de dados (vetores)
cafe_plots: List[Dict] = []         # Cada item: {"raio_m": float, "area_m2": float}
soja_plots: List[Dict] = []         # Cada item: {"compr_m": float, "larg_m": float, "area_m2": float}

# Utilidades
def m2_to_ha(area_m2: float) -> float:
    return area_m2 / 10_000.0

def input_float(msg: str, min_val: float = 0.0) -> float:
    while True:
        try:
            v = float(input(msg).replace(",", "."))
            if v < min_val:
                print(f"Valor deve ser >= {min_val}.")
                continue
            return v
        except ValueError:
            print("Entrada inválida. Digite um número.")

def print_header(title: str):
    print("\n" + "-" * 60)
    print(title)
    print("-" * 60)

def total_area_m2(vetor: List[Dict]) -> float:
    return sum(x["area_m2"] for x in vetor)

# Entrada de dados
def add_cafe_plot():
    print_header("Adicionar Talhão - Café (área circular)")
    r = input_float("Informe o raio do talhão em metros (m): ", 0.01)
    area = math.pi * r * r
    cafe_plots.append({"raio_m": r, "area_m2": area})
    print(f"Talhão de café adicionado. Área = {area:.2f} m² ({m2_to_ha(area):.4f} ha)")

def add_soja_plot():
    print_header("Adicionar Talhão - Soja (área retangular)")
    c = input_float("Comprimento do talhão em metros (m): ", 0.01)
    l = input_float("Largura do talhão em metros (m): ", 0.01)
    area = c * l
    soja_plots.append({"compr_m": c, "larg_m": l, "area_m2": area})
    print(f"Talhão de soja adicionado. Área = {area:.2f} m² ({m2_to_ha(area):.4f} ha)")

def entrada_dados():
    print_header("Entrada de Dados")
    print("1) Café (círculo)")
    print("2) Soja (retângulo)")
    op = input("Escolha a cultura (1-2): ").strip()
    if op == "1":
        add_cafe_plot()
    elif op == "2":
        add_soja_plot()
    else:
        print("Opção inválida.")

# Saída de dados
def listar_plots():
    print_header("Saída de Dados - Talhões")
    # Café
    print(">> Café (círculo)")
    if not cafe_plots:
        print("Nenhum talhão de café cadastrado.")
    else:
        for i, p in enumerate(cafe_plots):
            print(f"[{i}] raio={p['raio_m']:.2f} m | área={p['area_m2']:.2f} m² ({m2_to_ha(p['area_m2']):.4f} ha)")
        area_total = total_area_m2(cafe_plots)
        print(f"Total Café: {area_total:.2f} m² ({m2_to_ha(area_total):.4f} ha)")
    print("-" * 60)
    # Soja
    print(">> Soja (retângulo)")
    if not soja_plots:
        print("Nenhum talhão de soja cadastrado.")
    else:
        for i, p in enumerate(soja_plots):
            print(f"[{i}] C={p['compr_m']:.2f} m x L={p['larg_m']:.2f} m | área={p['area_m2']:.2f} m² ({m2_to_ha(p['area_m2']):.4f} ha)")
        area_total = total_area_m2(soja_plots)
        print(f"Total Soja: {area_total:.2f} m² ({m2_to_ha(area_total):.4f} ha)")

# Atualização de dados
def atualizar_dados():
    print_header("Atualização de Dados")
    print("1) Café   2) Soja")
    op = input("Escolha a cultura (1-2): ").strip()
    if op == "1":
        if not cafe_plots:
            print("Sem dados para atualizar.")
            return
        idx = input_float("Índice do talhão a atualizar: ", 0)
        idx = int(idx)
        if idx < 0 or idx >= len(cafe_plots):
            print("Índice inválido.")
            return
        r = input_float("Novo raio (m): ", 0.01)
        area = math.pi * r * r
        cafe_plots[idx] = {"raio_m": r, "area_m2": area}
        print("Talhão de café atualizado.")
    elif op == "2":
        if not soja_plots:
            print("Sem dados para atualizar.")
            return
        idx = input_float("Índice do talhão a atualizar: ", 0)
        idx = int(idx)
        if idx < 0 or idx >= len(soja_plots):
            print("Índice inválido.")
            return
        c = input_float("Novo comprimento (m): ", 0.01)
        l = input_float("Nova largura (m): ", 0.01)
        area = c * l
        soja_plots[idx] = {"compr_m": c, "larg_m": l, "area_m2": area}
        print("Talhão de soja atualizado.")
    else:
        print("Opção inválida.")

# Deletar  dados
def deletar_dados():
    print_header("Deletar Dados")
    print("1) Café   2) Soja")
    op = input("Escolha a cultura (1-2): ").strip()
    if op == "1":
        if not cafe_plots:
            print("Sem dados para deletar.")
            return
        idx = input_float("Índice do talhão a deletar: ", 0)
        idx = int(idx)
        if idx < 0 or idx >= len(cafe_plots):
            print("Índice inválido.")
            return
        removed = cafe_plots.pop(idx)
        print(f"Talhão removido. Área era {removed['area_m2']:.2f} m².")
    elif op == "2":
        if not soja_plots:
            print("Sem dados para deletar.")
            return
        idx = input_float("Índice do talhão a deletar: ", 0)
        idx = int(idx)
        if idx < 0 or idx >= len(soja_plots):
            print("Índice inválido.")
            return
        removed = soja_plots.pop(idx)
        print(f"Talhão removido. Área era {removed['area_m2']:.2f} m².")
    else:
        print("Opção inválida.")


# Manejo de insumos
def manejo_insumos():
    print_header("Manejo de Insumos")
    print("Escolha o tipo de cálculo:")
    print("1) Taxa por metro de rua (ex.: 500 mL/metro)")
    print("2) Taxa por hectare (ex.: 4 L/ha)")
    tipo = input("Opção (1-2): ").strip()

    produto = input("Nome do produto (ex.: fosfato, herbicida): ").strip()
    cultura = input("Cultura (café/soja): ").strip().lower()

    if tipo == "1":
        taxa_ml_por_m = input_float("Taxa de aplicação (mL por metro): ", 0.0)
        n_ruas = input_float("Número de ruas: ", 0.0)
        comp_rua_m = input_float("Comprimento de cada rua (m): ", 0.0)
        total_metros = n_ruas * comp_rua_m
        total_litros = (total_metros * taxa_ml_por_m) / 1000.0
        print(f"\nProduto: {produto}")
        print(f"Cultura: {cultura}")
        print(f"Total de metros: {total_metros:.2f} m")
        print(f"Volume necessário: {total_litros:.2f} L")
    elif tipo == "2":
        taxa_l_por_ha = input_float("Taxa de aplicação (L por hectare): ", 0.0)
        if cultura == "café":
            area_total_ha = m2_to_ha(total_area_m2(cafe_plots))
        elif cultura == "soja" or cultura == "soja" or cultura == "soja":
            area_total_ha = m2_to_ha(total_area_m2(soja_plots))
        else:
            print("Cultura não reconhecida. Use 'café' ou 'soja'.")
            return
        total_litros = taxa_l_por_ha * area_total_ha
        print(f"\nProduto: {produto}")
        print(f"Cultura: {cultura}")
        print(f"Área total: {area_total_ha:.4f} ha")
        print(f"Volume necessário: {total_litros:.2f} L")
    else:
        print("Opção inválida.")

# Exportação
def exportar_csv():
    print_header("Exportar dados para CSV")
    
    # Checar se há dados
    if not cafe_plots and not soja_plots:
        print("Não há dados para exportar.")
        return

    # Perguntar diretório para salvar
    default_dir = os.getcwd()
    diretorio = input(f"Diretório para salvar (Enter para usar atual '{default_dir}'): ").strip()
    if not diretorio:
        diretorio = default_dir

    # Validar diretório
    if not os.path.exists(diretorio):
        print(f"Diretório '{diretorio}' não existe. Criando diretório...")
        try:
            os.makedirs(diretorio)
        except Exception as e:
            print(f"Erro ao criar diretório: {e}")
            return

    # Perguntar nome do arquivo
    nome_arquivo = input("Nome do arquivo (Enter para usar 'farmtech_plots.csv'): ").strip()
    if not nome_arquivo:
        nome_arquivo = "farmtech_plots.csv"
    if not nome_arquivo.endswith('.csv'):
        nome_arquivo += '.csv'
    
    # Arquivo completo
    path = os.path.join(diretorio, nome_arquivo)

    # Preparar dados
    rows = []
    for p in cafe_plots:
        rows.append({
            "cultura": "cafe",
            "forma": "circulo",
            "param1": p["raio_m"],
            "param2": "",
            "area_m2": p["area_m2"],
            "area_ha": m2_to_ha(p["area_m2"])
        })
    for p in soja_plots:
        rows.append({
            "cultura": "soja",
            "forma": "retangulo",
            "param1": p["compr_m"],
            "param2": p["larg_m"],
            "area_m2": p["area_m2"],
            "area_ha": m2_to_ha(p["area_m2"])
        })
    
    try:
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["indice", "cultura", "forma", "param1", "param2", "area_m2", "area_ha"])
            writer.writeheader()
            writer.writerows(rows)
        print(f"Dados exportados para '{path}'.")
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")


# Menu principal
def menu():
    while True:
        print_header("FarmTech - Agricultura Digital ")
        print("1) Entrada de dados (cadastrar talhão)")
        print("2) Saída de dados (listar/exibir)")
        print("3) Atualização de dados")
        print("4) Deletar dados")
        print("5) Manejo de insumos")
        print("6) Exportar dados para CSV")
        print("7) Sair do programa")
        op = input("Escolha uma opção (1-7): ").strip()
        if op == "1":
            entrada_dados()
        elif op == "2":
            listar_plots()
        elif op == "3":
            atualizar_dados()
        elif op == "4":
            deletar_dados()
        elif op == "5":
            manejo_insumos()
        elif op == "6":
            exportar_csv()
        elif op == "7":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
# teste git