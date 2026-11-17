ARQUIVO_DADOS = "safeslope_dados.json"
FORMATO_DATA = "%d/%m/%Y %H:%M"

TIPOS_AREA = ("encosta", "alagamento")
TIPOS_RELATO = (
    "Rachadura em parede, muro ou solo",
    "Muro ou árvore inclinados",
    "Entulho ou lixo entupindo córrego/bueiro",
    "Vazamento de água na encosta",
    "Outro ponto de risco",
)
# Fluxo do protocolo: o status só pode avançar, nunca voltar.
STATUS_RELATO = ("RECEBIDO", "EM_ANALISE", "VISTORIADO", "RESOLVIDO")

# Duração da tempestade simulada (horas) - modelo da disciplina de Matemática
DURACAO_TEMPESTADE_H = 6