"""
Regras de negócio: risco, orientação ao morador, prioridade e indicadores.
"""

from datetime import datetime

from config import FORMATO_DATA
from dados import buscar_por_id, ultima_leitura


def relatos_graves_abertos(dados, area_id):
    """Quantidade de relatos de gravidade 4 ou 5 ainda não resolvidos na área."""
    total = 0
    for relato in dados["relatos"]:
        if (relato["area_id"] == area_id
                and relato["gravidade"] >= 4
                and relato["status"] != "RESOLVIDO"):
            total += 1
    return total


def classificar_risco(area, leitura, qtd_relatos_graves):
    """
    Retorna (nivel, pontuacao).
    Base: nível de água medido ÷ limite da área. Aumentam o risco: chuva forte
    (>= 30 mm/h), solo encharcado em encosta (>= 80%) e relatos graves de
    moradores ainda abertos (dado coletado pela própria comunidade).
    """
    pontuacao = leitura["nivel_mm"] / area["limite_mm"] * 100

    if leitura["chuva_mm_h"] >= 30:
        pontuacao += 10
    if area["tipo"] == "encosta" and leitura["umidade_pct"] >= 80:
        pontuacao += 15
    if qtd_relatos_graves > 0:
        pontuacao += 10

    if pontuacao < 50:
        nivel = "NORMAL"
    elif pontuacao < 75:
        nivel = "ATENCAO"
    elif pontuacao < 100:
        nivel = "ALERTA"
    else:
        nivel = "CRITICO"
    return nivel, round(pontuacao, 1)


def acao_recomendada(nivel, tipo_area):
    """Orientação ao morador de acordo com o nível e o tipo de área."""
    match (nivel, tipo_area):
        case ("CRITICO", "encosta"):
            return ("Saia de casa AGORA para um local seguro. Deslizamentos "
                    "podem ocorrer em minutos. Ligue 199 (Defesa Civil).")
        case ("CRITICO", "alagamento"):
            return ("Suba para um local alto e não atravesse a água. "
                    "Ligue 199 (Defesa Civil) ou 193 (Bombeiros).")
        case ("ALERTA", "encosta"):
            return "Separe documentos e remédios, avise vizinhos e esteja pronto para sair."
        case ("ALERTA", "alagamento"):
            return "Suba objetos e documentos do chão e evite passar perto do córrego."
        case ("ATENCAO", _):
            return "Fique atento: acompanhe os alertas e evite áreas de risco."
        case ("NORMAL", _):
            return "Situação estável. Siga a rotina e continue acompanhando."
        case _:
            return "Sem orientação disponível."


def avaliar_area(dados, area):
    """Retorna (nivel, pontuacao, leitura) da área; nivel None se não há leitura."""
    leitura = ultima_leitura(dados, area["id"])
    if leitura is None:
        return None, 0.0, None
    graves = relatos_graves_abertos(dados, area["id"])
    nivel, pontuacao = classificar_risco(area, leitura, graves)
    return nivel, pontuacao, leitura


def calcular_prioridade(relato, pontuacao_area):
    """Quanto maior, mais urgente: gravidade pesa mais, risco da área complementa."""
    return relato["gravidade"] * 10 + pontuacao_area * 0.5


def chave_prioridade(item):
    """Chave de ordenação da fila: o primeiro elemento da tupla é a prioridade."""
    return item[0]


def contar_leituras_criticas(dados):
    """Quantas leituras registradas chegaram ao nível CRITICO."""
    total = 0
    for leitura in dados["leituras"]:
        area = buscar_por_id(dados["areas"], leitura["area_id"])
        if area is None:
            continue
        nivel, _ = classificar_risco(area, leitura, 0)
        if nivel == "CRITICO":
            total += 1
    return total


def horas_entre(data_inicio, data_fim):
    """Diferença em horas entre duas datas de texto; None se o formato falhar."""
    try:
        inicio = datetime.strptime(data_inicio, FORMATO_DATA)
        fim = datetime.strptime(data_fim, FORMATO_DATA)
    except ValueError:
        return None
    return (fim - inicio).total_seconds() / 3600