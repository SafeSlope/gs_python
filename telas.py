"""
Telas compartilhadas entre os perfis (listar e escolher área).
"""

from dados import buscar_por_id
from entradas import ler_inteiro


def listar_areas(dados):
    print("\n--- Áreas monitoradas ---")
    if not dados["areas"]:
        print("Nenhuma área cadastrada ainda (a Defesa Civil cadastra no menu dela).")
        return False
    for a in dados["areas"]:
        print(f"[{a['id']}] {a['nome']} | {a['bairro']} | {a['tipo']}")
    return True


def escolher_area(dados):
    """Mostra as áreas e retorna a escolhida (dict) ou None se voltar."""
    if not listar_areas(dados):
        return None
    ids_validos = [a["id"] for a in dados["areas"]]
    while True:
        escolhido = ler_inteiro("Digite o ID da área (0 para voltar): ", 0, 100000)
        if escolhido == 0:
            return None
        if escolhido in ids_validos:
            return buscar_por_id(dados["areas"], escolhido)
        print("ID não encontrado.")