"""
Persistência em JSON e acesso aos dados (áreas, leituras e relatos).
"""

import json
from datetime import datetime

from config import ARQUIVO_DADOS, FORMATO_DATA


def dados_vazios():
    return {"areas": [], "leituras": [], "relatos": []}


def carregar_dados():
    """Lê o JSON; se não existir ou estiver corrompido, começa vazio."""
    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arq:
            dados = json.load(arq)
    except FileNotFoundError:
        return dados_vazios()
    except json.JSONDecodeError:
        print("Aviso: arquivo de dados corrompido. Começando com dados vazios.")
        return dados_vazios()

    # garante que as 3 listas existam mesmo em um arquivo antigo/incompleto
    for chave in ("areas", "leituras", "relatos"):
        dados.setdefault(chave, [])
    return dados


def salvar_dados(dados):
    try:
        with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arq:
            json.dump(dados, arq, indent=4, ensure_ascii=False)
    except OSError as erro:
        print(f"Erro ao salvar os dados: {erro}")


def agora():
    return datetime.now().strftime(FORMATO_DATA)


def buscar_por_id(lista, identificador):
    """Retorna o dicionário da lista com esse id, ou None."""
    for item in lista:
        if item["id"] == identificador:
            return item
    return None


def ultima_leitura(dados, area_id):
    """Leitura mais recente da área (ou None se ainda não houver)."""
    for leitura in reversed(dados["leituras"]):
        if leitura["area_id"] == area_id:
            return leitura
    return None


def gerar_protocolo(dados):
    return f"SS-{datetime.now().year}-{len(dados['relatos']) + 1:04d}"