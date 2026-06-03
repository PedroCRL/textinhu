# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="RepositorioFiap/templateFiapVfinal-main/assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# FarmTech

## IA_Underground

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/company/inova-fusca">Danilo Marques Dantas</a>
- <a href="https://www.linkedin.com/in/marlonmarinho/">Marlon Paulino Marinho</a>
- <a href="https://www.linkedin.com/in/pedro-carvalho-cea-149658137/">Pedro Carvalho Rocha Lima</a> 
- <a href="https://www.linkedin.com/in/viniciusl7">Vinicius Lisboa Porto</a> 
- <a href="https://www.linkedin.com/in/vinigama">Vinicius de Santana Gama</a>


## 📜 Descrição

O agronegócio é um dos pilares da economia brasileira, desempenhando um papel essencial na geração de renda, empregos e no fornecimento de alimentos para a população. Diante da crescente demanda global por alimentos e da necessidade de aprimorar a eficiência e a sustentabilidade das práticas agrícolas, a análise de dados tem se tornado uma ferramenta estratégica para apoiar a tomada de decisões nesse setor.<br>

Nesta atividade, foi desenvolvida uma base de dados representativa do contexto do agronegócio, contendo informações quantitativas e qualitativas sobre aspectos relevantes da produção agrícola. A base inclui variáveis como número de produtores (quantitativa discreta), produtividade média em toneladas por hectare (quantitativa contínua), tipo de cultura (qualitativa nominal) e nível de qualidade da produção (qualitativa ordinal).<br>

A partir dessa base de dados, foi realizada uma análise exploratória em R, com o objetivo de compreender o comportamento e a distribuição das variáveis. Para uma das variáveis quantitativas, foram calculadas as medidas de tendência central (média, mediana e moda), as medidas de dispersão (amplitude, variância e desvio padrão) e as medidas separatrizes (quartis e percentis). Além disso, foram construídos gráficos como histograma e boxplot para ilustrar visualmente a distribuição dos dados.<br>

Também foi escolhida uma variável qualitativa, para a qual foi elaborada uma análise gráfica por meio de gráficos de barras, permitindo observar a frequência e a predominância das categorias analisadas.<br>

A realização desta atividade possibilitou aplicar conceitos estatísticos e ferramentas de programação em R em um contexto real do agronegócio, demonstrando como a ciência de dados pode auxiliar na interpretação de informações e no apoio à tomada de decisão estratégica no setor.<br>



## 📁 Estrutura de pastas/arquivos

<b>.Rhistory:</b> Salva o histórico de todos os comandos digitados no console do R durante uma sessão de trabalho, facilitando a revisão e a reutilização de códigos. <br>

<b>base_agronegocio_soja_2024.xlsx - Página1.csv:</b> É o arquivo de dados brutos em formato CSV. Ele contém todas as informações sobre o agronegócio da soja que são utilizadas como base para a análise.<br>

<b>codigodeanalise.r:</b> O script principal do projeto. Contém o código em linguagem R que realiza a leitura, o tratamento, a análise estatística e a visualização dos dados do arquivo CSV.<br>

<b>README.md:</b> O documento de texto que descreve o projeto. Explica o objetivo da análise, a estrutura dos arquivos e como executar o código.<br>

<b>.DS_Store:</b> Um arquivo oculto gerado pelo sistema operacional macOS para armazenar as preferências de visualização de uma pasta. Não tem função direta no projeto e geralmente é ignorado.<br>

<b>.RData:</b> É o arquivo de workspace do R. Ele salva todos os objetos (variáveis, dataframes, funções, etc.) criados na memória durante a sessão de análise, permitindo que o trabalho seja retomado posteriormente.<br>

## 🔧 Como executar o código

<b>Pré-requisitos: Software Necessário</b> <br>
Antes de começar, você precisará de dois programas instalados:

<b>R:</b> A linguagem de programação. Baixe a versão mais recente para o seu sistema operacional no site oficial do R.<br>

<b>RStudio:</b> Um ambiente de desenvolvimento (IDE) que facilita o uso do R. Baixe a versão gratuita (Desktop) no site oficial do RStudio.<br>

<b>Git (Opcional, mas recomendado):</b> Para baixar o projeto diretamente do GitHub. Baixe no site oficial do Git.<br>

<b>Passo 1: Obter os Arquivos do Projeto</b> <br>

Abra o terminal (ou Git Bash no Windows).<br>

Navegue até a pasta onde você deseja salvar o projeto (ex: cd Documentos).<br>

Execute o seguinte comando para clonar o repositório:<br>

<p align="center">
<img src="assets/gitcloneN.png" border="0" width=40% height=40%>
</p>

<b>Passo 2: Abrir o Projeto e Instalar Pacotes</b><br>
Abra o RStudio.<br>

Vá em File > Open Project....<br>

Navegue até a pasta Fase-2 que você clonou ou extraiu, entre no subdiretório DecisaoComCienciaDeDados e abra o arquivo de projeto, se houver um com a extensão .Rproj. Caso não haja, simplesmente vá em File > Open File... e abra o arquivo codigodeanalise.r.<br>

Com o script codigodeanalise.r aberto, verifique as primeiras linhas por comandos como library(...). Eles indicam quais pacotes são necessários.<br>

Para instalar qualquer pacote que falte, vá ao painel Console no RStudio e digite:<br>

<b>install.packages("nome_do_pacote")</b>

<b>Passo 3: Executar o Script de Análise</b><br>
Agora que o ambiente está pronto, você pode rodar o código.<br>

Para executar o script inteiro de uma vez:<br>

Com o arquivo codigodeanalise.r em foco, clique no botão Source no canto superior direito do editor de código.<br>

<b>Passo 4: Verificar os Resultados</b><br>
Enquanto o código executa, observe os painéis do RStudio:<br>

Console (inferior esquerdo): Exibe mensagens, saídas de texto, tabelas e possíveis erros.<br>

Plots (inferior direito): Mostra todos os gráficos e visualizações gerados pelo script.<br>

Environment (superior direito): Lista os dataframes (tabelas de dados) e variáveis criados durante a execução.<br>

## 🗃 Histórico de lançamentos

* 0.1.0 - 15/10/2024
  