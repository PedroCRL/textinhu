# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# FarmTech Solutions

## IA_Underground

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/company/inova-fusca">Danilo Marques Dantas</a>
- <a href="https://www.linkedin.com/in/marlonmarinho/">Marlon Paulino Marinho</a>
- <a href="https://www.linkedin.com/in/pedro-carvalho-cea-149658137/">Pedro Carvalho Rocha Lima</a> 
- <a href="https://www.linkedin.com/in/viniciusl7">Vinicius Lisboa Porto</a> 
- <a href="https://www.linkedin.com/in/vinigama">Vinicius de Santana Gama</a>

## 📜 Descrição Python e além

Este projeto foi desenvolvido no âmbito do Problem Based Learning (PBL) com o tema Agronegócio, e consiste em uma solução de software para o gerenciamento de insumos agrícolas, com foco específico no controle de estoque e validade de sementes.

O agronegócio é um pilar fundamental da economia brasileira, um setor que vai muito além da fazenda e que hoje é sinônimo de inovação e tecnologia (AgroTech). No entanto, um dos desafios enfrentados por pequenos e médios produtores é a gestão eficiente de seus insumos. Perdas de sementes por vencimento, falta de controle sobre a quantidade disponível e dificuldade no planejamento de safras são problemas reais que impactam diretamente a produtividade e a lucratividade.

Visando solucionar essa "dor", este sistema oferece uma ferramenta simples e funcional, desenvolvida em Python e operada via terminal (interface de linha de comando). A aplicação se conecta a um banco de dados Oracle para garantir a persistência e a segurança dos dados, permitindo ao produtor realizar as seguintes operações:

<b>Cadastrar:</b> <br>
Adicionar novos tipos de sementes ao estoque, com informações de nome, quantidade e data de validade.

<b>Listar:</b> <br>
Visualizar de forma organizada todas as sementes em estoque, com um sistema de status que alerta sobre a proximidade do vencimento.

<b>Editar e Excluir:</b> <br>
Atualizar informações de sementes existentes ou remover itens do estoque.

<b>Buscar:</b> <br>
Pesquisar rapidamente por uma semente específica pelo nome.

<b>Verificar Validade:</b> <br>
Gerar um relatório focado em sementes que estão vencidas ou que irão vencer nos próximos 30 dias.

O projeto materializa o conceito de AgroTech ao aplicar tecnologia para resolver um problema prático do campo, oferecendo uma solução robusta para otimizar o controle de insumos, reduzir desperdícios e auxiliar na tomada de decisões estratégicas do produtor rural.


## 📁 Estrutura de pastas Python e além

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>#Gerenciamento de Sementes.py</b>: Aqui está todo o código fonte do projeto para poder ser executado.

- <b>database.py</b>: Código CRUD do Banco de Dados junto com integração a ORACLE

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

- <b>.gitignore</b>: Arquivo que serve para ignorar outros arquivos que não devem estar no GitHUb.

## 🔧 Como executar o código Python e além
Antes de começar, garanta que você tenha os seguintes softwares instalados:

<b>Python:</b> Versão 3.10 ou superior.

<b>Git:</b> Para clonar o repositório.

<b>Acesso a um Banco de Dados Oracle:</b> O sistema foi configurado para se conectar a uma instância Oracle. As credenciais e o endereço do banco precisam ser configurados.

<b>1 - Instalação e Configuração</b> <br>
<b>Clone o repositório:</b> Abra seu terminal e execute o seguinte comando:

<p align="center">
<img src="assets/gitcloneN.png" border="0" width=40% height=40%>
</p>

<b>2 - Navegue até a pasta do projeto:</b>

cd Fase-2/PythonAlem <br>
<b>Instale as dependências:</b>
O projeto requer a biblioteca oracledb para se comunicar com o banco de dados. Instale-a usando o pip:

<p align="center">
<img src="assets/pipInstall.png" border="0" width=40% height=40%>
</p>

<b>3 - Configure o Banco de Dados:</b><br>
Crie a tabela de sementes na sua instância Oracle executando o seguinte script SQL:

<p align="center">
<img src="assets/createTable.png" border="0" width=40% height=40%>
</p>

Abra o arquivo database.py e atualize as variáveis user, password e dsn com as suas credenciais de acesso ao banco de dados Oracle.

<b>4 - Execução</b><br>
Após a configuração, execute o programa principal a partir do terminal, na pasta do projeto:

<p align="center">
<img src="assets/rodar.png" border="0" width=40% height=40%>
</p>
O menu interativo da aplicação será exibido no terminal, e você poderá começar a usar o sistema.


## 🗃 Histórico de lançamentos

* 0.1.0 - 14/10/2025
  
