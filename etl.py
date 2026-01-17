import csv
import os
# CAMINHOS ABSOLUTOS
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PASTA_DATA = os.path.join(BASE_DIR, "data")

CAMINHO_USUARIOS = os.path.join(PASTA_DATA, "usuarios.csv")
CAMINHO_MENSAGENS = os.path.join(PASTA_DATA, "mensagens.csv")
# EXTRAÇÃO
usuarios = []

with open(CAMINHO_USUARIOS, newline="", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        usuarios.append(linha)
# TRANSFORMAÇÃO
mensagens = []

for usuario in usuarios:
    nome = usuario["nome"]
    conta = usuario["conta"]

    mensagem = (
        f"Olá {nome}, identificamos uma oportunidade especial "
        f"para sua conta {conta}. Aproveite os benefícios exclusivos!"
    )

    mensagens.append({
        "nome": nome,
        "mensagem": mensagem
    })
# CARREGAMENTO
with open(CAMINHO_MENSAGENS, mode="w", newline="", encoding="utf-8") as arquivo:
    campos = ["nome", "mensagem"]
    escritor = csv.DictWriter(arquivo, fieldnames=campos)
    escritor.writeheader()

    for msg in mensagens:
        escritor.writerow(msg)

print("ETL finalizado com sucesso.")
