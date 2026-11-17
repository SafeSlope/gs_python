"""
Leitura e validação das entradas do usuário.
"""

from config import TIPOS_AREA


def ler_texto(mensagem, tamanho_minimo=2):
    """Repete até receber um texto com pelo menos `tamanho_minimo` caracteres."""
    while True:
        texto = input(mensagem).strip()
        if len(texto) >= tamanho_minimo:
            return texto
        print(f"Entrada inválida: digite ao menos {tamanho_minimo} caracteres.")


def ler_numero(mensagem, minimo, maximo):
    """Repete até receber um número real entre minimo e maximo."""
    while True:
        try:
            valor = float(input(mensagem).strip().replace(",", "."))
        except ValueError:
            print("Entrada inválida: digite um número (ex.: 12,5).")
            continue
        if minimo <= valor <= maximo:
            return valor
        print(f"Valor fora do intervalo permitido ({minimo} a {maximo}).")


def ler_inteiro(mensagem, minimo, maximo):
    """Repete até receber um número inteiro entre minimo e maximo."""
    while True:
        try:
            valor = int(input(mensagem).strip())
        except ValueError:
            print("Entrada inválida: digite um número inteiro.")
            continue
        if minimo <= valor <= maximo:
            return valor
        print(f"Escolha um número entre {minimo} e {maximo}.")


def ler_tipo_area():
    while True:
        tipo = input("Tipo da área (encosta/alagamento): ").strip().lower()
        if tipo in TIPOS_AREA:
            return tipo
        print("Tipo inválido. Digite 'encosta' ou 'alagamento'.")