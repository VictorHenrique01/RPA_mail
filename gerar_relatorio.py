from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

# === Dados personalizados ===
nome_aluno = "Victor Henrique Souza Oliveira"
titulo_projeto = "RPA em Python com API de Conselhos"
api_usada = "https://api.adviceslip.com/advice"
justificativa = "Escolhi essa API por ser simples, gratuita e ideal para demonstrações de automação."
dificuldades = "Algumas dificuldades foram configurar o envio de e-mail e manipular o banco SQLite."
aprendizados = "Aprendi como integrar APIs, armazenar dados,\nprocessar texto e enviar e-mails automaticamente."
data_hoje = datetime.now().strftime("%d/%m/%Y")

# === Criar PDF ===
arquivo = "Relatorio_Projeto_RPA.pdf"
pdf = canvas.Canvas(arquivo, pagesize=A4)
largura, altura = A4

pdf.setTitle("Relatório do Projeto RPA")

# === Criar objeto de texto ===
text = pdf.beginText()
text.setTextOrigin(50, altura - 150)
text.setFont("Helvetica", 12)

# === Texto com quebras de linha ===
conteudo = f"""
Relatório do Projeto - {titulo_projeto}
Aluno: {nome_aluno}
Data: {data_hoje}

1. API Escolhida:
- URL: {api_usada}
- Justificativa: {justificativa}

2. Etapas Executadas:
- Coleta de dados via API (requests)
- Armazenamento no banco SQLite (sqlite3)
- Processamento com expressões regulares (re)
- Geração de relatório automático (este PDF)
- Envio automatizado por e-mail (smtplib)

3. Conclusão:
- Dificuldades: {dificuldades}
- Aprendizados: {aprendizados}
"""

# Adiciona cada linha (respeitando \n)
for linha in conteudo.strip().split('\n'):
    text.textLine(linha)

pdf.drawText(text)
pdf.save()
print(f"📄 Relatório gerado com sucesso: {arquivo}")
