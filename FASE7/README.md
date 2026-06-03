# FASE 7 — Sistema Integrado FarmTech Solutions

**Equipe:** IA_Underground | **FIAP ON** | 2025

---

## O que é essa fase?

A Fase 7 é o "painel de controle" de todo o projeto FarmTech. Em vez de ter que navegar em cada pasta e rodar cada script separadamente, a gente criou um sistema centralizado que permite iniciar qualquer fase com um único comando.

Resumindo: ela integra tudo que foi feito nas Fases 1 a 6 num único lugar.

---

## Estrutura dos arquivos

```
FASE7/
├── run.py            # Menu interativo no terminal (CLI)
├── launcher.py       # Dashboard visual no navegador (Streamlit)
├── config.json       # Configurações centralizadas de todas as fases
└── requirements.txt  # Dependências necessárias para rodar
```

---

## Como instalar

Antes de tudo, instale a dependência do launcher:

```bash
pip install -r requirements.txt
```

> Isso instala o Streamlit, que é a biblioteca usada para criar o dashboard visual.

---

## Como usar

### Opção 1 — Terminal (mais simples)

Abra o terminal na pasta `FASE7/` e rode:

```bash
# Abre o menu interativo com todas as fases
python run.py

# Lança uma fase específica direto (sem passar pelo menu)
python run.py 4d

# Abre o dashboard visual no navegador
python run.py dashboard

# Mostra todas as fases cadastradas (inclusive as desativadas)
python run.py --list
```

**Exemplo de menu interativo:**

```
  ══════════════════════════════════════════════════════════
  FarmTech Solutions
  Setor: Agronegócio  |  Equipe: IA_Underground
  ──────────────────────────────────────────────────────────
  [ 1]  [CLI]  Gestão de Áreas e Insumos
  [2a]  [CLI]  Gestão de Sementes (Oracle DB)
  [2b]  [ R ]  Consulta Meteorológica
  [2c]  [ R ]  Análise R — Áreas por Cultura
  [4t]  [CLI]  Treinar Modelos IoT
  [4d]  [WEB]  Dashboard ML — Irrigação  (:8502)
  [ 5]  [ NB]  Previsão de Rendimento (Cloud)
  [ 6]  [ NB]  Visão Computacional (YOLO)
  ──────────────────────────────────────────────────────────
  [ 0]  [WEB]  Dashboard Completo (Fase 7)
  [ q]         Sair
  ══════════════════════════════════════════════════════════

  Opção: _
```

### Opção 2 — Dashboard no navegador (mais visual)

```bash
streamlit run launcher.py
```

Depois acesse **http://localhost:8501** no navegador. O dashboard mostra todas as fases em cards e permite iniciar e parar cada uma com um botão.

> Se der conflito de porta com a Fase 4, use:
> `streamlit run launcher.py --server.port 8500`

---

## Fases disponíveis

| ID  | Nome                              | Tipo       | Porta |
|-----|-----------------------------------|------------|-------|
| 1   | Gestão de Áreas e Insumos         | CLI Python | —     |
| 2a  | Gestão de Sementes (Oracle DB)    | CLI Python | —     |
| 2b  | Consulta Meteorológica            | R Script   | —     |
| 2c  | Análise R — Áreas por Cultura     | R Script   | —     |
| 3   | Classificação de Culturas (ML)    | CLI Python | —     |
| 4t  | Treinar Modelos IoT               | CLI Python | —     |
| 4d  | Dashboard ML — Irrigação          | Streamlit  | 8502  |
| 5   | Previsão de Rendimento (Cloud)    | Jupyter    | —     |
| 6   | Visão Computacional (YOLO)        | Jupyter    | —     |

> **Atenção:** A Fase 3 requer as bibliotecas `pandas`, `scikit-learn`, `matplotlib` e `seaborn` instaladas. Instale com `pip install pandas scikit-learn matplotlib seaborn`.

---

## Tipos de execução

O sistema suporta 4 tipos de execução diferentes:

| Tipo         | Como roda                                   | Exemplo de uso           |
|--------------|---------------------------------------------|--------------------------|
| `cli_python` | Abre no próprio terminal                    | Fases 1, 2a, 4t          |
| `streamlit`  | Abre no navegador (nova aba)                | Fases 4d, 7 (dashboard)  |
| `r_script`   | Roda via Rscript (requer R instalado)       | Fases 2b, 2c             |
| `jupyter`    | Abre o Jupyter Notebook no navegador        | Fases 3, 5, 6            |

---

## Configurando o sistema — editando o config.json

O `config.json` é o coração do sistema. Qualquer mudança no projeto (nome, equipe, caminhos dos scripts) deve ser feita aqui.

### Estrutura geral

```json
{
  "sector": "Agronegócio",
  "project_name": "FarmTech Solutions",
  "team": "IA_Underground",
  "description": "Descrição do projeto",
  "phases": [ ... ]
}
```

### Estrutura de cada fase

```json
{
  "id": "4d",
  "name": "Dashboard ML — Irrigação",
  "description": "Descrição curta que aparece no dashboard.",
  "type": "streamlit",
  "path": "FASE4/CAP1/dashboard.py",
  "port": 8502,
  "enabled": true
}
```

**Campos explicados:**
- `id` — identificador único, é o que você digita no menu (ex: `4d`)
- `name` — nome que aparece no menu e no dashboard
- `description` — texto de ajuda que explica o que aquela fase faz
- `type` — tipo de execução: `cli_python`, `streamlit`, `r_script` ou `jupyter`
- `path` — caminho do script **a partir da pasta raiz do projeto** (não da FASE7)
- `port` — número da porta (só obrigatório para fases do tipo `streamlit`)
- `enabled` — `true` para aparecer no menu, `false` para esconder

---

## Requisitos por tipo de fase

| O que precisa | Para qual tipo |
|---------------|---------------|
| Python 3.10+  | Tudo          |
| `pip install streamlit` | Fases Streamlit e o dashboard |
| R + Rscript no PATH | Fases R Script |
| `pip install jupyter` | Fases Jupyter |
| Oracle Client + cx_Oracle | Fase 2a |

---

## Fluxo de uso recomendado

Para quem está abrindo o projeto pela primeira vez:

1. Instale as dependências: `pip install -r requirements.txt`
2. Rode `python run.py` para ver o menu
3. Comece pela Fase 1 para entender o fluxo básico
4. Para as análises de ML, rode a Fase 4t primeiro (treina os modelos) e depois a 4d (dashboard)
5. Para o dashboard visual completo, escolha a opção `0` no menu ou `python run.py dashboard`

---

## Observações importantes

- **Ctrl+C** encerra qualquer processo que esteja rodando (Streamlit, scripts, etc.)
- Se um script R não abrir, verifique se o R está instalado e o `Rscript` está no PATH do sistema
- O dashboard da Fase 7 fica na porta **8501** e o da Fase 4d na **8502** — portas diferentes para não conflitar
- Mudanças no `config.json` pelo dashboard visual são salvas automaticamente no arquivo
- A Fase 3 precisa do arquivo `produtos_agricolas.csv` na pasta `FASE3/` — ele já está incluído no projeto
