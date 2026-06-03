# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# FarmTech Solutions
# <a href="https://youtu.be/cqdMUJCMDng">Link vídeo no Youtube - Mapa do Tesouro</a>

## IA_Underground

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/company/inova-fusca">Danilo Marques Dantas</a>
- <a href="https://www.linkedin.com/in/marlonmarinho/">Marlon Paulino Marinho</a>
- <a href="https://www.linkedin.com/in/pedro-carvalho-cea-149658137/">Pedro Carvalho Rocha Lima</a> 
- <a href="https://www.linkedin.com/in/viniciusl7">Vinicius Lisboa Porto</a> 
- <a href="https://www.linkedin.com/in/vinigama">Vinicius de Santana Gama</a>

## 📜 Descrição

O projeto é modularizado em três diretórios principais, cada um contendo uma solução específica:

- <b>/PythonAlem</b>: Contém o código utilizado para o desenvolvimento da solução de software para o gerenciamento de insumos agrícolas. Trata-se de uma aplicação de linha de comando (CLI) em Python que permite o cadastro, listagem, edição e exclusão de sementes, com dados persistidos em um banco de dados Oracle.

<p align="center">
<img src="assets/gestao_semente_terminal.png" alt="Imagem Gestão de Semente no terminal de comando" border="0" width=30% height=30%>
</p>

- <b>/mapadotesouro</b>: Neste diretório está o projeto de hardware e IoT. Utilizando uma placa ESP32, sensores de temperatura, umidade e luminosidade, o sistema é projetado para o monitoramento e controle de ambientes agrícolas. O projeto foi desenvolvido com PlatformIO e pode ser simulado no Wokwi.

<p align="center">
<img src="assets/mapatesouro.png" alt="Imagem sensor Mapa do Tesouro" border="0" width=30% height=30%>
</p>

- <b>/DecisaoComCienciaDeDados</b>: Aqui se encontra a análise de dados do projeto. Utilizando a linguagem R, este componente analisa um conjunto de dados sobre o agronegócio da soja (base_agronegocio_soja_2024.csv) para extrair insights, visualizar tendências e auxiliar na tomada de decisões estratégicas no campo.


- <b>/README.md</b>: Este arquivo, que serve como guia e explicação geral sobre o projeto.

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>PythonAlem</b>: Todo o código utilizado para o desenvolvimento da solução de software para o gerenciamento de insumos agrícolas.

- <b>mapatesouro</b>: Todo o código utilizado para o monitoramento e controle de ambientes agrícolas.

- <b>DecolandoComCienciaDeDados</b>: Todo o código utilizado para analisar um conjunto de dados sobre o agronegócio da soja.

- <b>README.md</b>: Arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 🔧 Como executar o código

Entre em cada diretório para poder conseguir executar cada um dos códigos.

<b>PythonAlem (Gerenciamento de Sementes):</b>

Certifique-se de ter o Python e a biblioteca oracledb instalados (pip install oracledb).

Configure suas credenciais de acesso ao banco de dados Oracle no arquivo database.py ou através de variáveis de ambiente.

Execute o programa principal com o comando: python "Gerenciamento de Sementes.py". <br>

<b>mapadotesouro (Projeto IoT):</b>

É recomendado o uso do Visual Studio Code com a extensão PlatformIO.

Abra a pasta do projeto no VS Code.

Você pode compilar e enviar o código para uma placa ESP32 física ou iniciar uma simulação no Wokwi (utilizando o arquivo diagram.json). <br>

<b>DecisaoComCienciaDeDados (Análise em R):</b>

É necessário um ambiente R (como o RStudio).

Abra o script codigodeanalise.r.

Execute o script. Ele irá carregar o arquivo base_agronegocio_soja_2024.xlsx - Página1.csv para realizar a análise estatística e gerar as visualizações.

## 🗃 Histórico de lançamentos

* 0.1.0 - 14/10/2025
  
