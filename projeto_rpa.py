import requests
import sqlite3
import re
import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ======= 0. Carregar variáveis do .env ========
load_dotenv()
EMAIL_REMETENTE = os.getenv("EMAIL_REMETENTE")
EMAIL_SENHA = os.getenv("EMAIL_SENHA_APP")
EMAIL_DESTINATARIO = os.getenv("EMAIL_DESTINATARIO")

# ======= 1. Requisição à API ========
url = "https://api.adviceslip.com/advice"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    advice_id = data['slip']['id']
    advice_text = data['slip']['advice']
    print(f"🧠 Conselho recebido: {advice_text}")
else:
    print("❌ Erro ao acessar a API.")
    exit()

# ======= 2. Banco de Dados ========
conn = sqlite3.connect('projeto_rpa.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS conselhos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        advice_id INTEGER,
        texto TEXT
    )
''')
cursor.execute("INSERT INTO conselhos (advice_id, texto) VALUES (?, ?)", (advice_id, advice_text))
conn.commit()

# ======= 3. Processamento com regex ========
palavras = re.findall(r'\b\w{5,}\b', advice_text)
texto_processado = ', '.join(palavras)

cursor.execute('''
    CREATE TABLE IF NOT EXISTS dados_processados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        palavras_chave TEXT
    )
''')
cursor.execute("INSERT INTO dados_processados (palavras_chave) VALUES (?)", (texto_processado,))
conn.commit()

# ======= 4. Envio de e-mail ========
assunto = "Relatório Automático - Projeto RPA"
mensagem = f"""
Olá!

Segue abaixo o relatório automatizado:

🧾 Conselho Coletado:
"{advice_text}"

🔍 Palavras-chave extraídas (com 5 letras ou mais):
{texto_processado}

Atenciosamente,
Script RPA em Python
"""

msg = MIMEMultipart()
msg['From'] = EMAIL_REMETENTE
msg['To'] = EMAIL_DESTINATARIO
msg['Subject'] = assunto
msg.attach(MIMEText(mensagem, 'plain'))

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
        servidor.login(EMAIL_REMETENTE, EMAIL_SENHA)
        servidor.send_message(msg)
        print("📧 E-mail enviado com sucesso!")
except Exception as e:
    print(f"❌ Erro ao enviar e-mail: {e}")

conn.close()
