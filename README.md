🧠 Projeto RPA em Python com API de Conselhos
Automação em Python que coleta dados de uma API pública, armazena no SQLite, processa com expressões regulares, gera um relatório em PDF e envia por e-mail de forma automática.

📌 Objetivo
Demonstrar como utilizar Python para criar uma automação completa integrando API, banco de dados, processamento de texto e envio de e-mails — ideal para fins didáticos e projetos de aprendizado.

⚙️ Tecnologias Utilizadas
* Python 3
* Requests
* SQLite3
* re (Regex)
* smtplib
* ReportLab
* python-dotenv

🧩 Funcionalidades
* Coleta de conselhos aleatórios via API (https://api.adviceslip.com/advice)
* Armazenamento dos dados em banco SQLite
* Extração de palavras-chave com expressões regulares
* Geração automática de um relatório em PDF
* Envio do relatório por e-mail de forma automatizada

📄 Exemplo de Relatório Gerado
O PDF gerado inclui:
* Nome do autor do projeto
* Título do projeto
* API utilizada e justificativa
* Descrição das etapas realizadas
* Conclusão com dificuldades e aprendizados

🔐 Variáveis de Ambiente (.env)
Crie um arquivo .env com o seguinte conteúdo:

env: 
EMAIL_REMETENTE=seuemail@gmail.com
EMAIL_SENHA_APP=suasenhadeaplicativo
EMAIL_DESTINATARIO=destinatario@gmail.com
⚠️ A senha precisa ser uma senha de aplicativo do Gmail, não sua senha pessoal.

▶️ Como Executar
1. Clone o repositório
git clone https://github.com/seuusuario/nome-do-repositorio.git

2. Execute o script principal
python projeto_rpa.py

🧠 Aprendizados
Este projeto reforça o uso de bibliotecas nativas e externas do Python para resolver tarefas comuns em automação de processos, além de demonstrar boas práticas no uso de APIs, banco de dados e geração de relatórios.
